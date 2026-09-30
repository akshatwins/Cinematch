🎬 CineMatch V2 — Movie Recommendation System

«Discover movies. Understand your taste. Find what to watch next.»

CineMatch V2 is a production-oriented movie discovery and recommendation platform built with Python, FastAPI, machine-learning techniques, and the TMDB API.

Unlike a basic movie recommendation college project that relies on a small static CSV file and a single similarity calculation, CineMatch is designed as a scalable full-stack system with live movie metadata, hybrid recommendation ranking, API architecture, caching/database readiness, Docker support, automated testing, and a modern responsive interface.

---

✨ Overview

CineMatch combines live movie metadata from The Movie Database (TMDB) with an interpretable hybrid recommendation engine.

Users can:

- 🔎 Search for movies
- 🎬 Discover popular movies
- 🎭 Filter movies by genre
- ⭐ Filter movies by rating
- 📅 Filter movies by release year
- 📖 View detailed movie information
- 👥 Explore cast and director information
- ▶️ Access available trailers
- 🧠 Get similar movie recommendations
- 💡 Understand why a movie was recommended

The architecture is designed so the recommendation engine can later evolve from a content-based baseline into a fully personalized recommendation system using user interaction data.

---

🚀 Features

🎥 Live Movie Discovery

CineMatch integrates with the TMDB API to retrieve current movie metadata including:

- Movie titles
- Original titles
- Release dates
- Genres
- Movie descriptions
- Ratings
- Vote counts
- Popularity
- Posters
- Backdrops
- Cast
- Directors
- Runtime
- Trailers

The application does not expose the TMDB credential to the frontend.

---

🔍 Intelligent Search

Users can search for movies using the CineMatch search interface.

Example:

Inception
Interstellar
Batman
Dune
Spider-Man

Search requests are handled through the FastAPI backend and forwarded securely to TMDB.

---

🧠 Hybrid Recommendation Engine

CineMatch does not rely on a single similarity metric.

The current recommendation model combines multiple signals:

Signal| Weight
Content similarity| 45%
Genre similarity| 20%
Cast similarity| 10%
Director similarity| 10%
Rating quality| 10%
Popularity| 5%

Content Similarity

Movie descriptions and metadata are converted into TF-IDF vectors.

The system then calculates:

Cosine Similarity

to identify movies with similar textual characteristics.

Genre Similarity

The system calculates genre overlap between the selected movie and candidate movies.

Cast Similarity

Shared actors contribute to the recommendation score.

Director Similarity

Movies directed by the same filmmaker receive an additional similarity signal.

Rating Quality

Higher-rated movies receive a quality contribution to the ranking.

Popularity

Popularity contributes a smaller signal so that highly discovered movies can surface without completely dominating the recommendation model.

---

💡 Explainable Recommendations

CineMatch doesn't just return a recommendation score.

It also generates human-readable reasons such as:

Shared genres
Shared cast
Same director
Similar story & themes
Highly rated

Example:

Interstellar
94% match

Shared genres · Similar story & themes · Highly rated

This makes the recommendation system more interpretable.

---

🏗️ System Architecture

                    ┌─────────────────────┐
                    │       Browser       │
                    │   CineMatch Web UI  │
                    └──────────┬──────────┘
                               │
                               │ HTTP
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │     REST API        │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
        ┌────────────┐ ┌─────────────┐ ┌─────────────┐
        │ TMDB API   │ │ Recommender │ │ PostgreSQL  │
        │            │ │   Engine    │ │   Ready     │
        └────────────┘ └─────────────┘ └─────────────┘
                              │
                              ▼
                         ┌─────────┐
                         │  Redis  │
                         │  Ready  │
                         └─────────┘

---

📁 Project Structure

CineMatch/
│
├── backend/
│   │
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
├── docker-compose.yml
├── .env.example
├── .gitignore
├── LICENSE
├── PROJECT_STATUS.md
└── README.md

---

🛠️ Technology Stack

Backend

- Python
- FastAPI
- Pydantic
- HTTPX
- Scikit-learn
- NumPy

Machine Learning

- TF-IDF Vectorization
- Cosine Similarity
- Feature Engineering
- Hybrid Ranking
- Content-Based Recommendation

Data

- TMDB API
- PostgreSQL-ready architecture
- Seed fallback dataset

Caching

- Redis-ready architecture

Frontend

- HTML5
- CSS3
- JavaScript
- Responsive UI
- Native Fetch API

DevOps

- Docker
- Docker Compose
- GitHub Actions
- Automated tests
- Environment-based configuration

---

🔐 Environment Configuration

Create a ".env" file from:

.env.example

Example:

APP_NAME=CineMatch
ENVIRONMENT=development

TMDB_ACCESS_TOKEN=your_tmdb_access_token

TMDB_BASE_URL=https://api.themoviedb.org/3
TMDB_IMAGE_BASE_URL=https://image.tmdb.org/t/p

DATABASE_URL=sqlite:///./cinematch.db
REDIS_URL=

CORS_ORIGINS=http://localhost:8000

REQUEST_TIMEOUT_SECONDS=8

Important

Never commit your actual ".env" file.

The repository already contains:

.gitignore

with ".env" excluded.

---

🔑 TMDB API Setup

CineMatch V2 uses TMDB for live movie information.

Create your TMDB developer account and obtain an API credential.

The application expects:

TMDB_ACCESS_TOKEN=your_token_here

The token is used exclusively by the backend.

It is not exposed to browser JavaScript.

---

▶️ Running Locally

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/CineMatch.git
cd CineMatch

---

2. Create a virtual environment

cd backend
python -m venv .venv

Windows

.venv\Scripts\activate

macOS/Linux

source .venv/bin/activate

---

3. Install dependencies

pip install -r requirements.txt

---

4. Configure environment

Create:

.env

from:

.env.example

Add your TMDB credential:

TMDB_ACCESS_TOKEN=YOUR_TOKEN

---

5. Start the application

From the "backend" directory:

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000

---

📚 API Documentation

FastAPI automatically generates interactive API documentation.

Open:

http://127.0.0.1:8000/docs

Alternative OpenAPI documentation:

http://127.0.0.1:8000/redoc

---

🔌 API Endpoints

Health

GET /api/health

Example response:

{
  "status": "ok",
  "tmdb_configured": true
}

---

Movie Discovery

GET /api/movies

Optional parameters:

page
genre
min_rating
year

Example:

/api/movies?page=1&min_rating=8

---

Search

GET /api/search?q=inception

---

Movie Details

GET /api/movies/{movie_id}

Example:

/api/movies/27205

---

Recommendations

GET /api/movies/{movie_id}/recommendations

Example:

/api/movies/27205/recommendations?limit=10

---

Genres

GET /api/genres

---

🐳 Docker

CineMatch includes Docker support.

Build the backend:

docker build -t cinematch ./backend

Run:

docker run -p 8000:8000 --env-file .env cinematch

---

🐘 Full Development Infrastructure

The project includes:

docker-compose.yml

which provides:

FastAPI
PostgreSQL
Redis

Start everything:

docker compose up --build

The application will be available at:

http://localhost:8000

---

🧪 Testing

Run:

cd backend
pytest -q

The test suite covers:

- API health endpoint
- Movie endpoint
- Recommendation ranking
- Recommendation score validation
- Source-movie exclusion

---

⚙️ Continuous Integration

GitHub Actions automatically runs the test suite whenever code is pushed or a pull request is opened.

Workflow:

.github/workflows/ci.yml

Pipeline:

GitHub
   ↓
Checkout
   ↓
Python 3.12
   ↓
Install dependencies
   ↓
Run tests

---

🗄️ Database Architecture

PostgreSQL is included in the Docker development infrastructure.

The architecture is intentionally separated so persistent models can be introduced without changing the recommendation interface.

Potential production entities include:

users
movies
genres
people
movie_cast
movie_genres
ratings
watch_history
favorites
recommendation_events

---

⚡ Redis Architecture

Redis is included as a production-ready dependency.

Potential cache keys:

movie:{id}
search:{query}:{page}
discover:{filters}:{page}
recommendations:{movie_id}
genres

This reduces repeated calls to external services and improves response latency.

---

🧠 Recommendation Architecture

The current recommendation pipeline is intentionally interpretable.

Movie
  │
  ├── Overview
  ├── Genres
  ├── Cast
  ├── Director
  ├── Rating
  └── Popularity
        │
        ▼
Feature Engineering
        │
        ▼
TF-IDF Representation
        │
        ▼
Cosine Similarity
        │
        ├── Genre Similarity
        ├── Cast Similarity
        ├── Director Similarity
        ├── Rating Quality
        └── Popularity
        │
        ▼
Hybrid Ranking
        │
        ▼
Top-N Recommendations

---

📈 Future Personalization

The current V2 system is primarily a content-based hybrid recommender.

The next generation can introduce actual user personalization.

Potential signals:

Movie clicks
Movie views
Likes
Dislikes
Favorites
Watch history
Watch completion
Search history
Genre preferences
Actor preferences
Director preferences

These signals can eventually power:

Collaborative Filtering

User × Movie interaction matrix

Embedding-based Retrieval

Movie embeddings
        ↓
Vector search
        ↓
Semantic candidates

Learned Ranking

Candidate movies
       ↓
Feature engineering
       ↓
Learning-to-rank model
       ↓
Personalized recommendations

---

📊 Production Recommendation Roadmap

V2

- Live TMDB metadata
- Content-based recommendations
- Hybrid ranking
- API architecture
- Docker
- Redis-ready
- PostgreSQL-ready

V3

- User authentication
- Profiles
- Watch history
- Likes/dislikes
- Favorites
- Personalized recommendations
- Collaborative filtering

V4

- Learned recommendation ranking
- Vector embeddings
- Semantic search
- Recommendation analytics
- A/B testing
- Model monitoring

---

🔒 Security

CineMatch follows several basic security principles:

- API credentials remain server-side.
- ".env" is excluded from Git.
- Configuration is environment-driven.
- External API requests use timeouts.
- FastAPI validates request parameters.
- CORS can be restricted for production.
- Docker secrets/environment configuration can be used during deployment.

Before production deployment, additional controls should be enabled:

- HTTPS
- authentication
- authorization
- rate limiting
- secret manager
- structured logging
- monitoring
- request tracing
- database connection pooling

---

🌐 Deployment

The Dockerized backend can be deployed to cloud platforms supporting containers.

Typical architecture:

                 Internet
                    │
                    ▼
              Load Balancer
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    FastAPI Instance     FastAPI Instance
          │                   │
          └─────────┬─────────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Redis              PostgreSQL
                    │
                    ▼
                  TMDB

See:

docs/DEPLOYMENT.md

for deployment guidance.

---

🎨 Frontend

The CineMatch frontend is intentionally lightweight.

It uses:

- HTML
- CSS
- Vanilla JavaScript
- Fetch API

There is currently no mandatory frontend build system.

This makes the project easy to understand, deploy and modify while keeping the backend architecture production-oriented.

---

📱 Responsive Design

The interface supports:

- Desktop
- Tablet
- Mobile

The UI automatically adapts movie grids, navigation, search and movie-detail layouts to smaller screens.

---

🧩 Design Principles

CineMatch follows several engineering principles:

Separation of concerns

API routes, TMDB integration, recommendation logic, configuration and frontend code are separated.

Provider abstraction

TMDB is treated as a metadata provider rather than being tightly coupled to recommendation logic.

Explainability

Recommendation signals are transparent.

Graceful degradation

When TMDB credentials or network access are unavailable, the system can use its bundled seed catalog.

Production path

PostgreSQL, Redis, background jobs and personalized ML can be added without replacing the entire architecture.

---

⚠️ Data & Licensing

Movie metadata and images retrieved from TMDB are subject to the applicable TMDB terms and policies.

CineMatch's source code is separate from third-party movie data.

Do not redistribute third-party movie artwork unless you have the appropriate rights or license.

---

🙏 Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

Movie metadata and imagery are provided by The Movie Database (TMDB).

"TMDB" (https://www.themoviedb.org/)

---

👨‍💻 Project Purpose

CineMatch was built as a portfolio-level demonstration of:

- Data science
- Machine learning
- Recommendation systems
- Natural language processing
- Backend engineering
- REST API design
- Database architecture
- Caching
- Docker
- Testing
- CI/CD
- Frontend development
- Production-oriented software architecture

The goal is to demonstrate how a recommendation algorithm can be integrated into a complete software product rather than presented as an isolated notebook.

---

📌 Current Status

Version: "2.0.0"

Implemented

- [x] TMDB integration
- [x] Live movie discovery
- [x] Movie search
- [x] Movie details
- [x] Genre filtering
- [x] Rating filtering
- [x] Hybrid recommendations
- [x] Recommendation explanations
- [x] Responsive frontend
- [x] FastAPI REST API
- [x] Swagger documentation
- [x] Docker
- [x] Docker Compose
- [x] PostgreSQL infrastructure
- [x] Redis infrastructure
- [x] Automated tests
- [x] GitHub Actions CI
- [x] Environment-based secrets
- [x] Offline fallback dataset

Planned

- [ ] User authentication
- [ ] User profiles
- [ ] Watch history
- [ ] Likes/dislikes
- [ ] Favorites
- [ ] Collaborative filtering
- [ ] Personalized ranking
- [ ] Vector search
- [ ] Recommendation analytics
- [ ] A/B testing
- [ ] Model monitoring

---

📄 License

MIT License for the CineMatch project source code.

Third-party APIs, metadata, images and other external assets remain subject to their respective licenses and terms.

---

⭐ If you find this project useful

Consider starring the repository and exploring the architecture.

CineMatch — turning movie discovery into a recommendation system.
