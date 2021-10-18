""" Module who handle updating """
import os
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile
from typing import Union

from packaging.version import InvalidVersion, Version

from inupdater.config import SettingsManager
from inupdater.ui import UserInterface


@dataclass
class Exefile:
    exe_path: Path
    exe_version: Union[str, Version]


class ExeUpdater:
    def __init__(self, install_path: Path, ui: UserInterface) -> None:
        self.install_path = install_path
        self.ui = ui
        settings_path = install_path / Path("settings.json")

        # --------------------------------------
        # Test Purpose only
        # --------------------------------------
        appexemple_path = Path().cwd() / Path("tests/appexemple")
        test_settings = appexemple_path / Path("settings.json")

        if not settings_path.exists() and test_settings.exists():
            self.install_path = appexemple_path
            settings_path = test_settings
        # --------------------------------------

        settingsmanager = SettingsManager(settings_path)
        with settingsmanager as self.settings:
            self.local = None
            self.update = None
            self.ui.show_message("Checking for updates...")
            self.ui.set_state(2)

            if self.update.exe_version > self.local.exe_version:
                self.ui.show_message(
                    f"We find a new update ! : {self.update.exe_version}"
                )
                self.ui.set_state(4)
                copyfile(self.update.exe_path, self.local.exe_path)
                self.settings.version = self.update.exe_version
                self.ui.show_message("Update installed !")
                self.ui.set_state(6)

    @property
    def local(self) -> Exefile:

        exe_path = self.install_path / Path(
            f"{self.settings.exe_name}.exe"
        )  # TODO EXE or not?!? check with no Admin
        assert exe_path.exists()
        exe_version = self.settings.version

        return Exefile(exe_path, exe_version)

    @local.setter
    def local(self, _):
        return

    @property
    def update(self):
        exe_path = self.check_for_latest_update(self.settings.dist_path)
        exe_version = self.get_version(exe_path)
        return Exefile(exe_path, exe_version)

    @update.setter
    def update(self, _):
        return

    @staticmethod
    def get_version(pathver: Path) -> Version:
        try:
            return Version(pathver.stem.split("_")[1])
        except IndexError as idx:
            raise idx
        except InvalidVersion as ive:
            raise ive

    @staticmethod
    def get_exe_list(path: Path) -> list[Path]:
        return [
            f
            for f in Path(path).iterdir()
            if f.suffix == ".exe" and f.stem != "unins000"
        ]

    def check_for_latest_update(self, path: Path) -> Path:
        """Check for latest update in a given path"""

        exe_list = self.get_exe_list(path)
        last = sorted(exe_list, key=self.get_version)[-1]
        return last

    def launch(self, *args):
        command = [str(self.local.exe_path), *args]
        self.ui.show_message(f"Launching {self.settings.exe_name}")
        self.ui.set_state(8)

        self.ui.show_message("Please wait..")
        self.ui.set_state(10)

        self.ui.close()
        os.system(" ".join([str(c) for c in command]))
