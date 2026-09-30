# CineMatch V2 Architecture

## Runtime flow

1. Browser requests discovery/search.
2. FastAPI validates parameters.
3. Catalog service requests TMDB.
4. TMDB response is mapped into internal schemas.
5. Movie details can be enriched with credits/videos.
6. Recommendation service builds a hybrid score.
7. Response is returned as stable application-level JSON.

## Recommendation model

The current V2 ranker is an interpretable hybrid baseline:

- 45% TF-IDF content similarity
- 20% genre overlap
- 10% cast overlap
- 10% director match
- 10% rating quality
- 5% popularity

This is deliberately transparent. A production ML iteration can replace the manually weighted ranker with a learned-to-rank model trained on impressions, clicks, likes, watch completion, saves, and skips.

## Scaling

For a real deployment:

```text
CDN
 |
Load Balancer
 |
FastAPI replicas
 |--------|
Redis   PostgreSQL
 |
Recommendation cache / feature store
 |
Offline model training + ingestion jobs
 |
TMDB
```

Use scheduled ingestion for popular/discover catalogs and cache frequently requested details.

## Important boundary

TMDB is a metadata source, not the recommendation model. CineMatch owns the ranking logic. This separation allows the metadata provider to change later without rewriting the recommendation layer.
