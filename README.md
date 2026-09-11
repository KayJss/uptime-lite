# Uptime Lite

A lightweight website uptime and response-time monitor with a clean Flask dashboard and a tiny JSON API.

[![CI](https://github.com/KayJss/uptime-lite/actions/workflows/ci.yml/badge.svg)](https://github.com/KayJss/uptime-lite/actions/workflows/ci.yml)

## What it does

Uptime Lite checks HTTP/HTTPS endpoints and reports whether they are reachable, their HTTP status code, response time, and network errors. It is intentionally small enough to understand quickly while still following a testable service structure.

## Features

- Monitor up to 10 endpoints from the dashboard
- HTTP status and response-time measurements
- Redirect and timeout handling
- JSON check API
- Health endpoint for deployments
- Responsive dashboard
- Automated tests and GitHub Actions CI

## Quick start

```bash
git clone https://github.com/KayJss/uptime-lite.git
cd uptime-lite
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## API

```text
GET /api/check?url=https://example.com
GET /health
```

Example response:

```json
{
  "url": "https://example.com",
  "online": true,
  "status_code": 200,
  "response_time_ms": 120,
  "error": null
}
```

## Tests

```bash
pytest -q
```

CI runs the test suite on supported Python versions for pushes and pull requests.

## Project structure

```text
app.py                 Flask routes and dashboard
monitor.py             URL validation and monitoring logic
templates/index.html   Dashboard markup
static/style.css       Responsive UI
tests/                 Unit and endpoint tests
.github/workflows/     Continuous integration
```

## Stack

Python 3.11+, Flask, Requests and Pytest.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
