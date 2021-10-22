"""Updater Test File"""
import pytest

from inupdater.updater import Exefile


class TestExefile:
    def test_equal_pass(self):
        exe_dict_1 = {
            "path": "appexemple",
            "version": "0.0.1",
        }
        exe_dict_2 = {
            "path": "appexemple1",
            "version": "0.0.1",
        }
        exe_1 = Exefile(**exe_dict_1)
        exe_2 = Exefile(**exe_dict_2)
        assert exe_1 == exe_2

    def test_lt_pass(self):
        exe_dict_1 = {
            "path": "appexemple",
            "version": "0.0.1",
        }
        exe_dict_2 = {
            "path": "appexemple1",
            "version": "0.0.2",
        }
        exe_1 = Exefile(**exe_dict_1)
        exe_2 = Exefile(**exe_dict_2)
        assert exe_1 < exe_2

    def test_le_pass(self):
        exe_dict_1 = {
            "path": "appexemple",
            "version": "0.0.1",
        }
        exe_dict_2 = {
            "path": "appexemple1",
            "version": "0.0.2",
        }
        exe_1 = Exefile(**exe_dict_1)
        exe_2 = Exefile(**exe_dict_2)
        assert exe_1 <= exe_2

    def test_gt_pass(self):
        exe_dict_1 = {
            "path": "appexemple",
            "version": "0.1.8",
        }
        exe_dict_2 = {
            "path": "appexemple1",
            "version": "0.0.2",
        }
        exe_1 = Exefile(**exe_dict_1)
        exe_2 = Exefile(**exe_dict_2)
        assert exe_1 > exe_2

    def test_ge_pass(self):
        exe_dict_1 = {
            "path": "appexemple",
            "version": "8.5.1",
        }
        exe_dict_2 = {
            "path": "appexemple1",
            "version": "8.4.9",
        }
        exe_1 = Exefile(**exe_dict_1)
        exe_2 = Exefile(**exe_dict_2)
        assert exe_1 >= exe_2
