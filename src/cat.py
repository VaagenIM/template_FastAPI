"""
Cat API - Flere API-endepunkter i egne filer

Inkluderes i app.py med:
    from cat import cat
    app.include_router(cat)
"""
import requests
from fastapi import APIRouter


cat = APIRouter(prefix="/cat", tags=["Cat"])


@cat.get("/", summary="Get a cat fact")
async def get_root() -> dict:
    """Get a random cat fact from https://cat-fact.herokuapp.com/"""
    r = requests.get("https://cat-fact.herokuapp.com/facts/random")
    if r.status_code != 200:
        return {"error": "Could not get cat fact, try again later"}
    return {"cat_fact": r.json().get("text")}