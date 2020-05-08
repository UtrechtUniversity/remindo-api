# content of ./conftest.py
import pytest
from remindoapi import apikey
from remindoapi import client


def pytest_configure(config):
    # TODO: Create mocking fixture
    # TODO: apply e2e and use with "-m e2e"
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def rclient():
    rclient = client.RemindoClient(
        uuid=apikey.uuid, secret=apikey.secret, url_base=apikey.url_base
    )
    yield rclient
