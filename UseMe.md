<h1 align=center><strong>FastAPI Bewise.ia Test Application</strong></h1>

<br>

This is a Browse.ia repository meant for a test job! This template uses the following technology stack:

* 🐳 [Dockerized](https://www.docker.com/)
* 🐘 [Asynchronous PostgreSQL](https://www.postgresql.org/docs/current/libpq-async.html)
* 🐍 [FastAPI](https://fastapi.tiangolo.com/)

When the `Docker` is started, these are the URL addresses:

* Backend Application (API docs) $\rightarrow$ `http://localhost:8000/docs`
* Database editor (Adminer) $\rightarrow$ `http//localhost:8080`


## Setup Guide

1. Enter development folder:
   ```shell
   cd Bewise.ia
   ```

2. Backend app credentials setup:
    If you are not used to VIM or Linux CLI, then ignore the `echo` command and do it manually. All the secret variables for this template are located in `.env.example`.

    ```shell
    # Make sure you are in the ROOT project directory
    touch .env
   
    cp .env.example .env
    ```

3. Docker setup:
   ```shell
    # Every time you write a new code, update your container with:
    docker-compose -f docker-compose.dev.yml up -d --build
   ```

4. (IMPORTANT) Database setup:
   ```shell
    # (Docker) Generate revision for the database auto-migrations
    docker exec -ti fast-api alembic revision --autogenerate -m "YOUR MIGRATION TITLE"
    docker exec -ti fast-api alembic upgrade head    # to register the database classes
   ```
