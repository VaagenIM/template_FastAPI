"""
# app.py er hovedfilen som starter opp API-et, denne bør ikke endre navn.
#
# Den trenger dog ikke inneholde så mye kode, vi kan dele opp API-et i flere filer, og ha
# denne filen minst mulig, slik at vi kan ha en god oversikt over API-et vårt.
#
# Lesestoff / Dokumentasjon: https://fastapi.tiangolo.com/
"""

import uvicorn
from fastapi import FastAPI

# Ekstra API-endepunkter / Python filer
from cat import cat

# Hvis du ikke vil ha docs, sett docs_url=None og redoc_url=None
app = FastAPI(docs_url="/docs", redoc_url="/redoc")

# Legg til ekstra API-endepunkter (se cat.py, slik at vi kan dele opp koden i flere filer)
app.include_router(cat)


@app.get("/")
async def read_root() -> dict:
    # Merk at funksjonsnavn blir brukt som "summary" i dokumentasjonen
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    """
    Docstrings blir også synlige, denne kan du se på http://localhost:8000/docs eller /redoc under "GET /items/{item_id}"

    - **item_id**: The ID of the item to get
    """
    return {"item_id": item_id}


# Kjør med "uvicorn app:app --reload", eller deploy i Docker ved å kjøre "docker-compose up --build"
# Du kan også kjøre denne filen med Python dersom du ønsker det.
# Besøk http://localhost:8000/docs for å se dokumentasjonen, denne genereres automatisk ;)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
