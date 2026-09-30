from functools import lru_cache
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.schemas.movie import Movie, Recommendation


def _text(movie: Movie) -> str:
    genres = " ".join(g.name for g in movie.genres)
    cast = " ".join(p.name for p in movie.cast)
    director = movie.director.name if movie.director else ""
    return f"{movie.title} {movie.overview} {genres} {cast} {director}"


def rank(source: Movie, candidates: list[Movie], limit: int = 10) -> list[Recommendation]:
    if not candidates:
        return []

    documents = [_text(source)] + [_text(m) for m in candidates]
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(documents)
    content_scores = cosine_similarity(matrix[0:1], matrix[1:]).ravel()

    source_genres = {g.id for g in source.genres}
    source_cast = {p.id for p in source.cast}
    source_director = source.director.id if source.director else None

    max_pop = max((m.popularity for m in candidates), default=1) or 1

    ranked = []
    for i, movie in enumerate(candidates):
        movie_genres = {g.id for g in movie.genres}
        genre = len(source_genres & movie_genres) / max(1, len(source_genres | movie_genres))
        cast = len(source_cast & {p.id for p in movie.cast}) / max(1, len(source_cast))
        director = 1.0 if source_director and movie.director and source_director == movie.director.id else 0.0
        quality = movie.rating / 10
        popularity = min(1.0, np.log1p(movie.popularity) / np.log1p(max_pop))

        score = (
            0.45 * float(content_scores[i])
            + 0.20 * genre
            + 0.10 * cast
            + 0.10 * director
            + 0.10 * quality
            + 0.05 * popularity
        )

        reasons = []
        if genre >= 0.25:
            reasons.append("Shared genres")
        if cast > 0:
            reasons.append("Shared cast")
        if director:
            reasons.append("Same director")
        if content_scores[i] >= 0.10:
            reasons.append("Similar story & themes")
        if movie.rating >= 8:
            reasons.append("Highly rated")
        if not reasons:
            reasons.append("Strong overall similarity")

        ranked.append(
            Recommendation(
                movie=movie,
                score=round(float(score), 4),
                reasons=reasons[:3],
            )
        )

    return sorted(ranked, key=lambda r: r.score, reverse=True)[:limit]
