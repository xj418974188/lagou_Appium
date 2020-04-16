#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------   下面是使用 Appium Inspector 生成的代码块  ------
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["autoGrantPermissions"] = "true"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4724/wd/hub", caps)

el1 = driver.find_element_by_id("com.tencent.wework:id/gq_")
el1.click()
el2 = driver.find_element_by_id("com.tencent.wework:id/ffq")
el2.send_keys("西西")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView")
el3.click()
el4 = driver.find_element_by_id("com.tencent.wework:id/dtv")
el4.send_keys("测试")
el5 = driver.find_element_by_id("com.tencent.wework:id/dtr")
el5.click()

driver.quit()


