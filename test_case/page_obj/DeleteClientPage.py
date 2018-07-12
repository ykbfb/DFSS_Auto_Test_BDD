#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2017年4月26日

@author: Administrator
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

class DeleteClientPage(Page):
    clientCheckBox_loc = '//*[@id="datagrid-row-r3-2-0"]/td[1]'  # 客户列表中的checkbox
    right_delete_loc = (By.ID,'contextMenuId_sc')#右键【删除】按钮
    confirm_del_loc = (By.CLASS_NAME,'layui-layer-btn0')


    def deleteClientAction(self):
        '''填写共享页详情'''
        self.switchWindow()
        self.click_element(*self.confirm_del_loc)

    def deleteClientByRigthClick(self):
        '''列表页右键删除'''
        self.rightClick(self.clientCheckBox_loc)
        self.click_element(*self.right_delete_loc)
        self.setWaitTime(10)
        self.deleteClientAction()

    list_del_loc = (By.ID,'operateItems_sc')#右上角【删除】按钮
    def deleteClientFromList(self):
        '''列表页右上角删除'''
        self.click_element(*self.list_del_loc)
        self.deleteClientAction()





    

        
   