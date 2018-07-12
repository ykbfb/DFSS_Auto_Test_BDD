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
from test_case.page_obj.BillReceiptPage import NewOrderPage
from data.TestData import Data
import time


class BillTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.finance_name, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)


    # 创建收款单
    def test_1_createBillReceipt(self):
        self.user_login_verify()
        new_Bill = NewOrderPage(self.driver)
        new_Bill.createBill(Data.ContractCode)
        new_Bill.setWaitTime(2)

        #校验收款单是否创建成功
        new_Bill.backtoBillList()
        new_Bill.searchBillReceipt(Data.ContractCode)
        self.assertEqual(new_Bill.verifyBillReceiptActionSucess().strip(),"未结算")
        functions.insert_img(self.driver, current_time + "__createBill.png")
        new_Bill.setWaitTime(2)
        new_Bill.close()

    # 结算收款单
    def test_2_caculateBillReceipt(self):
        self.user_login_verify()
        new_Bill = NewOrderPage(self.driver)
        new_Bill.caculateBill(Data.ContractCode)
        new_Bill.setWaitTime(2)
        functions.insert_img(self.driver, current_time + "__caculateBill.png")

        #校验收款单是否结算成功
        new_Bill.searchBillReceipt(Data.ContractCode,'已结算')
        self.assertEqual(new_Bill.verifyBillReceiptActionSucess().strip(), "已结算")
        functions.insert_img(self.driver, current_time + "__VerifyCaculateBillSucess.png")
        new_Bill.setWaitTime(2)
        new_Bill.close()

if __name__ == '__main__':
    unittest.main()