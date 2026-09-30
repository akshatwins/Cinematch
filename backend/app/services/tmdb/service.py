from app.services.tmdb.client import tmdb
from app.services.tmdb.mapper import map_movie


async def discover(page: int = 1, genre: int | None = None,
                   min_rating: float = 0, year: int | None = None) -> list:
    params = {
        "page": page,
        "sort_by": "popularity.desc",
        "include_adult": "false",
        "include_video": "false",
        "language": "en-US",
        "vote_count.gte": 100,
        "vote_average.gte": min_rating,
    }
    if genre:
        params["with_genres"] = genre
    if year:
        params["primary_release_year"] = year
    data = await tmdb.get("/discover/movie", params)
    return [map_movie(m) for m in data.get("results", [])]


async def search(query: str, page: int = 1) -> list:
    data = await tmdb.get(
        "/search/movie",
        {
            "query": query,
            "page": page,
            "include_adult": "false",
            "language": "en-US",
        },
    )
    return [map_movie(m) for m in data.get("results", [])]


async def details(movie_id: int):
    data = await tmdb.get(
        f"/movie/{movie_id}",
        {
            "language": "en-US",
            "append_to_response": "credits,videos",
        },
    )
    return map_movie(data, detailed=True)


async def genres() -> list[dict]:
    data = await tmdb.get("/genre/movie/list", {"language": "en-US"})
    return data.get("genres", [])
