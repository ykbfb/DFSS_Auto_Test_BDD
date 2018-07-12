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
from test_case.page_obj.ForceCloseOrderPage import ForceCloseOrderPage
from data.TestData import Data
import time


class ForceCloseOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="zhangyu1087", password="123456", city="shanghai"):
        login(self.driver).user_login(username, password, city)

    #强制结案
    def test_0001_ForceCloseOrder(self):
        self.user_login_verify()
        close_order_page = ForceCloseOrderPage(self.driver)
        close_order_page.forceCloseOrder(Data.cmp_name)

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__chanl_result_approve_Director.png")
        close_order_page.close()


if __name__ == '__main__':
    unittest.main()