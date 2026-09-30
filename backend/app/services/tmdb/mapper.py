from datetime import date
from app.schemas.movie import Movie, Genre, Person
from app.services.tmdb.client import tmdb


def _person(p: dict, role: str | None = None) -> Person:
    return Person(
        id=p.get("id", 0),
        name=p.get("name", ""),
        character=p.get("character"),
        job=role or p.get("job"),
        profile_path=tmdb.image_url(p.get("profile_path"), "w185"),
    )


def map_movie(data: dict, detailed: bool = False) -> Movie:
    credits = data.get("credits", {})
    crew = credits.get("crew", [])
    director_raw = next((p for p in crew if p.get("job") == "Director"), None)
    cast = [_person(p) for p in credits.get("cast", [])[:10]]
    genres = [
        Genre(id=g["id"], name=g["name"])
        for g in data.get("genres", [])
    ]
    if not genres:
        genres = [Genre(id=g, name=str(g)) for g in data.get("genre_ids", [])]

    release_date = data.get("release_date") or None
    year = None
    if release_date:
        try:
            year = int(release_date[:4])
        except ValueError:
            pass

    trailer = None
    for v in data.get("videos", {}).get("results", []):
        if v.get("site") == "YouTube" and v.get("type") == "Trailer":
            trailer = f"https://www.youtube.com/watch?v={v['key']}"
            break

    return Movie(
        id=data["id"],
        title=data.get("title") or data.get("name", "Untitled"),
        original_title=data.get("original_title"),
        overview=data.get("overview") or "",
        release_date=release_date,
        year=year,
        rating=float(data.get("vote_average") or 0),
        vote_count=int(data.get("vote_count") or 0),
        popularity=float(data.get("popularity") or 0),
        poster_url=tmdb.image_url(data.get("poster_path"), "w500"),
        backdrop_url=tmdb.image_url(data.get("backdrop_path"), "w1280"),
        genres=genres,
        cast=cast,
        director=_person(director_raw, "Director") if director_raw else None,
        runtime=data.get("runtime"),
        trailer_url=trailer,
        tmdb_url=f"https://www.themoviedb.org/movie/{data['id']}",
    )
