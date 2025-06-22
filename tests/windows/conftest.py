import os
import subprocess
import time

import pyautogui
import pytest
from dotenv import load_dotenv


def pytest_configure():
    load_dotenv()


@pytest.fixture(scope="session")
def env_vars():
    """Фикстура для доступа к переменным окружения"""
    return {
        'installer_path': os.getenv('VK_TEAMS_INSTALLER_EXE_PATH'),
        'vkteams_path': os.path.expandvars(os.getenv('VK_TEAMS_EXE_PATH')),
        'vkteams_label': os.path.expandvars(os.getenv('VK_TEAMS_LABEL')),
        'vkteams_config': os.path.expandvars(os.getenv('VK_TEAMS_CONFIG'))
    }


@pytest.fixture(scope='session', autouse=True)
def install(env_vars, request) -> None:
    """
    Фикстура запуска инсталлера и установки приложения.
    Отключается при запуске с флагом --no-install
    """

    # Отключение установки
    if request.config.getoption("--no-install"):
        print("Installation skipped due to --no-install flag")
        return

    print("Install process started")

    installer_exe = env_vars['installer_path']
    process = subprocess.Popen([installer_exe])
    time.sleep(2)  # Задержка для запуска GUI инсталлера
    pyautogui.press('enter')
    process.wait()

    # Задержка для создания рабочих директорий приложения
    # Без этого не проходит тест windows.test_install.test_config_files_exist
    time.sleep(2)

    print("Install process exited")
