import winreg
from pathlib import Path

import pytest


def test_exe_file_exist(env_vars) -> None:
    """Проверка создания исполняемого файла и его прав на исполнение"""
    vkteams_exe = Path(env_vars['vkteams_path'])
    assert vkteams_exe.exists()
    assert vkteams_exe.stat().st_mode & 0o111  # Проверка прав на исполнение


def test_decktop_label_exist(env_vars) -> None:
    """Проверка создания ярлыка на рабочем столе"""
    vkteams_label = Path(env_vars['vkteams_label'])
    assert vkteams_label.exists()


def test_config_files_exist(env_vars) -> None:
    """Проверка создания папки конфигурации приложения"""
    vkteams_config = Path(env_vars['vkteams_config'])
    assert vkteams_config.exists()


def test_check_url_protocol() -> None:
    """Проверка создания регистра URL схемы"""
    key_path = r"SOFTWARE\Classes\vkteams"
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path):
            pass
    except FileNotFoundError:
        pytest.fail("URL protocol not found in registry")


def test_check_uninstall_entry() -> None:
    """Проверка записи в списке установленных программ"""
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    found = False

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            i = 0
            while True:
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            display_name, _ = winreg.QueryValueEx(subkey, "DisplayName")
                            if "VK Teams" in display_name:
                                found = True
                                break
                        except FileNotFoundError:
                            pass
                    i += 1
                except OSError:
                    break
    except OSError:
        pass

    assert found, "VK Teams not found in uninstall registry"
