import pytest


@pytest.mark.smoke
@pytest.mark.engine
def test_engine_true():
    assert True
