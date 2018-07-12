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
from test_case.page_obj.createContractPage import NewContractPage
from data.TestData import Data
import time


class ContractTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)


    # 创建会员合同
    def test_1_createVIPContract(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        contract_page = NewContractPage(self.driver)
        contract_page.createVIPContract()
        functions.insert_img(self.driver, current_time + "__createVIPContract.png")

        #验证合同是否创建成功
        contract_page.gobackToContractlist()
        self.assertEqual(contract_page.verifyContractCreateSucess(),'发票申请')
        functions.insert_img(self.driver, current_time + "__CheckCreateVIPContractSucess.png")
        my_client.setWaitTime(2)
        my_client.close()

    # 创建外包合同
    def aa_test_2_createBPOContract(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        contract_page = NewContractPage(self.driver)
        contract_page.createBPOContract()
        functions.insert_img(self.driver, current_time + "__createBPOContract.png")

        #验证外包合同是否创建成功
        contract_page.gobackToContractlist()
        self.assertEqual(contract_page.verifyContractCreateSucess(),'发票申请')
        functions.insert_img(self.driver, current_time + "__CheckCreateBPOContract.png")
        my_client.setWaitTime(2)
        my_client.close()

    #外包转会员
    def AA_test_BPOContractTransToVIP(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        contract_page = NewContractPage(self.driver)
        contract_page.BPOContractTransToVIP()
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__BPOContractChangeToVIP.png")
        my_client.close()

if __name__ == '__main__':
    unittest.main()


