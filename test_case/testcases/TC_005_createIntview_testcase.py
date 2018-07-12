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
from test_case.models import myunit, functions,Screen
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.createIntviewPage import NewIntviewPage
from data.TestData import Data
import time


class ContractTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)


    # 创建已来访邀约
    # @Screen(webdriver)
    def test_0001_createIntview(self):
        try:
            self.user_login_verify()
            my_client = myClient(self.driver)
            my_client.gotoMyClientList_All(Data.lnk_moblie)
            my_client.setWaitTime(2)

            intview_page = NewIntviewPage(self.driver)
            intview_page.createIntview()
            functions.insert_img(self.driver, current_time + "__createIntview.png")

            #创建成功之后 返回邀约【待审】列表页，校验是否创建成
            intview_page.gobacktoIntviewList()
            self.assertEqual(intview_page.verifyIntviewCreateSucess(),'自动化测试：创建邀约')
            functions.insert_img(self.driver, current_time + "__CheckCreateIntviewSucess.png")
            my_client.close()
        except Exception as e:
            print('Case执行异常：%s' %e)
            functions.insert_img(self.driver,current_time + "__caseError.png")
            raise


    # 创建DC访邀约
    def aa_test_0002_createIntview_DC(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        intview_page = NewIntviewPage(self.driver)
        intview_page.createIntview_DC()
        functions.insert_img(self.driver, current_time + "__createDCIntview.png")

        # 修改成功之后 返回邀约【待审】列表页，校验是否修改成功
        intview_page.gobacktoDraftIntviewList()
        self.assertEqual(intview_page.verifyDCIntviewCreateSucess(), '修改')
        functions.insert_img(self.driver, current_time + "__CheckCreateDCIntviewSucess.png")
        my_client.close()

    # 修改邀约
    def aa_test_0003_modifyIntview(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        intview_page = NewIntviewPage(self.driver)
        intview_page.modifyIntview()
        functions.insert_img(self.driver, current_time + "__modifyIntview.png")

        # 创建成功之后 返回邀约【待审】列表页，校验是否创建成
        intview_page.gobacktoIntviewList()
        self.assertEqual(intview_page.verifyIntviewCreateSucess(), '自动化测试：修改邀约')
        functions.insert_img(self.driver, current_time + "__CheckModifyIntviewSucess.png")
        my_client.close()


if __name__ == '__main__':
    unittest.main()

