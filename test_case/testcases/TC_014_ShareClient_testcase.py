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
from test_case.page_obj.ShareClientPage import ShareClientPage
from test_case.page_obj.createClientPage import createClient
from test_case.page_obj.CallDetailPage import CallDetailPage
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="yanfang", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    #列表页右键客户共享
    def test_0001_rigthClickShareClient(self):
        self.user_login_verify()
        create_client = createClient(self.driver)
        create_client.createNewClient(Data.share_phone1) #创建一个新客户

        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.share_phone1)

        share_page = ShareClientPage(self.driver)
        share_page.shareClientByRigthClick()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        share_page.close()

    #列表页右右上角客户共享
    def test_0002_listShareClient(self):
        self.user_login_verify()
        create_client = createClient(self.driver)
        create_client.createNewClient(Data.share_phone2) #创建一个新客户

        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.share_phone2)

        share_page = ShareClientPage(self.driver)
        share_page.shareClientFromList()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        share_page.close()

    #呼叫详情页客户共享
    def test_0003_listShareClient(self):
        self.user_login_verify()
        create_client = createClient(self.driver)
        create_client.createNewClient(Data.share_phone3) #创建一个新客户

        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.share_phone3)

        call_page = CallDetailPage(self.driver)
        call_page.openCallDetailPage() #呼叫页面共享

        share_page = ShareClientPage(self.driver)
        share_page.shareClientFromCallPage()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        share_page.close()



if __name__ == '__main__':
    unittest.main()
