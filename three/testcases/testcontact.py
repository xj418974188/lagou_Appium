#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from appium_zhibo_demo.three.page.app import App


class TestAddContact():

    def setup(self):
        self.main = App().start().main()
        print(self.main)

    @pytest.mark.parametrize("username, gender, phonenum",yaml.safe_load(open("../data/contact.yml")))
    def test_addcontact(self, username, gender, phonenum):
        self.main.goto_addresslist().\
            click_addmember().click_menualadd().\
            input_name(username).set_gender(gender).input_phone(phonenum).click_save().veriy_toast().click_back()