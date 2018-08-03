# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: kun yang
'''
import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.createClientPage import createClient
from data.ReadTestData import Data
import time

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
init = Data()

class createNewClient(myunit.MyTest):

    # 登录融管系统
    def user_login_verify(self, username='', password="", city=''):
        login(self.driver).user_login(username, password, city)

    # 测试创建客户-电话号码已经存在
    def test_1_verify_mobileNo_isExist(self):
        user = init.getUser('销售顾问')
        self.user_login_verify(username=user['username'],password =user['password'],city=user['city'])
        new_client = createClient(self.driver)
        new_client.setWaitTime(2)
        new_client.open_rapidOperation()
        new_client.open_newClient()
        new_client.switchToNewClientFrame()
        new_client.inputMobile(init.getClient('老客户')['lnk_mobile'])
        new_client.checkMobileIsDuplicate()
        self.assertEqual(new_client.check_num_isExist(), init.getExpectedResult('验证客户已存在'))
        functions.insert_img(self.driver, current_time + "__Client_isExist.png")
        new_client.close()

    #测试创建客户
    def test_2_create_newClient(self):
        user = init.getUser('销售顾问')
        self.user_login_verify(username=user['username'],password =user['password'],city=user['city'])
        new_client = createClient(self.driver)
        new_client.setWaitTime(2)
        new_client.open_rapidOperation()
        new_client.open_newClient()
        new_client.switchToNewClientFrame()
        new_client.inputMobile(init.getClient('新客户')['lnk_mobile'])
        new_client.checkMobileIsDuplicate()
        time.sleep(1)
        self.assertEqual(new_client.check_num_isExist(), init.getExpectedResult('验证客户不存在'))
        functions.insert_img(self.driver, current_time + "__Client_isNotExist.png")
        new_client.selectCltExeStatus()
        new_client.selectLoanArea()
        new_client.saveClient()
        time.sleep(1)
        functions.insert_img(self.driver, current_time + "__Client_isCreateSuccess.png")#客户详情

        #校验客户是否创建成功
        new_client.checkClientCreateSuccess(init.getClient('新客户')['lnk_mobile'])
        self.assertEqual(new_client.check_client_createSucess(), '')
        functions.insert_img(self.driver, current_time + "__CheckClient_isCreateSuccess.png")
        new_client.close()




if __name__ == '__main__':
    unittest.main()


