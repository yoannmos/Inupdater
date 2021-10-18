import pytest
from PySide6.QtGui import QPixmap

from inupdater.splash import SplashScreen


@pytest.fixture
def app(qtbot):
    qpix = QPixmap("inupdater\data\splash.png")
    splashscreen = SplashScreen(qpix)
    qtbot.addWidget(splashscreen)
    return splashscreen


def test_message(app):
    app.set_message("Test")
    assert app._messageLabel.text() == "Test"


def test_progressbar_value(app):
    app.set_progress_value(1)
    assert app._progressBar.value() == 1


def test_progressbar_min(app):
    app.set_progress_min(2)
    app.set_progress_value(0)
    assert app._progressBar.value() == 1


def test_progressbar_max(app):
    app.set_progress_max(10)
    app.set_progress_value(11)
    assert app._progressBar.value() == -1


def splash_TESTING():
    """TODO : Reel testing"""
    import random
    import sys
    import time

    from PySide6.QtGui import QPixmap
    from PySide6.QtWidgets import QApplication, QLabel

    from inupdater.splash import SplashScreen

    app_name = "My APP"
    version = "1.1"

    a = QApplication(sys.argv)

    qpix = QPixmap("inupdater\data\splash.png")
    # qpix.scaled(w:10,
    splash = SplashScreen(qpix)
    splash.show()

    messages = [
        "Checking for updates...",
        f"We find a new update ! {app_name}_{version}",
        f"Downloading {app_name}_{version}...",
        "Update downloaded !",
        f"Installing {app_name}_{version}...",
        "Update installed !",
        f"Launching {app_name}_{version}...",
        "Please wait...",
    ]
    splash.set_progress_max(len(messages))
    for idx, msg in enumerate(messages):
        splash.set_message(msg)
        a.processEvents()
        splash.set_progress_value(idx + 1)
        time.sleep(random.randint(10, 20) / 10)

    w = QLabel("My App")
    w.resize(600, 400)
    splash.finish(w)
    time.sleep(0.2)
    w.show()


if __name__ == "__main__":
    splash_TESTING()
