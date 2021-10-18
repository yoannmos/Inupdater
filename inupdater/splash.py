import random
import sys
import time

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QProgressBar,
    QSplashScreen,
    QVBoxLayout,
)


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap: QPixmap = None, f: Qt.WindowFlags = Qt.WindowFlags()):
        super().__init__(pixmap=pixmap, f=f)
        self.__init_ui__()

    def __init_ui__(self):
        self._progressBar = QProgressBar()
        self._progressBar.setMinimumWidth(250)
        self._progressBar.setTextVisible(False)
        self._progressBar.setStyleSheet(
            """
            QProgressBar{
                border: 2px solid grey;
                border-radius: 10px;
                text-align: center
                }
            
            QProgressBar::chunk {
                background-color: #339c80;
                border-radius: 8px;
                margin: 0px;
                }
            """
        )

        self._messageLabel = QLabel()
        self._messageLabel.setStyleSheet(
            """
            QLabel{
            color: white
            }
            """
        )

        # Text Font
        f = QFont()
        f.setPointSize(16)
        self._messageLabel.setFont(f)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addWidget(self._messageLabel, 0, Qt.AlignHCenter)
        layout.addWidget(self._progressBar, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.setLayout(layout)

        self._app = QApplication.instance()
        # self._app.processEvents()

    def __update__(self):
        self._app.processEvents()

    def set_message(self, message: str):
        self._messageLabel.setText(message)
        self.__update__()

    def set_progress_value(self, value: int):
        self._progressBar.setValue(value)

    def set_progress_min(self, min: int):
        self._progressBar.setMinimum(min)

    def set_progress_max(self, max: int):
        self._progressBar.setMaximum(max)
