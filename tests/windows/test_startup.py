import time


def test_application_startup(startup) -> None:
    """
    Верификация успешного запуска приложения.
    """
    for _ in range(5):
        assert startup.poll() is None, "Process terminated prematurely"
        time.sleep(1)