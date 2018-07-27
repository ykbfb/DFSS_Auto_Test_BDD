#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2017年4月26日

@author: kun
'''
#--==================================================================
#By 函数的属性：
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
#--==================================================================

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
import time

class login(Page):
    
    url = '/'
    
    dfss_login_user_loc = (By.XPATH,'//*[@id="main"]/div[2]/div/div')
    dfss_login_button_loc = (By.XPATH,'//*[@id="main"]/div[2]/div/div/div/div[6]/input')
    
    def dfss_login(self):
        self.find_element(*self.dfss_login_user_loc).click()
        self.setWaitTime(5)
        self.find_element(*self.dfss_login_button_loc).click()
    
    lodin_username_loc = (By.ID,"UserName")
    login_password_loc = (By.ID,"Password")
    login_city_loc = (By.ID,"City")
    login_button_loc = (By.XPATH,'//*[@id="main"]/div[2]/div/div/div/div[6]/input')

    
    #登录用户名
    def login_username(self,username):
        self.find_element(*self.lodin_username_loc).send_keys(username)
    
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    
    #登录城市   
    def login_city(self,city):
        self.find_element(*self.login_city_loc).send_keys(city)
        
    #登录按钮   
    def login_button(self): 
        self.find_element(*self.login_button_loc).click()
    
    #定义统一登录入口
    def user_login(self,username = "liuchao",password = '123456',city = 'suzhou'):
        self.open()
        self.dfss_login()
        self.login_username(username)
        self.login_password(password)
        self.login_city(city)
        self.login_button()
        self.setWaitTime(5)

    #=================================================
    def user_login_verify(self,username="",password="",city=""):
        login(self.driver).user_login(username,password,city)
        time.sleep(2)
    #=================================================

    username_empty_hint_loc = (By.XPATH,'//*[@id="main"]/div[2]/div/div/div/div[1]/div/span')
    password_empty_hint_loc = (By.XPATH,'//*[@id="main"]/div[2]/div/div/div/div[2]/div/span')
     
    username_error_hint_loc = (By.XPATH,'//*[@id="main"]/div[1]/form/div/ul/li')
    password_error_hint_loc = (By.XPATH,'//*[@id="main"]/div[1]/form/div/ul/li')
    city_error_hint_loc = (By.XPATH,'//*[@id="main"]/div[1]/form/div/ul/li')
    user_login_success_loc = (By.XPATH,'//*[@id="Main_Page"]/div[1]/div/div/span[3]/label')

    #用户名为空
    def username_empty_hint(self): 
        return self.find_element(*self.username_empty_hint_loc).text
    
    #密码为空
    def  password_empty_hint(self):
        return self.find_element(*self.password_empty_hint_loc).text
      
    #用户名错误
    def username_error_hint(self):
        return self.find_element(*self.username_error_hint_loc).text
    
    #密码错误
    def  passwword_error_hint(self):
        return self.find_element(*self.password_error_hint_loc).text
    
    #城市错误
    def city_error_hint(self):
        return self.find_element(*self.city_error_hint_loc).text
    
    #登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
        
        
   