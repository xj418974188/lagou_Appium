#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver

class TestSearch:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        testcode = "测试1"
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/gq_")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/ffq")
        el2.send_keys("西西")
        # el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView")
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/dnb")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/dtv")
        el4.send_keys(testcode)
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/dtr")
        el5.click()

        el = self.driver.find_elements_by_id("com.tencent.wework:id/dtg")
        assert testcode == el[-1].text

