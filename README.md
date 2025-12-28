# SpotifyAPI

Authors
- Carlos Andres Gomez Orduz
- Gustavo Mena Orduz

---

## Overview

SpotifyAPI is a data engineering and analytics project designed to analyze artist and track popularity trends — with an emphasis on Colombia — using the Spotify Web API. The repository contains ingestion pipelines, ETL components, persistence to PostgreSQL, and tooling for prototyping (pandas).

Primary research goals include:
- Measuring time-to-recognition across regions and genres (e.g., reggaeton artists in Puerto Rico vs. Colombia).
- Estimating time to reach milestones (e.g., 1 million monthly streams) by genre and region.
- Quantifying the impact of collaborations/remixes across genres and geographies.
- Evaluating how release frequency affects long-term artist popularity.

---

## Key Features

- Spotify Web API ingestion to fetch artists, tracks, popularity, and temporal metrics.
- Modular ETL pipelines.
- PostgreSQL persistence via psycopg2 and SQLAlchemy models.
- Test suite using pytest for unit and integration tests.
- Docker and Docker Compose for reproducible local environments.
- Initialization scripts (in `init/`) for DB and environment bootstrapping.
- Architecture diagram: `carl_og.drawio`.

---

## Technology Stack

- Language: Python
- Data / processing:
  - pandas
  - numpy
- HTTP/API:
  - requests
- Database:
  - PostgreSQL (psycopg2-binary)
  - SQLAlchemy (ORM)
- Tooling & testing:
  - pytest
  - argparse
  - json5
- Containerization:
  - Docker
  - Docker Compose

Dependencies (from `requirements.txt`):
- json5
- numpy==1.23.5
- pandas==1.5.3
- argparse
- psycopg2-binary==2.9.10
- pyspark==3.5.5
- pytest==7.1.2
- requests
- SQLAlchemy

---

## Repository Layout (top-level)

- `src/` — source code (ETL, ingestion, utilities)
- `init/` — initialization scripts for DB or dataset seeding
- `tests/` — test suite (pytest)
- `requirements.txt` — Python dependencies
- `docker-compose.yml` — service composition (e.g., postgres)
- `dockerfile` — app image build (note: file name is `dockerfile` in repo)
- `.vscode/` — editor settings
- `carl_og.drawio` — architecture/diagram file

---

## Prerequisites

- Git
- Python 3.8+ (or the version compatible with the project)
- pip
- (Optional) Docker & Docker Compose — recommended to reproduce DB and services
- (Optional) Apache Spark installation or use via Docker if running PySpark jobs locally

---

## Quick Start

Clone repository:
```bash
git clone https://github.com/CarloosG/SpotifyAPI.git
cd SpotifyAPI
```

Option A — Start with Docker Compose (recommended)
```bash
# make sure Docker and Docker Compose are installed
docker-compose up -d
# follow logs if necessary
docker-compose logs -f
```
- Inspect `docker-compose.yml` to confirm service names (e.g., postgres).
- If `init/` contains DB initialization scripts, ensure they run either automatically via Compose or run them manually.

Option B — Local Python environment
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file or export these variables in your environment. Example `.env` template:
```env
# Spotify API credentials
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

# Database
DATABASE_URL=postgres://user:password@host:5432/database_name

# Optional: other configuration values
LOG_LEVEL=INFO
```
- Do not commit secrets or `.env` to version control. Use secret management for production.

---

## Database Initialization

If using Docker Compose with a postgres service, wait until the DB is ready. Then either:
- Run SQL scripts found in `init/` (if present), for example:
  ```bash
  psql $DATABASE_URL -f init/create_tables.sql
  ```
- Or use a Python setup script / SQLAlchemy model migration flow if implemented:
  ```bash
  python src/db_setup.py
  ```
(Replace above filenames with actual scripts found in `src/` or `init/`.)

---

## Running Tests

Run test suite with pytest:
```bash
pytest -q
```

---

## Development Workflow

- Work on a feature branch: `git checkout -b feature/your-feature`
- Add or update tests in `tests/` for new behavior
- Run linters/tests locally before creating a PR
- Push and open a Pull Request describing the change and its rationale

---

## Recommendations & Best Practices

- Register an app at the Spotify Developer Dashboard to obtain `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`.
- Keep secrets out of the repository; use environment variables or secret stores.
- Use Docker Compose during development to guarantee DB and service compatibility.
- Use PySpark for large-scale processing and pandas for exploratory analysis.
- Add CI to run tests automatically (GitHub Actions, etc.) and consider integration tests that run against a test Postgres instance.

---

## Contributing

Contributions are welcome. Suggested process:
1. Fork the repository.
2. Create a branch: `git checkout -b feature/<name>`.
3. Implement your changes and add/adjust tests.
4. Open a Pull Request describing the changes and any migration/upgrade steps.

---

## Contact

Authors:
- Carlos Andres Gomez Orduz
- Gustavo Mena Orduz

For questions or collaboration requests, open an issue in the repository or create a Pull Request.

---
