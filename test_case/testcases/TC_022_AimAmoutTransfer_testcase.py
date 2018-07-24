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
from test_case.page_obj.AimRefundTransferPage import AimRefundTransPage
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="yanfang", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    #顾问创建意向金转业绩
    def aa_test_0001_createAimAmtTransfer(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.aim_clt_phone)

        aim_trans = AimRefundTransPage(self.driver)
        aim_trans.createAimTransfer()

        functions.insert_img(self.driver, current_time + "__aim_transfer.png")
        aim_trans.close()

    #销售经理审批意向金转业绩
    def aa_test_0002_approveAimAmtTransfer_SalesManager(self):
        self.user_login_verify(Data.sales_manager,'123456',Data.city)

        aim_trans = AimRefundTransPage(self.driver)
        aim_trans.approveAimTransfer(Data.aim_clt_phone)

        functions.insert_img(self.driver, current_time + "__approve_aim_transfer_SalesManager.png")
        aim_trans.close()

    #销售总监审批意向金转业绩
    def aa_test_0003_approveAimAmtTransfer_Director(self):
        self.user_login_verify(Data.sales_director,'123456',Data.city)

        aim_trans = AimRefundTransPage(self.driver)
        aim_trans.approveAimTransfer_Director(Data.aim_clt_phone)

        functions.insert_img(self.driver, current_time + "__approve_aim_transfer_Director.png")
        aim_trans.close()

    #分总审批意向金转业绩
    def aa_test_0004_approveAimAmtTransfer_DivManager(self):
        self.user_login_verify(Data.div_manager,'123456',Data.city)

        aim_trans = AimRefundTransPage(self.driver)
        aim_trans.approveAimTransfer_DivManager(Data.aim_clt_phone)

        functions.insert_img(self.driver, current_time + "__approve_aim_transfer_DivManager.png")
        aim_trans.close()

    #数据部审批意向金转业绩
    def test_0005_approveAimAmtTransfer_DataManager(self):
        self.user_login_verify('longlixia','123456','shanghai')

        aim_trans = AimRefundTransPage(self.driver)
        aim_trans.approveAimTransfer_DataManager(Data.aim_clt_phone)

        functions.insert_img(self.driver, current_time + "__approve_aim_transfer_DataManager.png")
        aim_trans.close()
if __name__ == '__main__':
    unittest.main()
