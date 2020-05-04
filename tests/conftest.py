# content of ./conftest.py
import pytest
from remindo_api import apikey
from remindo_api import client

# TODO: Create mocking fixture

# TODO: apply e2e and use with "-m e2e"
def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def rclient():
    rclient = client.RemindoClient(
        uuid=apikey.uuid, secret=apikey.secret, url_base=apikey.url_base
    )
    yield rclient
