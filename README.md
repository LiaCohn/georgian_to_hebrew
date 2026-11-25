# Georgian to Hebrew Date Converter

A small FastAPI service that converts a Gregorian date to its Hebrew date using the [Hebcal Date Converter API](https://www.hebcal.com/home/219/hebrew-date-converter-rest-api).

## Requirements

- Python 3.10 or later

## Run locally

From the project directory, create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

The service will be available at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Request with Postman

Create a `GET` request to:

```text
http://127.0.0.1:8000/hebrew-date?date=2024-10-14
```

To request the Hebrew date after sunset, set the optional `after_sunset` query parameter to `true`:

```text
http://127.0.0.1:8000/hebrew-date?date=2024-10-14&after_sunset=true
```

Alternatively, enter these values in Postman's **Params** tab:

| Key | Value |
| --- | --- |
| `date` | `2024-10-14` |
| `after_sunset` | `true` |

Example response:

```json
{
  "gregorian": "2024-10-14",
  "hebrew": "י״ב בְּתִשְׁרֵי תשפ״ה"
}
```

The `date` parameter must be a valid Gregorian date in `YYYY-MM-DD` format. Invalid dates are rejected with HTTP `422`. If Hebcal is unavailable or returns an invalid response, the service returns HTTP `502`.
