from app.services.recommendations.hybrid import rank
from app.seed import SEED_MOVIES


def test_hybrid_recommender_returns_ranked_items():
    source = SEED_MOVIES[0]
    results = rank(source, SEED_MOVIES[1:], limit=3)
    assert len(results) == 3
    assert all(0 <= r.score <= 1 for r in results)
    assert all(r.movie.id != source.id for r in results)
