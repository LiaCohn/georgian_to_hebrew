# main.py
import httpx
from datetime import date
from fastapi import FastAPI, HTTPException
from consts import URL
app = FastAPI()


@app.get("/hebrew-date")
def hebrew_date(date: date, after_sunset: bool | None = None):
    params = {
        "cfg": "json",
        "gy": date.year,
        "gm": date.month,
        "gd": date.day,
        "g2h": 1,
        "strict": 1,
    }
    if after_sunset:
        params["gs"] = "on"

    try:
        response = httpx.get(
            URL,
            params=params,
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()
    except httpx.HTTPError as error:
        raise HTTPException(status_code=502, detail="Hebcal is unavailable") from error
    except (ValueError, TypeError) as error:
        raise HTTPException(status_code=502, detail="Hebcal returned an invalid response") from error

    hebrew = data.get("hebrew")
    if not isinstance(hebrew, str) or not hebrew:
        raise HTTPException(status_code=502, detail="Hebcal returned an invalid response")

    return {"gregorian": date.isoformat(), "hebrew": hebrew}