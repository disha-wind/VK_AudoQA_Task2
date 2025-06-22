import os
from subprocess import run
from datetime import datetime
from pathlib import Path


def generate_report() -> None:
    """Генерирует отчет по всем тестам, добавляя к названию файла текущую дату и время"""
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = reports_dir / f"report_{timestamp}.html"

    run([
        "pytest",
        f"--html={report_file}",
        "--self-contained-html"
    ])


if __name__ == '__main__':
    # Устанавливаю рабочую директорию в папку скрипта
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    generate_report()
