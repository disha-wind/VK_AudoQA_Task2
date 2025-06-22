import subprocess
import time
from pathlib import Path

import pyautogui


def test_app_install(env_vars) -> None:
    installer_exe = env_vars['installer_path']
    process = subprocess.Popen([installer_exe])
    time.sleep(2)
    pyautogui.press('enter')
    process.wait()

    vkteams_exe = env_vars['vkteams_path']
    assert Path(vkteams_exe).exists()
