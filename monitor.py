from __future__ import annotations

from dataclasses import asdict, dataclass
from time import perf_counter
from urllib.parse import urlparse

import requests


@dataclass(frozen=True)
class CheckResult:
    url: str
    online: bool
    status_code: int | None
    response_time_ms: int | None
    error: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def normalize_url(url: str) -> str:
    url = url.strip()
    if not url:
        raise ValueError("URL cannot be empty")

    if "://" not in url:
        url = f"https://{url}"

    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Enter a valid HTTP or HTTPS URL")
    return url


def check_url(url: str, timeout: float = 5.0) -> CheckResult:
    normalized = normalize_url(url)
    started = perf_counter()

    try:
        response = requests.get(
            normalized,
            timeout=timeout,
            allow_redirects=True,
            headers={"User-Agent": "UptimeLite/1.0"},
        )
        elapsed = round((perf_counter() - started) * 1000)
        return CheckResult(
            url=normalized,
            online=response.status_code < 500,
            status_code=response.status_code,
            response_time_ms=elapsed,
        )
    except requests.RequestException as exc:
        elapsed = round((perf_counter() - started) * 1000)
        return CheckResult(
            url=normalized,
            online=False,
            status_code=None,
            response_time_ms=elapsed,
            error=exc.__class__.__name__,
        )
