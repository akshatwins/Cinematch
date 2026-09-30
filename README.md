# CineMatch V2 — Production-Ready Movie Recommendation Platform

CineMatch V2 is a full-stack movie discovery and recommendation platform designed as a serious data-science/software-engineering portfolio project.

It uses **TMDB as the live movie metadata source**, a FastAPI backend, a hybrid recommendation layer, PostgreSQL/Redis-ready infrastructure, a responsive frontend, automated tests, Docker, and CI.

> **TMDB notice:** This product uses the TMDB API but is not endorsed or certified by TMDB. TMDB attribution is included in the application.

## What makes V2 different from a college demo?

- Live movie metadata and posters through TMDB.
- Search, discovery, detail pages and recommendation endpoints.
- Secure server-side API credential handling.
- Hybrid ranking instead of a single cosine-similarity call.
- Repository/service architecture.
- PostgreSQL-ready persistence layer.
- Redis-ready caching layer.
- Health/readiness endpoints.
- Structured configuration.
- Docker Compose for local infrastructure.
- Automated tests and GitHub Actions.
- Production deployment notes.
- Graceful fallback to a bundled seed catalog when TMDB is not configured.

## Features

### Discovery
- Trending/popular movies
- Search
- Genre filtering
- Rating filtering
- Year filtering
- Pagination

### Movie details
- Poster and backdrop
- Overview
- Ratings and vote count
- Genres
- Cast
- Director
- Runtime
- Trailer/video metadata when available
- TMDB source link

### Recommendations
Hybrid score:

```text
45% content similarity
20% genre overlap
10% cast similarity
10% director similarity
10% quality
5% popularity
```

The architecture is deliberately modular so these weights can later be learned from user interaction data.

## Required setup

### 1. Create a TMDB account and API credential

TMDB provides an API key and an API Read Access Token in account/API settings.

For V2, use the **API Read Access Token**:

```env
TMDB_ACCESS_TOKEN=your_token_here
```

Do NOT put the real token in GitHub.

### 2. Configure environment

Copy:

```text
.env.example
```

to:

```text
.env
```

Then set:

```env
TMDB_ACCESS_TOKEN=your_token
DATABASE_URL=sqlite:///./cinematch.db
REDIS_URL=
```

The app can run without PostgreSQL/Redis initially. Docker Compose includes PostgreSQL and Redis when you want the full stack.

## Run without Docker

```bash
cd backend
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Run the complete infrastructure

From the project root:

```bash
docker compose up --build
```

Then open:

```text
http://localhost:8000
```

## API endpoints

```text
GET /api/health
GET /api/movies
GET /api/search?q=inception
GET /api/movies/{tmdb_id}
GET /api/movies/{tmdb_id}/recommendations
GET /api/genres
```

## Architecture

```text
                         ┌──────────────────┐
                         │  Browser / SPA    │
                         └────────┬─────────┘
                                  │ HTTP
                         ┌────────▼─────────┐
                         │    FastAPI       │
                         │ API + Validation │
                         └───┬──────────┬───┘
                             │          │
                    ┌────────▼───┐  ┌──▼──────────┐
                    │ TMDB Client│  │ Recommender │
                    └──────┬─────┘  └────┬────────┘
                           │              │
                    ┌──────▼──────┐ ┌────▼──────┐
                    │ TMDB API    │ │ Cache/DB  │
                    └─────────────┘ └───────────┘
```

## Data strategy

TMDB is the live source for movie metadata, images, credits, videos and discovery. The project also includes a tiny seed catalog so the UI and API can be evaluated without credentials.

For production, use a persistent database/cache and a scheduled ingestion process instead of repeatedly fetching the same data from TMDB.

## Security

- Credentials are loaded from environment variables.
- `.env` is ignored by Git.
- TMDB credentials never reach browser JavaScript.
- CORS is configurable.
- Request timeouts are configured.
- External API failures degrade gracefully.

## Testing

```bash
cd backend
pytest -q
```

## Production roadmap

The codebase is ready for the next layers:

1. User accounts.
2. Watch history and likes.
3. User-item collaborative filtering.
4. Learned ranking from interactions.
5. PostgreSQL persistence.
6. Redis caching.
7. Celery/RQ scheduled ingestion.
8. Vector embeddings for semantic retrieval.
9. A/B testing of ranking models.
10. Observability and analytics.

## TMDB attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

See `frontend/index.html` and `docs/DEPLOYMENT.md` for attribution guidance.

## License

MIT for the project code. Third-party movie data/images remain subject to their respective terms and licenses.
