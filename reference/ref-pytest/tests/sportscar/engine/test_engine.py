import pytest


@pytest.mark.smoke
@pytest.mark.engine
def test_engine_true():
    assert True


def test_browser(chrome_browser):
    resp = chrome_browser.get(
        "https://selenium-python.readthedocs.io/getting-started.html"
    )
    assert True
