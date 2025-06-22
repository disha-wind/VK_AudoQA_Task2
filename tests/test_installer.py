import subprocess
import time

import pyautogui


def test_app_install(env_vars) -> None:
    process = subprocess.Popen([env_vars['installer_path']])
    time.sleep(2)
    pyautogui.press('enter')
    process.wait()
