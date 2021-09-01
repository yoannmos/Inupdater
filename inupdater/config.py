import json
from pathlib import Path
from typing import Any, Union

from packaging.version import InvalidVersion, Version
from pydantic import BaseSettings, validator


class SettingsEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if any([isinstance(o, str), isinstance(o, Path), isinstance(o, Version)]):
            return str(o)
        else:
            return super().default(o)


class Settings(BaseSettings):

    exe_name: str
    dist_path: Path
    version: Union[str, Version]

    @validator("exe_name")
    def name_only(cls, v: str):
        if v.isalpha:
            return v
        elif len(v.split("_")) > 1:
            try:
                Version(v.split("_")[1])
                return v.split("_")[0]
            except InvalidVersion:
                pass
        else:
            raise TypeError(
                "Exe name should be alphanumeric or contain valid version after '_'"
            )

    @validator("dist_path")
    def path_exists(cls, v):
        if not v.exists():
            raise FileExistsError("Path is not valid")
        return v

    @validator("version", always=True)
    def check_exist_version(cls, v):
        if isinstance(v, str):
            return Version(v)

        if isinstance(v, Version):
            return v

        if not v:
            return Version("0.0.1")

        else:
            raise InvalidVersion

    class Config:
        validate_assignment = True


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
            json.dump(self.settings.dict(), f, cls=SettingsEncoder, indent="\t")
