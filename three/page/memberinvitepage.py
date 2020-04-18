#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from appium_zhibo_demo.three.page.addresslistpage import AddressListPage
from appium.webdriver.common.mobileby import MobileBy

from appium_zhibo_demo.three.page.base_page import BasePage
# from appium_zhibo_demo.three.page.contactaddpage import ContactAddPage


class MemberInvitePage(BasePage):

    def click_menualadd(self):
        from appium_zhibo_demo.three.page.contactaddpage import ContactAddPage

        self.find(MobileBy.ID, "com.tencent.wework:id/c56").click()

        return ContactAddPage(self._driver)

    def click_back(self):
        from appium_zhibo_demo.three.page.addresslistpage import AddressListPage
        return AddressListPage(self._driver)

    def veriy_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        return self