#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium_zhibo_demo.three.page.base_page import BasePage
from appium_zhibo_demo.three.page.main import Main
from appium import webdriver

class App(BasePage):
    def start(self):
        # 启动 app
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)