# content of ./conftest.py
"""Configure tests."""
import pytest
import tests.apikey as ak
from remindo_api import client


def pytest_configure(config):
    # TODO: Create mocking fixture
    # TODO: apply e2e and use with "-m e2e"
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def rclient():
    rclient = client.RemindoClient(
        uuid=ak.uuid,
        secret=ak.secret,
        url_base=ak.url_base,
        sha="SHA1"
    )
    yield rclient
