from test_twttr1.twttr import shorten
import pytest

def test_upper():
    assert shorten("IHSANUL HAQ") == "HSNL HQ"

def test_lower():
    assert shorten("ihsanul haq") == "hsnl hq"
