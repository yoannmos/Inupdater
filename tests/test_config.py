"""Config Test File"""
from pathlib import Path

import pytest
from packaging.version import InvalidVersion, Version

from inupdater.config import Settings


@pytest.fixture
def standard_setting_dict():
    settings_dict = {
        "exe_name": "appexemple",
        "dist_location": "tests\\appexemple\\dist_test",
        "version": "0.0.1",
    }
    return settings_dict


class TestSettings:
    def test_exename_alpha(self, standard_setting_dict):
        setting = Settings(**standard_setting_dict)
        assert "appexemple" == setting.exe_name

    def test_exename_version(self, standard_setting_dict):
        with pytest.raises(TypeError):
            standard_setting_dict["exe_name"] = "appexemple_1.0.7"
            Settings(**standard_setting_dict)

    def test_exename_notalpha(self, standard_setting_dict):
        with pytest.raises(TypeError):
            standard_setting_dict["exe_name"] = "appexemple!"
            Settings(**standard_setting_dict)

    def test_dist_location_path(self, standard_setting_dict):
        settings = Settings(**standard_setting_dict)
        assert Path(standard_setting_dict["dist_location"]) == settings.dist_location

    def test_dist_location_pathdontexist(self, standard_setting_dict):
        with pytest.raises(TypeError):
            standard_setting_dict["dist_location"] = (
                "folderthatnotexist\\tests\\appexemple\\dist_test",
            )
            Settings(**standard_setting_dict)

    def test_dist_location_notapath(self, standard_setting_dict):
        with pytest.raises(TypeError):
            standard_setting_dict["dist_location"] = 828
            Settings(**standard_setting_dict)

    @pytest.mark.skip
    def test_dist_location_github(self):
        assert False

    def test_version_str(self, standard_setting_dict):
        standard_setting_dict["version"] = "1.8.4a"
        setting = Settings(**standard_setting_dict)
        assert Version("1.8.4a") == setting.version

    def test_version_version(self, standard_setting_dict):
        standard_setting_dict["version"] = Version("5.4.3")
        setting = Settings(**standard_setting_dict)
        assert Version("5.4.3") == setting.version

    def test_version_none(self, standard_setting_dict):
        standard_setting_dict["version"] = None
        setting = Settings(**standard_setting_dict)
        assert Version("0.0.1") == setting.version

    def test_version_invalid(self, standard_setting_dict):
        with pytest.raises(InvalidVersion):
            standard_setting_dict["version"] = "0.0spooky.1"
            Settings(**standard_setting_dict)

    def test_version_invalid_nottype(self, standard_setting_dict):
        with pytest.raises(InvalidVersion):
            standard_setting_dict["version"] = []
            Settings(**standard_setting_dict)

    def test_asdict(self, standard_setting_dict):
        setting = Settings(**standard_setting_dict)
        assert standard_setting_dict == setting.asdict()
