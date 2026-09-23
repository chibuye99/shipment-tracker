# shipment-tracker

A Flask API for Northwind Logistics shipment tracking, containerized with Docker and deployed to AWS EC2.

CI/CD is handled by GitHub Actions: every push to `main` builds the image, pushes it to Docker Hub tagged with the commit SHA, SSHes into the server, deploys it, verifies the `/health` endpoint, and rolls back automatically if verification fails.

The app exposes `/`, `/health`, and `/greeting`, listens on port 5000, and reads its configuration from environment variables (`PORT`, `FLASK_ENV`, `GREETING_STYLE`).

Run it locally with `docker build -t shipment-tracker . && docker run -p 5000:5000 shipment-tracker`.

**Status: work in progress.** Known gaps still being addressed — tests in the pipeline, secret management, external monitoring, and IaC for the server. See the known issues section for the full list.
