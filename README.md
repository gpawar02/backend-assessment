# Backend Developer Technical Assessment

## Overview

This project demonstrates a **data pipeline** with three Dockerized services:

1. **Flask Mock Server** – Serves customer data from a JSON file.
2. **FastAPI Pipeline** – Ingests customer data from Flask into PostgreSQL with upsert logic.
3. **PostgreSQL** – Stores customer data for querying.

**Data Flow:**  
`Flask (JSON)` → `FastAPI (Ingest & Store)` → `PostgreSQL` → `FastAPI API Response`

---

## Prerequisites

- **Docker Desktop** (running)
- **Python 3.10+**
- **Git**
- Optional: PowerShell / Bash for testing API endpoints

Verify installations:

```bash
docker --version
docker-compose --version
python --version
git --version
