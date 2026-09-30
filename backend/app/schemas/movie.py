from pydantic import BaseModel, Field


class Genre(BaseModel):
    id: int
    name: str


class Person(BaseModel):
    id: int
    name: str
    character: str | None = None
    job: str | None = None
    profile_path: str | None = None


class Movie(BaseModel):
    id: int
    title: str
    original_title: str | None = None
    overview: str = ""
    release_date: str | None = None
    year: int | None = None
    rating: float = Field(0, ge=0, le=10)
    vote_count: int = 0
    popularity: float = 0
    poster_url: str | None = None
    backdrop_url: str | None = None
    genres: list[Genre] = []
    cast: list[Person] = []
    director: Person | None = None
    runtime: int | None = None
    trailer_url: str | None = None
    tmdb_url: str


class Recommendation(BaseModel):
    movie: Movie
    score: float
    reasons: list[str]
