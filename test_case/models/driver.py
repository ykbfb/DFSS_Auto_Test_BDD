#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8
'''
Created on 2017-09-05

@author: Kun Yang
'''

#from selenium.webdriver import Remote
from selenium import webdriver

def broswer():
    driver = webdriver.Chrome()
#     host = '10.40.3.230:10003'
#     dc = {'broswername':'chrome'}
#     driver = Remote(command_executor='http://' + host + '/Account/Logon',desired_capabilities = dc)    
    return driver
    
if __name__ == '__main__':
    dr = broswer()
    dr.get("https://www.baidu.com")
