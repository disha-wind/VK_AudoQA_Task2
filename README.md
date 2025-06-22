# Автоматизация тестирования установки и запуска приложения `VK Teams`

Тестирование производится под платформу `Windows`. Соответственно все команды приведены для тестируемой платформы.

## Установка зависимостей

Установите тестовую среду
```shell
pip install -r requirements.dev.txt
```

Скачайте установщик `VK Teams` в директорию [tests\windows\installer](tests\windows\installer)
```shell
New-Item -ItemType Directory -Force -Path "tests\windows\installer"
Invoke-WebRequest -Uri "https://vkteams-www.hb.bizmrg.com/win/x64/vkteamssetup.exe" -OutFile "tests\windows\installer\vkteamssetup.exe"
```

## Запуск тестов

Запуск всех тестов
```shell
pytest
```

Запуск тестов без установки приложения (для тех случаев, если приложение уже установлено или если нужно проверить, как работают тесты без установленного приложения)

```shell
pytest --no-install
```

Другие конфигурации запуска:
- Тест установки приложения
    ```shell
    pytest tests/windows/test_install.py
    ```
    ```shell
    pytest tests/windows/test_install.py --no-install
    ```
- Test запуска приложения
    ```shell
    pytest tests/windows/test_startup.py
    ```
    ```shell
    pytest tests/windows/test_startup.py --no-install
    ```

## Генерация отчета

Отчеты генерируются с текущей датой и временем в папку [reports](tests/reports).  
Используется библиотека [pytest-html](https://pypi.org/project/pytest-html/).

```shell
python tests/report.py
```