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

class ShareClientPage(Page):
    clientCheckBox_loc = '//*[@id="datagrid-row-r3-2-0"]/td[1]'  # 客户列表中的checkbox
    right_share_loc = (By.ID,'contextMenuId_gx')#右键【共享】按钮

    pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    share_reason_loc = (By.ID,'txtShareReason')
    confirm_loc = "btnSubmit"
    confirm_btn_loc = (By.ID,'btnSubmit')

    def inputShareDetail(self):
        '''填写共享页详情'''
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_frame_loc)
        self.scrollToElement('id', self.confirm_loc)
        self.input_value(self.share_reason_loc, '自动化测试：客户释放公海')
        self.click_element(*self.confirm_btn_loc)

    def shareClientByRigthClick(self):
        '''列表页右键共享'''
        self.rightClick(self.clientCheckBox_loc)
        self.click_element(*self.right_share_loc)
        self.setWaitTime(10)
        self.inputShareDetail()

    list_share_loc = (By.ID,'operateItems_gx')#右上角【共享】按钮
    def shareClientFromList(self):
        '''列表页右上角共享'''
        self.click_element(*self.list_share_loc)
        self.inputShareDetail()


    call_share_loc = (By.ID,'btnShare')#呼叫页【共享】按钮
    moveto_client_type_loc = 'r1'
    client_type_loc = (By.ID,'r1')
    def shareClientFromCallPage(self):
        '''呼叫详情页释放客户'''
        self.scrollToElement('id',self.moveto_client_type_loc)
        self.click_element(*self.client_type_loc)
        self.click_element(*self.call_share_loc)
        time.sleep(1)
        self.close_alert()
        self.inputShareDetail()





    

        
   