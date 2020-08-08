# content of ./test_helloworld.py
"""Tests for helloWorld."""
from remindo_api.helloworld import RemindoHelloWorld


def test_helloworld(rclient):
    """Test function to check the validity of helloworld() call."""
    response = rclient.hello_world()
    assert isinstance(response, RemindoHelloWorld)
    assert response.message == "hello world"
