from pathlib import Path


def test_exe_file_exist(env_vars) -> None:
    vkteams_exe = Path(env_vars['vkteams_path'])
    assert vkteams_exe.exists()
    assert vkteams_exe.stat().st_mode & 0o111  # Проверка прав на исполнение


def test_decktop_label_exist(env_vars) -> None:
    vkteams_label = Path(env_vars['vkteams_label'])
    assert vkteams_label.exists()


def test_config_files_exist(env_vars) -> None:
    vkteams_config = Path(env_vars['vkteams_config'])
    assert vkteams_config.exists()
