#Простий бекенд, який зберігає кількість заходів на сторінку у postgres і віддає їх загальну кількість
import os
from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI

DATABASE_URL = os.environ["DATABASE_URL"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    with psycopg.connect(DATABASE_URL, autocommit=True) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS visits ("
            "id serial PRIMARY KEY, "
            "created_at timestamptz NOT NULL DEFAULT now())"
        )
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/health")
def health():
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("SELECT 1")
    return {"status": "ok"}


@app.post("/api/visits")
def add_visit():
    with psycopg.connect(DATABASE_URL, autocommit=True) as conn:
        conn.execute("INSERT INTO visits DEFAULT VALUES")
        total = conn.execute("SELECT count(*) FROM visits").fetchone()[0]
    return {"visits": total}
