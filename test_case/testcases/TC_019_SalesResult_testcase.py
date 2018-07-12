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
from data.TestData import Data
import time


class SalesResultsTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

#=======================================================================================================
    # 顾问创建新退款
    def test_1_createSalesResult_Sales(self):
        self.user_login_verify()
        sales_results = SalesResultApprovalPage(self.driver)
        sales_results.createSalesResult_Sales(Data.sal_clt_name)
        sales_results.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__create_Sales_Result.png")


if __name__ == '__main__':
    unittest.main()


