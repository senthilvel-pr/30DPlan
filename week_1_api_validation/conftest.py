import pytest

def pytest_addoption(parser):
    # This adds a new flag: --product_id
    parser.addoption("--product_id", action="store", default="1", help="Product ID to test")

@pytest.fixture
def product_id(request):
    return request.config.getoption("--product_id")