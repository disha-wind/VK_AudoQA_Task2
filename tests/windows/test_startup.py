import time


def test_application_startup(startup) -> None:
    """
    Верификация успешного запуска приложения.
    """
    # Если приложение не упало через 5 секунд после старта, то работает в допустимых пределах.
    # Другие проверки посчитал излишними в рамках тестового задания.
    for i in range(10):
        assert startup.poll() is None, f"Process terminated prematurely (after {i * 0.5:.1f}s)"
        time.sleep(0.5)
