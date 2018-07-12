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
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.SalseManagerAsignOrderPage import SaleseOrderAsignPage
from data.TestData import Data
import time


class SalseOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales_manager, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    # 接单
    def test_1_acceptSalesOrder(self):
        self.user_login_verify()
        salse_order = SaleseOrderAsignPage(self.driver)
        salse_order.acceptSalseOrder(Data.cmp_name)
        salse_order.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__SalesOrderAccept.png")

        #校验销售订单接单成功
        self.assertEqual(salse_order.verifySalesOrderAcceptSucess().strip(),'暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__VerifySalesOrderAccept.png")
        salse_order.close()

    # 派单
    def test_2_asignSalesOrder(self):
        self.user_login_verify()
        salse_order = SaleseOrderAsignPage(self.driver)
        salse_order.asignSalesOrder(Data.cmp_name)
        salse_order.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__myClient_fuzzysearch.png")

        #校验销售订单派单成功
        self.assertIn(str(salse_order.verifySalesOrderAsignedSuccess().strip()).split('.')[0],Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__VerifySalesOrderAsignedSucess.png")
        salse_order.close()

if __name__ == '__main__':
    unittest.main()


