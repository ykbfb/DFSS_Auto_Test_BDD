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
from test_case.page_obj.LoanRedRefundPage import LoanRefundPage
from test_case.page_obj.base import *
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.service_manager, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    # 融服填写放款红冲
    def aa_test_0001_createLoanRedRefund(self):
        self.user_login_verify(username='xulingyun',password='123456',city='shanghai')
        rebate = LoanRefundPage(self.driver)
        rebate.createLoanRedRefund(Data.rebate_suborder_no)
        rebate.setWaitTime(2)

        #校验接单成功
        # self.assertEqual(rebate.verifyOrderAcceptSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__createLoanRedRefundSuccess.png")
        rebate.close()

    def aa_test_0002_approveLoanRedRefund(self):
        self.user_login_verify(username='xulingyun',password='123456',city='shanghai')
        rebate = LoanRefundPage(self.driver)
        rebate.approveRedRefund(Data.rebate_suborder_no)
        rebate.setWaitTime(2)

        #校验接单成功
        # self.assertEqual(rebate.verifyOrderAcceptSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__createLoanRedRefundSuccess.png")
        rebate.close()

    def test_0003_approveLoanRedRefund_DataManager(self):
        self.user_login_verify(username='longlixia',password='123456',city='shanghai')
        rebate = LoanRefundPage(self.driver)
        rebate.approveRedLoanRedRefund_DataManager(Data.rebate_suborder_no)
        rebate.setWaitTime(2)

        #校验接单成功
        # self.assertEqual(rebate.verifyOrderAcceptSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__createLoanRedRefundSuccess.png")
        rebate.close()


if __name__ == '__main__':
    unittest.main()


