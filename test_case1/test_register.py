# -*- coding: UTF-8 -*-
import pytest

from page1.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()
