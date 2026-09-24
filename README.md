# shipment-tracker

Flask API for Northwind Logistics shipment tracking. Containerized, deployed to AWS EC2 via GitHub Actions.

**Status:** work in progress. Known gaps documented below.

## Architecture

Developer → GitHub (main) → GitHub Actions → Docker Hub → EC2 → Docker container.

Two pipeline jobs:
- **build:** checkout → build image → tag with short git SHA → push to Docker Hub
- **deploy:** SSH to EC2 → pull image → stop/rm old container → run new → curl /health → rollback on failure

## Stack

| Layer | Tech |
|---|---|
| App | Python 3.11, Flask 3.0 |
| Container | Docker, `python:3.11-slim` |
| Registry | Docker Hub (`chibuye/shipment-tracker`) |
| CI/CD | GitHub Actions |
| Server | AWS EC2, Ubuntu 22.04, t2.micro |
| Network | Security group `northwind-prod-sg` |

## Endpoints

| Method | Path | Response |
|---|---|---|
| GET | `/` | `{"service":"shipment-tracker","status":"running"}` |
| GET | `/health` | `{"status":"ok"}` |
| GET | `/greeting` | `{"greeting":"...","name":"...","style":"..."}` |

## Env Vars

| Var | Default | Purpose |
|---|---|---|
| `PORT` | `5000` | App bind port |
| `FLASK_ENV` | `production` | Flask env |
| `GREETING_STYLE` | `formal` | `formal`, `casual`, `enthusiastic` |

## Run Locally

```bash
docker build -t shipment-tracker .
docker run -p 5000:5000 -e GREETING_STYLE=casual shipment-tracker
curl http://localhost:5000/health
