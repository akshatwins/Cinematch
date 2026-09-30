from fastapi import APIRouter, HTTPException, Query
from app.services.catalog import browse, search_movies, get_movie, recommendations
from app.services.tmdb.service import genres

router = APIRouter(prefix="/api")


@router.get("/health")
async def health():
    from app.services.tmdb.client import tmdb
    return {"status": "ok", "tmdb_configured": tmdb.configured}


@router.get("/movies")
async def movies(
    page: int = Query(1, ge=1, le=500),
    genre: int | None = None,
    min_rating: float = Query(0, ge=0, le=10),
    year: int | None = Query(None, ge=1880, le=2100),
):
    return await browse(page, genre, min_rating, year)


@router.get("/search")
async def search(q: str = Query(..., min_length=1), page: int = Query(1, ge=1, le=500)):
    return await search_movies(q, page)


@router.get("/genres")
async def genre_list():
    try:
        return await genres()
    except Exception:
        return []


@router.get("/movies/{movie_id}")
async def movie(movie_id: int):
    result = await get_movie(movie_id)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return result


@router.get("/movies/{movie_id}/recommendations")
async def movie_recommendations(movie_id: int, limit: int = Query(10, ge=1, le=20)):
    result = await recommendations(movie_id, limit)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found or no recommendations")
    return result
