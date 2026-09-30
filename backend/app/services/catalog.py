from app.services.tmdb.service import discover, search, details
from app.services.recommendations.hybrid import rank
from app.seed import SEED_MOVIES


async def browse(page=1, genre=None, min_rating=0, year=None):
    if page == 1:
        try:
            return await discover(page, genre, min_rating, year)
        except Exception:
            pass
    return SEED_MOVIES[:20]


async def search_movies(query: str, page=1):
    try:
        return await search(query, page)
    except Exception:
        q = query.lower()
        return [m for m in SEED_MOVIES if q in m.title.lower()][:20]


async def get_movie(movie_id: int):
    try:
        return await details(movie_id)
    except Exception:
        return next((m for m in SEED_MOVIES if m.id == movie_id), None)


async def recommendations(movie_id: int, limit=10):
    source = await get_movie(movie_id)
    if not source:
        return []
    candidates = await browse(page=1)
    candidates = [m for m in candidates if m.id != source.id]
    return rank(source, candidates, limit)
