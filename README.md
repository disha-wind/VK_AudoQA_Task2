# Автоматизация тестирования установки и запуска приложения

Тестирование производится под платформу `Windows`. Соответственно все команды приведены для тестируемой платформы.

## Установка зависимостей

Установите тестовую среду
```shell
pip install -r requirements.dev.txt
```

Скачайте установщик `VK Teams`
```shell
New-Item -ItemType Directory -Force -Path "tests\installer"
Invoke-WebRequest -Uri "https://vkteams-www.hb.bizmrg.com/win/x64/vkteamssetup.exe" -OutFile "tests\installer\vkteamssetup.exe"
```

## Запуск тестов

Перейдите в рабочую директорию
```shell
cd tests
```

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
    pytest windows/test_install.py
    ```
    ```shell
    pytest windows/test_install.py --no-install
    ```
- Test запуска приложения
    ```shell
    pytest windows/test_startup.py
    ```
    ```shell
    pytest windows/test_startup.py --no-install
    ```