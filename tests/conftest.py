import os
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption("--no-install", action="store_true", help="Skip installation")

# Устанавливаю рабочую директорию в папку tests
script_dir = Path(__file__).parent
os.chdir(script_dir)