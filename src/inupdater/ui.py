import sys
import time
from abc import ABC, abstractmethod

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication

import inupdater.resource
from inupdater.splash import SplashScreen


class UserInterface(ABC):
    """Interface for GUI element"""

    def __init__(self) -> None:
        self.state = 0

    @abstractmethod
    def show_message(self, msg: str):
        """Show a message"""

    @abstractmethod
    def set_state(self, state: int):
        """Set the program progress by a state value"""

    @abstractmethod
    def close(self):
        """Close the updtater UI"""


class CmdUI(UserInterface):
    """Commande line UI"""

    def __init__(self) -> None:
        super().__init__()

    def show_message(self, msg: str):
        print(self.state, msg)

    def set_state(self, state: int):
        """Set the program progress by a state value"""
        self.state = state

    def close(self):
        pass


class QtUI(UserInterface):
    def __init__(self) -> None:
        super().__init__()
        app = QApplication(sys.argv)
        qpix = QPixmap(":/src/inupdater/data/splash.png")
        self.splash = SplashScreen(qpix)
        self.splash.set_progress_max(10)
        self.splash.show()

    def show_message(self, msg: str):
        self.splash.set_message(msg)

    def set_state(self, state: int):
        """Set the program progress by a state value"""
        self.splash.set_progress_value(self.state)
        self.state = state
        time.sleep(1)

    def close(self):
        self.splash.close()
