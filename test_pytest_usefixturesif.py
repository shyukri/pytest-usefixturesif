# -*- coding: utf-8 -*-

pytest_plugins = "pytester"
import pytest


class TestUseFixturesIf(object):

    def setup_method(self, method):
        self.conftest = open("./pytest_usefixturesif.py", "r")
