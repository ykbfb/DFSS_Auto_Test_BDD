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
from test_case.page_obj.FinceBookInfoPage import finceBookInfo
from data.TestData import Data
import time


class FinanceBookTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    # 测试修改保存需求书
    def test_1_financeBookInfo_save(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__myClient_fuzzysearch.png")

        fin_book = finceBookInfo(self.driver)#打开需求书
        fin_book.saveFinancBookInfo()
        my_client.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__financeBookInfo_afterSave.png")

        #校验需求书是否保存成功
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(fin_book.verify_finceBookInfo_save_success(),'自动化测试有限公司')
        functions.insert_img(self.driver,current_time+"__myClient_verifyFinBookSave.png")
        my_client.close()

    #测试修改提交需求书
    def test_2_financeBookInfo_submit(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__myClient_aftersearch.png")

        fin_book = finceBookInfo(self.driver)#打开需求书
        fin_book.submitFinanceBookInfo()
        fin_book.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__financeBookInfo_afterSubmit.png")
        # fin_book.close()

        #校验需求书是否保存成功
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(fin_book.verify_finceBookInfo_save_success(),Data.cmp_name)
        functions.insert_img(self.driver,current_time+"__myClient_verifyFinBookSubmit.png")
        my_client.setWaitTime(2)
        my_client.close()



if __name__ == '__main__':
    unittest.main()


