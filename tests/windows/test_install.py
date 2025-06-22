import winreg
from pathlib import Path


def test_exe_file_exist(env_vars) -> None:
    """Проверка создания исполняемого файла"""
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
    assert winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) is not None
