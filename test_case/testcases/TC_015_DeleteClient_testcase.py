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
from test_case.page_obj.DeleteClientPage import DeleteClientPage
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="yanfang", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    #列表页右键客户删除
    def test_0001_rigthClickDeleteClient(self):
        self.user_login_verify()
        create_client = createClient(self.driver)
        create_client.createNewClient(Data.delete_phone1) #创建一个新客户

        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.delete_phone1)

        del_page = DeleteClientPage(self.driver)
        del_page.deleteClientByRigthClick()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__deleteClientByRightClick.png")
        del_page.close()

    #列表页右右上角客户删除
    def test_0002_listDeleteClient(self):
        self.user_login_verify()
        create_client = createClient(self.driver)
        create_client.createNewClient(Data.delete_phone2) #创建一个新客户

        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.delete_phone2)

        del_page = DeleteClientPage(self.driver)
        del_page.deleteClientFromList()

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__deleteClientFromList.png")
        del_page.close()




if __name__ == '__main__':
    unittest.main()
