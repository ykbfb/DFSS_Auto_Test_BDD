#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8
'''
Created on 2018-01-10

@author: kun yang
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from .driver import broswer
import unittest
import os


class MyTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.driver = broswer()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()  # 删除所有cookie

    def tearDown(self):
        self.driver.quit()

    def clearCache(self):
        #清除浏览器缓存 Ctrl + F5
        ActionChains(self.driver).key_down(Keys.CONTROL).key_down(Keys.F5).send_keys(Keys.UP).perform()




    
