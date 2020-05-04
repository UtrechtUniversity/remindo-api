# content of ./conftest.py
import pytest
from remindoapi import apikey
from remindoapi import client


@pytest.fixture
def rclient():
    rclient = client.RemindoClient(
        uuid = apikey.uuid,
        secret = apikey.secret,
        url_base = apikey.url_base
    )
    yield rclient
