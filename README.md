# Автоматизация тестирования установки и запуска приложения

Тестирование производится под платформу `Windows`.

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