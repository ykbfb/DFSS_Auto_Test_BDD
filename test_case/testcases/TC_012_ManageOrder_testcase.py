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
from test_case.page_obj.ServiceOrderManagePage import ServiceManageOrderPage
from test_case.page_obj.base import *
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.service_manager, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    # 融服接单订单
    def aa_test_0001_acceptOrder(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.acceptOrder(Data.cmp_name)
        my_order.setWaitTime(2)

        #校验接单成功
        self.assertEqual(my_order.verifyOrderAcceptSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__myOrder_verifyOrderAcceptSucess.png")
        my_order.close()

    #【贷前调查】转入【专家测评】
    #@unittest.Myskip #如果上一个case执行失败，则跳过次case
    def aa_test_0002_moveToExpert(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.moveToExpert(Data.cmp_name)

        #校验转入专家测评成功
        self.assertEqual(my_order.verifyOrderMovetoExprtSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__myOrder_movetoexpert.png")
        my_order.close()

    #【专家测评】转入【机构寻访】
    #@unittest.Myskip
    def aa_test_0003_moveToAgency(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.moveToAgencySearch(Data.cmp_name)
        my_order.setWaitTime(2)

        #校验转入专家测评成功
        self.assertEqual(my_order.verifyOrderMovetoAgencyResearchSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__myOrder_movetoAgency.png")
        my_order.setWaitTime(2)
        my_order.close()

    #创建意向单
    #@unittest.Myskip
    def aa_test_0004_createAimOrder(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.createAimOrder(Data.cmp_name,Data.org_name,Data.prd_name)
        my_order.setWaitTime(2)
        self.assertIsNot(my_order.verifyAimOrderCreateSucess().strip(),'0/0/0/0/0')
        #self.assertEqual(my_order.verifyAimOrderCreateSucess().strip(), '暂无查询到任何数据...')
        functions.insert_img(self.driver, current_time + "__myOrder_createAimOrder.png")
        my_order.setWaitTime(2)
        my_order.close()

    #创建子订单
    #@unittest.Myskip
    def aa_test_0005_createSubOrder(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.createSubOrder(Data.cmp_name,Data.credit_manager,Data.org_name)
        my_order.setWaitTime(2)
        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myOrder_createSubsOrder.png")
        my_order.setWaitTime(2)
        my_order.close()

    #子订单【贷前辅导】转入【机构审批】
    #@unittest.Myskip
    def aa_test_0006_moveSubOrderToOrgApproval(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.moveToOrgApproval(Data.cmp_name)
        my_order.setWaitTime(2)
        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myOrder_moveSubsOrderToOrgApproval.png")
        my_order.setWaitTime(2)
        my_order.close()

    #【机构审批】--信贷经理评价
    #@unittest.Myskip
    def aa_test_0007_estimateCreditManager(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.estimateCreditManager(Data.cmp_name)
        my_order.setWaitTime(2)
        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myOrder_moveSubsOrderToOrgApproval.png")
        my_order.close()

    #【机构审批】--机构审批：不通过
    #@unittest.Myskip
    def aa_test_0008_OrgApproveNotPass(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.orgApproveReject(Data.cmp_name)
        my_order.setWaitTime(2)
        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myOrder_OrgApprove_reject.png")
        my_order.setWaitTime(2)
        my_order.close()

    #【机构审批】--机构审批： 通过
    #@unittest.Myskip
    def aa_test_0009_OrgApprovePass(self):
        self.user_login_verify()
        time.sleep(1)
        b = Page(self.driver)
        time.sleep(1)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.orgApprovePass(Data.cmp_name)
        my_order.setWaitTime(2)
        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myOrder_OrgApprov_pass.png")
        my_order.setWaitTime(2)
        my_order.close()

    #【机构审批】--子订单成交，提交放款喜报
    #@unittest.Myskip
    def test_0010_submitChanelResult(self):
        self.user_login_verify()
        time.sleep(2)
        b = Page(self.driver)
        b.close_alert()
        my_order = ServiceManageOrderPage(self.driver)
        my_order.submitChanelResult(Data.cmp_name)
        my_order.setWaitTime(2)
        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myOrder_OrgApprove_pass.png")
        my_order.setWaitTime(2)
        my_order.close()

if __name__ == '__main__':
    unittest.main()


