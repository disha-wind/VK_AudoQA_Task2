import os
import subprocess
import time
from pathlib import Path

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

    if request.config.getoption("--no-install"):
        print("Installation skipped due to --no-install flag")
        return

    print("Install process started")

    installer_exe = env_vars['installer_path']
    if not Path(installer_exe).exists():
        pytest.fail(f"Installer not found: {installer_exe}")

    process = subprocess.Popen([installer_exe])
    time.sleep(2)  # Задержка для запуска GUI инсталлера
    pyautogui.press('enter')
    process.wait()

    # Задержка для создания рабочих директорий приложения
    # Без этого не проходит тест windows.test_install.test_config_files_exist
    time.sleep(2)

    print("Install process exited")


@pytest.fixture(scope="function")
def startup(env_vars):
    """
    Фикстура для запуска и остановки приложения.

    Запускает приложение, передает управление тесту,
    а затем останавливает приложение после завершения теста.
    """

    vkteams_exe = env_vars['vkteams_path']
    if not Path(vkteams_exe).exists():
        pytest.fail(f"VKTeams executable not found: {vkteams_exe}")

    process = subprocess.Popen([vkteams_exe])
    time.sleep(5)

    yield process

    process.terminate()

    try:
        process.wait(timeout=10)
        print("Application stopped successfully")
    except subprocess.TimeoutExpired:
        print("Failed to terminate process gracefully, forcing kill")
        process.kill()
