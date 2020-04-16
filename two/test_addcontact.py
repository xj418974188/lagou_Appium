#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestAdd:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    # def setup(self):
    #     pass
    #
    # def teardown(self):
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()

    @pytest.fixture()
    def add_fixture(self):
        yield
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, gender, phonenum",[
        ("霍格name6", "男", "13801010106"),
        ("霍格name7", "女", "13801010107")
    ])
    def test_addcontact(self, add_fixture, username, gender, phonenum):

        # 进入到 通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        # 滚动查找 添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                               'new UiSelector().scrollable(true).instance(0))'
                                                               '.scrollIntoView(new UiSelector().text("添加成员")'
                                                               '.instance(0));').click()
        # 手动添加
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c56").click()

        sleep(2)

        # 验证 添加联系人页面

        current_act = self.driver.current_activity

        print(current_act)

        assert ".contact.controller.ContactAddActivity" in current_act

        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(username)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/at7']").click()
        # 选择性别
        if gender == '男':
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()
        else :
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("女")').click()

        # 输入手机号
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phonenum)

        # 点击 保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()

        sleep(2)
        print(self.driver.page_source)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        # assert "添加成功" in self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text



