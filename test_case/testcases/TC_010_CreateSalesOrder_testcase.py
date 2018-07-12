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
from test_case.page_obj.CreateOrderPage import NewOrderPage
from data.TestData import Data
import time


class OrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    # 创建企业主、个体户订单
    def test_1_createOrder_CMP(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__myClient_fuzzysearch.png")

        order = NewOrderPage(self.driver)
        order.createOrderForCMP()
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")

        # 校验销售订单是否创建成功
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        order.clickOrderTab()
        my_client.setWaitTime(2)
        self.assertEqual(order.verifySalesOrderCreateSucess().strip(), Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__myClient_verifySalesOrderCreateSucessCMP.png")
        my_client.setWaitTime(2)
        my_client.close()

    # 创建工薪族、其他订单
    def aa_test_2_createOrder_Person(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(my_client.search_by_fuzzy(), Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__myClient_fuzzysearch.png")

        order = NewOrderPage(self.driver)
        order.createOrderForPerson()
        functions.insert_img(self.driver, current_time + "__myClient_orderCreatePerson.png")

        # 校验销售订单是否创建成功
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        order.clickOrderTab()
        self.assertEqual(order.verifySalesOrderCreateSucess().strip(), Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__myClient_verifySalesOrderCreateSucessPerson.png")
        my_client.close()


if __name__ == '__main__':
    unittest.main()


