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
from data.ReadTestData import Data
import time

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
init = Data()

class MyClientTests(myunit.MyTest):

    # 登录融管系统
    def user_login_verify(self, username='', password="", city=''):
        login(self.driver).user_login(username, password, city)
    

    #修改联系人
    def test_1_modifyCltLnk(self):
        user = init.getUser('销售顾问')
        self.user_login_verify(username=user['username'],password =user['password'],city=user['city'])
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(init.getClient('新客户')['lnk_mobile'])
        my_client.setWaitTime(2)
        my_client.modifyLnkMan('坤坤测试','测试总经理','创始人','8888888','yk@test.com')
        self.assertEqual(my_client.verify_modify_lnkMan(),'坤坤测试')
        functions.insert_img(self.driver,current_time+"__myClient_modifyLnkMan.png")
        my_client.close()

    #模糊查询
    def test_2_fuzzySearch(self):
        user = init.getUser('销售顾问')
        self.user_login_verify(username=user['username'],password =user['password'],city=user['city'])
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(init.getClient('新客户')['lnk_mobile'])
        my_client.setWaitTime(2)
        self.assertEqual(my_client.search_by_fuzzy(),'坤坤测试')
        functions.insert_img(self.driver,current_time+"__myClient_fuzzysearch.png")
        my_client.close()



 

if __name__ == '__main__':
    unittest.main()        
        
        
        