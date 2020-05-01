import pytest
import requests


@pytest.mark.vcr()
def test_iana():
    response = requests.get("http://www.iana.org/domains/reserved")
    assert "Example domains" in response.text


@pytest.mark.vcr()
def test_iana_2():
    response = requests.get("http://www.iana.org/domains/reserved")
    assert "Example domains" in response.text
