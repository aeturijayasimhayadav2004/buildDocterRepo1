from app.settings import REQUEST_TIMEOUT


def test_timeout_is_positive():
    assert REQUEST_TIMEOUT > 0
