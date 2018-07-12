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
from test_case.page_obj.CallDetailPage import CallDetailPage
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="yanfang", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    #呼叫保存
    def aa_test_0001_call(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)

        call_page = CallDetailPage(self.driver)
        call_page.callClient()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        call_page.close()

    #列表右键呼叫
    def aa_test_0002_rightCall(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)

        call_page = CallDetailPage(self.driver)
        call_page.rigthClickCall()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        call_page.close()

    #列表呼叫
    def aa_test_0003_listCall(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)

        call_page = CallDetailPage(self.driver)
        call_page.callFromList()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        call_page.close()

    #列表呼叫
    def test_0004_multCall(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)

        call_page = CallDetailPage(self.driver)
        call_page.multCall()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        call_page.close()



if __name__ == '__main__':
    unittest.main()
