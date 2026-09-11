# Uptime Lite

A lightweight website uptime and response-time monitor built with Python and Flask.

## Features

- Monitor multiple HTTP/HTTPS endpoints
- Track status code and response time
- Simple web dashboard
- JSON API endpoint for checks
- Timeout and network error handling
- Basic automated tests
- No external database required

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## API

Check a URL:

```text
GET /api/check?url=https://example.com
```

Example response:

```json
{
  "url": "https://example.com",
  "online": true,
  "status_code": 200,
  "response_time_ms": 120
}
```

## Tests

```bash
pytest
```

## Stack

Python 3.11+, Flask, Requests, Pytest.

## License

MIT
