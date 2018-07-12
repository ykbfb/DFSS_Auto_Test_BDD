# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: Administrator
'''
import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ApproveIntviewPage import ApproveIntviewPage
from test_case.page_obj.base import *
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales_manager, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    #邀约审批
    def test_0001_ApproveIntview(self):
        self.user_login_verify()
        intview_appr_page = ApproveIntviewPage(self.driver)
        intview_appr_page.approveIntview()
        functions.insert_img(self.driver, current_time + "__intview_approve_sucess.png")

        #校验邀约是否审批成功
        intview_appr_page.gotoIntviewCompleteList()
        #self.assertIn(Data.lnk_moblie,intview_appr_page.verfifyIntviewAppvSuccess())
        self.assertEqual(intview_appr_page.verfifyIntviewAppvSuccess().strip(),Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__verify_intview_approve_success.png")
        intview_appr_page.close()

    #邀约DC
    def aa_test_0002_ApproveIntview(self):
        self.user_login_verify()
        intview_appr_page = ApproveIntviewPage(self.driver)
        intview_appr_page.intview_DC()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        intview_appr_page.close()