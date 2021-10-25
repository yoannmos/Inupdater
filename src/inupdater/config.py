import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from packaging.version import InvalidVersion, Version


@dataclass
class Settings:
    exe_name: str
    dist_location: Path # Actually support only path
    version: Version

    @property
    def exe_name(self):
        return self._exe_name

    @exe_name.setter
    def exe_name(self, value):
        match value:
            case str() if value.isalpha():
                self._exe_name = value
            case _:
                raise TypeError("Exe name should be alphanumeric")

    @property
    def dist_location(self):
        """Can be return a method ?"""
        return self._dist_location

    @dist_location.setter
    def dist_location(self, value):
        match value:
            case Path() | str() if Path(value).exists() and Path(value).is_dir():
                self._dist_location = Path(value)

            case _:
                raise TypeError(
                    "Your dist_location is not a valid, actually only Path are supported")

    @property
    def version(self) -> Version:
        return self._version

    @version.setter
    def version(self, value: str | Version):
        match value:
            case str():
                self._version = Version(value)
            case Version():
                self._version = value
            case None:
                self._version = Version("0.0.1")
            case _:
                raise InvalidVersion

    def asdict(self):
        return {"exe_name": self._exe_name,
                "dist_location": self.dist_location,
                "version": self.version}


class SettingsEncoder(json.JSONEncoder):
    def default(self, object: Any) -> Any:
        if any([isinstance(object, str), isinstance(object, Version)]):
            return str(object)
        if isinstance(object, Path):
            new = str(object)
            new = new.replace("\\", "/")
            new = new.replace("\\\\", "/")
            return new
        else: # pragma: no cover
            return super().default(object)

class SettingsManager:

    settings: Settings

    def __init__(self, settings_path: Path) -> None:
        self.settings_path = settings_path

    def __enter__(self) -> Settings:
        with open(self.settings_path) as f:
            self.settings = Settings(**json.load(f))
        return self.settings

    def __exit__(self, *exc) -> None:
        with open(self.settings_path, "w") as f:
            json.dump(self.settings.asdict(), f, cls=SettingsEncoder, indent="\t")
