# Deployment

## Environment variables

Required:

```env
TMDB_ACCESS_TOKEN=...
```

Recommended production settings:

```env
ENVIRONMENT=production
DATABASE_URL=postgresql+psycopg://...
REDIS_URL=redis://...
CORS_ORIGINS=https://your-domain.example
```

## Secrets

Never commit `.env`, access tokens, passwords, or private keys.

Use your deployment provider's secret manager/environment configuration.

## TMDB attribution

The application must retain TMDB attribution and follow TMDB's current API/branding requirements. The current UI includes:

> This product uses the TMDB API but is not endorsed or certified by TMDB.

Review the latest TMDB developer terms before commercial deployment.

## Deployment options

The Dockerized backend can be deployed to services such as Render, Railway, Fly.io, AWS, Azure or Google Cloud. Use a managed PostgreSQL and Redis service for production.

## Health checks

Use:

```text
GET /api/health
```

as the container health endpoint.

## Recommended production hardening

- HTTPS only
- secret manager
- restricted CORS
- structured logging
- request IDs
- rate limiting
- Redis response caching
- database connection pooling
- error tracking
- metrics and tracing
- background ingestion jobs
