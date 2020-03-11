import pytest


@pytest.mark.body
class BodyTests:
    def test_body_true(self):
        assert True

    def test_body_false(self):
        assert False == False
