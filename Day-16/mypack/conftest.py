import pytest

@pytest.fixture()
def setup():
    print("Test Environmental is opened")
    yield
    print("Test Environmental is closed ")