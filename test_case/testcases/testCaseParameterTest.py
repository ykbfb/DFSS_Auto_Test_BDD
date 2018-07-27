#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018年1月04日

@author: kun yang
登录参数化：从excel中读取数据
'''

import unittest,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from test_case.models import myunit,functions,getDir
from test_case.page_obj.loginPage import login
from test_case.models.common import get_excel_value
import time
import paramunittest

proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
loginCase = get_excel_value("loginCase.xls", "login_test")


@paramunittest.parametrized(*loginCase)
class loginTest(myunit.MyTest):

    def setParameters(self, case_name, username, password,city, excepted):
        """
        从 excel 中获取用例
        :param case_name: 用例名称
        :param username: 用户名
        :param password: 密码
        :param city: 城市       :
        :param excepted: 期望值
        :return:
        """
        self.case_name = case_name
        self.username = username
        self.password = password
        self.city = city
        self.excepted = excepted

    #登录融管系统
    def user_login_verify(self,username="",password="",city=""):
        login(self.driver).user_login(username,password,city)

    def test_login(self):
        # self._testMethodDoc = self.case_name  # 设置用例名称
        self.user_login_verify(self.username,self.password,self.city)
        po = login(self.driver)
        if self.case_name == '用户名，密码，城市都正确':
            self.assertEqual(po.user_login_success(),self.excepted)
            current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))
            functions.insert_img(self.driver, "user_login_success_"+current_time+".png")
        else:
            self.assertEqual(po.username_error_hint(),self.excepted)
            current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))
            functions.insert_img(self.driver,"user_login_failed_"+current_time+".png")