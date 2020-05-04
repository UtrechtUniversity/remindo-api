# content of ./conftest.py
import pytest
from remindo_api import apikey
from remindo_api import client


@pytest.fixture
def rclient():
    rclient = client.RemindoClient(
        uuid = apikey.uuid,
        secret = apikey.secret,
        url_base = apikey.url_base
    )
    yield rclient
