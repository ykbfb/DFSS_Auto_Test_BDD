#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: Administrator
'''
import unittest,sys
sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit,functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from data.TestData import Data
import time

class MyClientTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)
    

    #修改联系人
    def test_1_modifyCltLnk(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        my_client.modifyLnkMan('坤坤测试','测试总经理','创始人','8888888','yk@test.com')
        self.assertEqual(my_client.verify_modify_lnkMan(),'坤坤测试')
        functions.insert_img(self.driver,current_time+"__myClient_modifyLnkMan.png")
        my_client.close()

    #模糊查询
    def test_2_fuzzySearch(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(my_client.search_by_fuzzy(),'坤坤测试')
        functions.insert_img(self.driver,current_time+"__myClient_fuzzysearch.png")
        my_client.close()



 

if __name__ == '__main__':
    unittest.main()        
        
        
        