# Template for FastAPI
Dette er en enkel mal for å kunne komme raskt i gang med FastAPI, med enkle eksempler og enkel deploy til GitHub Container Registry ved hjelp av GitHub Actions.

Dokumentasjon: https://fastapi.tiangolo.com (Video fra ArjanCodes: https://www.youtube.com/watch?v=SORiTsvnU28)

## Komme i gang
Installer nødvendige pakker med `pip install -r requirements.txt`. Deretter redigerer du filene i `src` mappen. 

Når du er klar til å teste API-et ditt, kjører du applikasjonen med `uvicorn app:app --reload`, eller ved å kjøre `app.py`

Ditt API blir tilgjengelig på `http://localhost:8000/docs`.

> OBS: Hver gang du publiserer en ny versjon av API-et ditt, vil det bli lages en ny container image som blir publisert til GitHub Container Registry. Dette gjør det enkelt å deploye API-et ditt til en server ved å kjøre `docker run <ghcr.io-image>`, hvorav image filen finner du i feltet "packages" på GitHub (til høyre på skjermen). (Eller ved å bruke `docker-compose up`, se `docker-compose.yml`).
> 
> Dette er ikke noe en nødvendigvis trenger å gjøre, men i en ordentlig setting vil en gjerne ha en egen server som kjører API-et ditt, og da er dette en enkel måte å gjøre det på, ettersom en slipper å tenke på å installasjon eller oppsett av noe som helst når en bruker Docker.

## Hvorfor lage et API?
Et API gjør det mulig å dele data med andre programmer, uten at de trenger direkte tilgang til hverken databasen eller koden din. Så og si alle store tjenester har et API, som gjør det mulig for andre å lage programmer som bruker dataen deres. For eksempel har Spotify et API som gjør det mulig for andre å lage programmer som kan spille musikk fra Spotify, eller hente ut informasjon om sanger og album.

Se for deg at du lager en applikasjon som lagrer og henter vitser. Appen skal kunne brukes som en app, nettside og gjøres tilgjengelig i form av en Discord bot. Alternativene dine er å lage en egen database for hver av disse - eller lage et felles API som kan brukes av alle tre. Som i tillegg har fordelen med at applikasjonene vil være synkronisert, slik at en vits som blir lagt til i appen også vil være tilgjengelig i Discord boten. Nyttig!

_(Ja, du kan i teorien dele samme database for alle appene, men det kan fort bli komplisert og vanskelig å vedlikeholde i forhold til et API)._