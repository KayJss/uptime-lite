import pytest

from monitor import normalize_url


def test_normalize_adds_https():
    assert normalize_url("example.com") == "https://example.com"


def test_normalize_keeps_https():
    assert normalize_url("https://example.com") == "https://example.com"


def test_normalize_rejects_empty_url():
    with pytest.raises(ValueError):
        normalize_url("   ")


def test_normalize_rejects_unsupported_scheme():
    with pytest.raises(ValueError):
        normalize_url("ftp://example.com")
