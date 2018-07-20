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
from test_case.page_obj.ApproveSalesResultPage import SalesResultApprovalPage
from test_case.page_obj.base import *
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="yanghongyuan", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    #销售喜报审批--分公司财务
    def test_0001_ApproveSalesResult_Finance(self):
        self.user_login_verify(username=Data.finance_name, password="123456", city=Data.city)
        chan_appr_page = SalesResultApprovalPage(self.driver)
        chan_appr_page.approveSalesResult_Finance(Data.sal_clt_name)

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司)
        functions.insert_img(self.driver, current_time + "__sales_result_approve_Finance.png")
        chan_appr_page.close()

    #销售喜报审批--数据部
    def test_0002_ApproveSalesResult_DataManager(self):
        self.user_login_verify(username="longlixia", password="123456", city="shanghai")
        chan_appr_page = SalesResultApprovalPage(self.driver)
        chan_appr_page.approveSalesResult_DataManager(Data.sal_clt_name)

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司)
        functions.insert_img(self.driver, current_time + "__sales_result_approve_DataManager.png")
        chan_appr_page.close()

if __name__ == '__main__':
    unittest.main()