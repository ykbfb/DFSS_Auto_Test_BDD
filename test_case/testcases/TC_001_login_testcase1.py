#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018年1月04日

@author: kun yang
'''

import unittest,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from test_case.models import myunit,functions
from test_case.page_obj.loginPage import login
import time
# from data.ReadTestData import TestData

class loginTest(myunit.MyTest):
    global current_time 
    current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    #登录融管系统
    def user_login_verify(self,username="",password="",city=""):
        login(self.driver).user_login(username,password,city)
    
    def test_0001_login(self):
        '''用户名错误，密码和城市为空'''
        self.user_login_verify()
        po = login(self.driver)
        if po.username_empty_hint() == '用户名 字段是必需的。' and po.password_empty_hint() == '密码 字段是必需的。':
            self.assertEqual(po.username_empty_hint(),"用户名 字段是必需的。")  #
            self.assertEqual(po.password_empty_hint(),"密码 字段是必需的。")
            print("case1: pass")
        elif  po.username_empty_hint() == 'The 用户名 field is required.' and po.password_empty_hint() == 'The 密码 field is required':
            self.assertEqual(po.username_empty_hint(),"The 用户名 field is required.")  #
            self.assertEqual(po.password_empty_hint(),"The 密码 field is required")
            print("case11: pass")
        else:
            print("case1: failed")
        functions.insert_img(self.driver,current_time+"__user_pwd_ept.png")
        po.setWaitTime(5)
        print("case1: pass")
        po.close()
    
    def test_0002_login2(self):
        '''用户名错误，密码和城市正确'''
        self.user_login_verify(username = 'hello',password = '123456',city = 'suzhou')
        po = login(self.driver)
        self.assertEqual(po.username_error_hint(),"您的登录信息有误，请检查用户名和相关城市！")
        functions.insert_img(self.driver,current_time+"__user_username_error.png")
        po.setWaitTime(5)
        print("case2: pass")
        po.close()

        
    def test_0003_login3(self):
        '''用户名正确，密码错误'''
        self.user_login_verify(username = 'qiushun',password = 'wqwq',city = 'suzhou')
        po = login(self.driver)
        self.assertEqual(po.passwword_error_hint(),"提供的用户名或密码不正确。")
        functions.insert_img(self.driver,current_time+"__user_pwd_error.png")
        po.setWaitTime(5)
        print("case3: pass")
        po.close()
                        
    def test_0004_login4(self):
        '''用户名、密码正确，城市错误'''
        self.user_login_verify(username = 'qiushun',password = '123456',city = 'shanghai')
        po = login(self.driver)
        self.assertEqual(po.city_error_hint(),"您的登录信息有误，请检查用户名和相关城市！")
        functions.insert_img(self.driver,current_time+"__user_city_error.png")
        po.setWaitTime(5)
        print("case4: pass")
        po.close()

        
    def test_0005_login5(self):
        '''成功登陆'''
        self.user_login_verify(username = 'qiushun',password = '123456',city = 'suzhou')
        po = login(self.driver)
        self.assertEqual(po.user_login_success(),"Hello,邱顺 [AA1128]")
        functions.insert_img(self.driver,current_time+"__user_login_success.png")
        po.setWaitTime(5)
        print("case5: pass")
        po.close()

if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        

