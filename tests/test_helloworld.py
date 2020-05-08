# content of ./test_helloworld.py
from remindoapi.helloworld import RemindoHelloWorld


def test_helloworld(rclient):
    response = rclient.hello_world()
    assert isinstance(response, RemindoHelloWorld)
    assert response.message == "hello world"
