# 🎬 CineMatch V2

### Intelligent Movie Discovery & Recommendation Platform

<p align="center">
  <strong>A production-oriented movie recommendation platform powered by TMDB, FastAPI, machine learning, and a hybrid recommendation engine.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.116-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/TMDB-API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white" alt="TMDB">
  <img src="https://img.shields.io/badge/Machine%20Learning-Hybrid-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</p>

---

## 📌 Overview

**CineMatch V2** is a full-stack movie discovery and recommendation platform designed to provide intelligent, explainable, and personalized-style movie recommendations.

The platform integrates **live movie information from TMDB** with a hybrid recommendation engine that analyzes movie content, genres, cast, directors, ratings, and popularity.

Unlike a basic movie recommendation demo, CineMatch V2 is structured around a production-oriented architecture with:

- ⚡ FastAPI backend
- 🤖 Machine-learning recommendation engine
- 🎬 Live TMDB movie data
- 🔎 Movie search and discovery
- 🎯 Hybrid recommendation scoring
- 🧠 TF-IDF and cosine similarity
- 📊 Explainable recommendation reasons
- 🗄️ PostgreSQL-ready architecture
- ⚡ Redis-ready architecture
- 🐳 Docker and Docker Compose
- 🧪 Automated testing
- 🔄 GitHub Actions CI
- 📱 Responsive frontend

---

# ✨ Features

## 🎬 Movie Discovery

- Browse popular movies
- Discover movies by genre
- Filter movies by rating
- Filter movies by release year
- Search movies using TMDB
- View detailed movie information
- View posters and backdrops
- View trailers when available

## 👥 Movie Details

Each movie can provide information such as:

- Title
- Overview
- Release date
- Genres
- Runtime
- Rating
- Vote count
- Popularity
- Director
- Cast
- Trailer
- Similar/recommended movies

## 🤖 Hybrid Recommendation Engine

CineMatch combines multiple signals instead of relying on a single similarity metric.

| Recommendation Signal | Weight |
|---|---:|
| Content Similarity | 45% |
| Genre Similarity | 20% |
| Cast Similarity | 10% |
| Director Similarity | 10% |
| Rating Quality | 10% |
| Popularity | 5% |

### Recommendation Formula

```text
Final Score =
    Content Similarity × 0.45
  + Genre Similarity × 0.20
  + Cast Similarity × 0.10
  + Director Similarity × 0.10
  + Rating Quality × 0.10
  + Popularity × 0.05
```

This allows CineMatch to combine machine-learning similarity with movie quality and popularity signals.

---

# 🧠 Machine Learning

CineMatch uses **TF-IDF vectorization** to transform movie metadata into numerical representations.

The recommendation pipeline uses:

```text
Movie Metadata
      │
      ▼
Text Processing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Content Similarity
      │
      ├── Genre Similarity
      ├── Cast Similarity
      ├── Director Similarity
      ├── Rating Quality
      └── Popularity
              │
              ▼
       Hybrid Scoring
              │
              ▼
      Ranked Recommendations
```

---

# 💡 Explainable Recommendations

CineMatch does not only return a list of movies.

It can also provide reasoning behind recommendations, such as:

```text
Recommended because it has:
✓ Similar genres
✓ Similar movie content
✓ Related cast
✓ Same director
✓ Strong audience rating
```

This makes the recommendation system easier to understand and demonstrate.

---

# 🌐 TMDB Integration

CineMatch uses the **TMDB API** as its primary movie data source.

The application can retrieve:

- Movies
- Search results
- Genres
- Movie details
- Cast
- Directors
- Videos
- Trailers
- Popularity information
- Ratings

> This product uses the TMDB API but is not endorsed or certified by TMDB.

---

# 🏗️ Project Architecture

```text
                         ┌──────────────────────┐
                         │       Frontend       │
                         │   HTML / CSS / JS    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI API     │
                         │       Backend        │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
             ┌────────────┐  ┌────────────┐  ┌────────────┐
             │    TMDB    │  │Recommendation│ │ PostgreSQL │
             │    API     │  │   Engine     │  │   Ready    │
             └────────────┘  └────────────┘  └────────────┘
                                    │
                                    ▼
                             ┌────────────┐
                             │   Redis    │
                             │   Ready    │
                             └────────────┘
```

---

# 📁 Project Structure

```text
CineMatch/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── db/
│   │   │
│   │   ├── models/
│   │   │
│   │   ├── schemas/
│   │   │   └── movie.py
│   │   │
│   │   ├── services/
│   │   │   ├── catalog.py
│   │   │   │
│   │   │   ├── recommendations/
│   │   │   │   └── hybrid.py
│   │   │   │
│   │   │   └── tmdb/
│   │   │       ├── client.py
│   │   │       ├── mapper.py
│   │   │       └── service.py
│   │   │
│   │   ├── seed.py
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── test_api.py
│   │   └── test_recommendations.py
│   │
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── assets/
│
├── docs/
│   ├── ARCHITECTURE.md
│   └── DEPLOYMENT.md
│
├── scripts/
│   └── run_local.sh
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .env.example
├── .gitignore
├── LICENSE
├── PROJECT_STATUS.md
└── README.md
```

---

# 🛠️ Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API
- Responsive UI

## Backend

- Python 3.12
- FastAPI
- Pydantic
- HTTPX
- Uvicorn

## Machine Learning

- Scikit-learn
- TF-IDF
- Cosine Similarity
- Hybrid Recommendation

## Data

- TMDB API
- PostgreSQL-ready architecture
- Seed fallback dataset

## Infrastructure

- Docker
- Docker Compose
- Redis
- PostgreSQL
- GitHub Actions

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | API health check |
| `GET` | `/api/movies` | Discover movies |
| `GET` | `/api/search` | Search movies |
| `GET` | `/api/genres` | Get movie genres |
| `GET` | `/api/movies/{movie_id}` | Get movie details |
| `GET` | `/api/movies/{movie_id}/recommendations` | Get recommendations |

---

# 🔐 Environment Configuration

Create a `.env` file in the project root.

```env
TMDB_ACCESS_TOKEN=YOUR_TMDB_ACCESS_TOKEN

TMDB_BASE_URL=https://api.themoviedb.org/3
TMDB_IMAGE_BASE_URL=https://image.tmdb.org/t/p

DATABASE_URL=postgresql+psycopg://cinematch:cinematch@postgres:5432/cinematch

REDIS_URL=redis://redis:6379/0

CORS_ORIGINS=*

REQUEST_TIMEOUT_SECONDS=15
```

### ⚠️ Security

Never upload your actual `.env` file or TMDB credentials to GitHub.

The repository already contains:

```text
.env.example
.gitignore
```

Use `.env.example` as the template for your local configuration.

---

# 🔑 Getting a TMDB API Credential

1. Create a TMDB account.
2. Open your TMDB account settings.
3. Go to the API section.
4. Generate an API credential.
5. Copy the access token.
6. Add it to your `.env` file.

Example:

```env
TMDB_ACCESS_TOKEN=your_real_token_here
```

Do **not** place the token directly inside Python or JavaScript source files.

---

# 🚀 Running Locally

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CineMatch.git
cd CineMatch
```

## 2. Create the environment file

```bash
cp .env.example .env
```

On Windows:

```powershell
copy .env.example .env
```

Add your TMDB access token to `.env`.

---

## 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 5. Start the application

```bash
uvicorn backend.app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🐳 Docker

CineMatch includes Docker support for a more consistent development and deployment environment.

## Build and start

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d --build
```

Stop the services:

```bash
docker compose down
```

---

# 🗄️ Infrastructure

The Docker architecture is prepared for:

```text
┌──────────────────────────┐
│       CineMatch API      │
│         FastAPI          │
└────────────┬─────────────┘
             │
       ┌─────┴─────┐
       │           │
       ▼           ▼
┌────────────┐ ┌────────────┐
│ PostgreSQL │ │   Redis    │
│  Database  │ │   Cache    │
└────────────┘ └────────────┘
```

PostgreSQL provides persistent data storage while Redis can be used for caching frequently requested data.

---

# 🧪 Testing

The project includes automated backend tests.

Run:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

The test suite covers API behavior and recommendation logic.

---

# 🔄 Continuous Integration

GitHub Actions is configured through:

```text
.github/
└── workflows/
    └── ci.yml
```

The CI workflow automatically:

1. Sets up Python
2. Installs dependencies
3. Runs the test suite
4. Reports failures through GitHub Actions

---

# 📊 Recommendation Pipeline

```text
User selects a movie
        │
        ▼
Retrieve movie information
        │
        ▼
Extract metadata
        │
        ├── Overview
        ├── Genres
        ├── Cast
        ├── Director
        ├── Rating
        └── Popularity
        │
        ▼
Generate similarity signals
        │
        ▼
Calculate hybrid score
        │
        ▼
Rank candidate movies
        │
        ▼
Return recommendations
        │
        ▼
Display results + explanation
```

---

# 🎯 Project Goals

CineMatch was designed to demonstrate practical implementation of:

- Machine Learning
- Recommendation Systems
- Natural Language Processing
- REST API development
- Full-stack development
- External API integration
- Database architecture
- Caching architecture
- Docker deployment
- Automated testing
- CI/CD
- Explainable recommendations

---

# 🔮 Future Roadmap

## V3 — Personalization

Potential improvements:

- User accounts
- Watch history
- Favorites
- Ratings
- Personalized recommendations
- User preference profiles
- Collaborative filtering
- User-item recommendation matrix

## V4 — Advanced Recommendation Intelligence

Potential improvements:

- Deep-learning recommendation models
- Embeddings
- Vector database
- Semantic search
- Personalized ranking
- Real-time recommendation updates
- Advanced analytics
- Recommendation A/B testing

---

# 🔒 Production Security

For production deployment, the following practices should be implemented:

- Store secrets in environment variables
- Never commit API keys
- Use HTTPS
- Restrict CORS origins
- Add API rate limiting
- Validate incoming requests
- Use secure database credentials
- Enable production logging
- Monitor application health
- Keep dependencies updated

---

# 📱 Responsive Interface

The CineMatch frontend is designed to work across:

- 💻 Desktop
- 💻 Laptop
- 📱 Mobile
- 📱 Tablet

The interface adapts its movie cards, navigation, search controls, and recommendation sections according to screen size.

---

# 📈 Project Status

**Current Version:** `V2.0`

**Status:** Production-oriented development build

### Implemented

- [x] FastAPI backend
- [x] TMDB integration
- [x] Movie search
- [x] Movie discovery
- [x] Genre filtering
- [x] Movie details
- [x] Cast and director information
- [x] Trailer support
- [x] Hybrid recommendation engine
- [x] TF-IDF similarity
- [x] Cosine similarity
- [x] Explainable recommendations
- [x] Responsive frontend
- [x] Docker support
- [x] PostgreSQL-ready architecture
- [x] Redis-ready architecture
- [x] Automated tests
- [x] GitHub Actions CI
- [x] Environment-based configuration

---

# 👨‍💻 Developer

**CineMatch** is developed as a professional portfolio project demonstrating the integration of:

```text
Data Science
      +
Machine Learning
      +
Backend Engineering
      +
Frontend Development
      +
API Integration
      +
Software Architecture
```

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 🙏 Attribution

Movie information and images are provided through the TMDB API.

> This product uses the TMDB API but is not endorsed or certified by TMDB.

TMDB is a trademark of their respective owners.

---

<p align="center">
  <strong>🎬 CineMatch V2</strong>
  <br>
  Intelligent Movie Discovery & Recommendation Platform
  <br><br>
  Built with Python • FastAPI • Machine Learning • TMDB • JavaScript
</p>
