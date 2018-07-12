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
from test_case.page_obj.RefundPage import RefundPage
from data.TestData import Data
import time


class RefundTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

#=======================================================================================================
    # 顾问创建新退款
    def aa_test_1_createRefund_SALES(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(my_client.search_by_fuzzy(), Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__myClient_fuzzysearch.png")
        my_client.setWaitTime(2)

        refund = RefundPage(self.driver)
        refund.createRefund()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #总监新退费审批
    def test_2_approveRefund_Director(self):
        self.user_login_verify(username='pengxiaoli',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveRefund_Director(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #分总新退费审批
    def test_3_approveRefund_DivManager(self):
        self.user_login_verify(username='renyuan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveRefund_DivManager(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #分公司财务新退费审批
    def test_4_approveRefund_Finance(self):
        self.user_login_verify(username='sunquan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveRefund_Finance(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #总部应收会计新退费审批
    def test_5_approveRefund_Accantant(self):
        self.user_login_verify(username='duanxuesa',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveRefund_Accountant(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #CFO新退费审批
    def test_6_approveRefund_CFO(self):
        self.user_login_verify(username='lingju',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveRefund_CFO(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #总部付款出纳新退费审批
    def test_7_approveRefund_Cash(self):
        self.user_login_verify(username='yangshuai',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveRefund_Cashier(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

#===================================================================================================================
    #顾问创建意向金退费
    def bb_test_8_aimRefund_Sales(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(my_client.search_by_fuzzy(), Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__myClient_fuzzysearch.png")
        my_client.setWaitTime(2)

        refund = RefundPage(self.driver)
        refund.createAimRefund_Sales()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #意向金退费审批--总监
    def bb_test_9_approveAimRefund_Director(self):
        self.user_login_verify(username='pengxiaoli',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveAimRefund_Director()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #意向金退费审批--分总
    def bb_test_10_approveAimRefund_DivManager(self):
        self.user_login_verify(username='renyuan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveAimRefund_DivManager()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #意向金退费审批--分公司财务
    def bb_test_11_approveRefund_Finance(self):
        self.user_login_verify(username='sunquan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveAimRefund_Finance()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #意向金退费审批--总部应收会计
    def bb_test_12_approveRefund_Accountant(self):
        self.user_login_verify(username='duanxuesa',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveAimRefund_Accountant()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #意向金退费审批--总部付款出纳
    def bb_test_13_approveRefund_Cashier(self):
        self.user_login_verify(username='yangshuai',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveAimRefund_Cashier()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

#=====================================================================================================
    #创建紧急退费--分总
    def cc_test_14_createUrgencyRefund_DivManager(self):
        self.user_login_verify(username='renyuan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.createUrgencyRefund(Data.ur_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #紧急退费审批--分公司财务
    def cc_test_15_approveUrgencyRefund_Finance(self):
        self.user_login_verify(username='sunquan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveUrgencyRefund_Finance(Data.ur_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #紧急退费审批--总部应收会计
    def cc_test_16_approveUrgencyRefund_Account(self):
        self.user_login_verify(username='duanxuesa',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveUrgencyRefund_Accountant(Data.ur_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #紧急退费审批--CFO
    def cc_test_17_approveUrgencyRefund_CFO(self):
        self.user_login_verify(username='lingju',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveUrgencyRefund_CFO(Data.ur_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #紧急退费审批--总部付款出纳
    def cc_test_18_approveUrgencyRefund_Cashier(self):
        self.user_login_verify(username='yangshuai',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveUrgencyRefund_Cashier(Data.ur_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #紧急退费审批--销售经理
    def cc_test_19_approveUrgencyRefund_SalesManager(self):
        self.user_login_verify(username='wangweiwei',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveUrgencyRefund_SalesManager(Data.ur_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #紧急退费终审--分公司财务
    def cc_test_20_finalApproveUrgencyRefund_Finance(self):
        self.user_login_verify(username='sunquan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.final_ApproveUrgencyRefund_Finance(Data.ur_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

#=====================================================================================================================================
    #强制退费创建--客服专员
    def dd_test_21_createForceRefund_CustomerService(self):
        self.user_login_verify(username='chenxiang5134',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.createForceRefund(Data.force_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #强制退费审批--客服专员
    def dd_test_22_approveForceRefund_CustomerService(self):
        self.user_login_verify(username='chenxiang5134',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveForceRefund_CustomerScevice(Data.force_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #强制退费审批--客服总监
    def dd_test_23_approveForceRefund_CustomerService(self):
        self.user_login_verify(username='liujianlin',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveForceRefund_ServiceDirector(Data.force_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #强制退费审批--分公司财务
    def dd_test_24_approveForceRefund_CustomerService(self):
        self.user_login_verify(username='sunquan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveForceRefund_Finance(Data.force_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #强制退费审批--分公司财务
    def dd_test_25_approveForceRefund_Accountant(self):
        self.user_login_verify(username='duanxuesa',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveForceRefund_Accountant(Data.force_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #强制退费审批--CFO
    def dd_test_26_approveForceRefund_CFO(self):
        self.user_login_verify(username='lingju',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveForceRefund_CFO(Data.force_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #强制退费审批--总部付款出纳
    def dd_test_27_approveForceRefund_Cashier(self):
        self.user_login_verify(username='yangshuai',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveForceRefund_Cashier(Data.force_clt_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

if __name__ == '__main__':
    unittest.main()


