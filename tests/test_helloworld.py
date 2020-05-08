# content of ./test_helloworld.py
from remindo_api.helloworld import RemindoHelloWorld


def test_helloworld(rclient):
    response = rclient.hello_world()
    assert isinstance(response, RemindoHelloWorld)
    assert response.message == "hello world"
