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
from test_case.page_obj.createClientPage import createClient
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="yanfang", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    #将客户划转到大项目部
    def test_0001_moveClientToBigProject(self):
        self.user_login_verify()
        create_client = createClient(self.driver)
        create_client.createNewClient(Data.move_client_phone) #创建一个新客户

        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.move_client_phone)
        my_client.moveClientToBigProject()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__deleteClientByRightClick.png")
        my_client.close()


if __name__ == '__main__':
    unittest.main()
