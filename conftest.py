import pytest
from fixture.application import Applicaton


@pytest.fixture(scope="session")
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture