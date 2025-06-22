def pytest_addoption(parser):
    parser.addoption("--no-install", action="store_true", help="Skip installation")

