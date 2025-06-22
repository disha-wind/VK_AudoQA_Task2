import os
from dotenv import load_dotenv
import pytest


def pytest_configure(config):
    load_dotenv()


@pytest.fixture(scope="session")
def env_vars():
    """Фикстура для доступа к переменным окружения"""
    return {
        'installer_path': os.getenv('VK_TEAMS_INSTALLER_PATH'),
        'vkteams_path': os.path.expandvars(os.getenv('VK_TEAMS_PATH'))
    }
