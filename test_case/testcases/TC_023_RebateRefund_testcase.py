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
from test_case.page_obj.RebateRefundPage import RebatePage
from test_case.page_obj.base import *
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.service_manager, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    # 融服填写返佣喜报
    def AA_test_0001_createRebaterefund(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        rebate = RebatePage(self.driver)
        rebate.createRedRebateRefund_Sales(Data.rebate_suborder_no)
        rebate.setWaitTime(2)

        #校验接单成功
        # self.assertEqual(rebate.verifyOrderAcceptSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__rebateSubmitSuccess.png")
        rebate.close()

    #返佣红冲审批--总监
    def AA_test_0002_approveRebaterefund_Director(self):
        self.user_login_verify(username=Data.ser_director_manager,password='123456',city=Data.city)
        rebate = RebatePage(self.driver)
        rebate.approveRebateRedRefund_Director(Data.rebate_suborder_no)
        rebate.setWaitTime(2)

        #校验接单成功
        # self.assertEqual(rebate.verifyOrderAcceptSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__ApproveRebateSuccess_Director.png")
        rebate.close()

    #返佣红冲审批--数据部
    def test_0003_approveRebaterefund_DataManager(self):
        self.user_login_verify(username='longlixia',password='123456',city='shanghai')
        rebate = RebatePage(self.driver)
        rebate.approveRebateRedRefund_DataManager(Data.rebate_suborder_no)
        rebate.setWaitTime(2)

        #校验接单成功
        # self.assertEqual(rebate.verifyOrderAcceptSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__ApproveRebateSuccess_DataManager.png")
        rebate.close()

if __name__ == '__main__':
    unittest.main()


