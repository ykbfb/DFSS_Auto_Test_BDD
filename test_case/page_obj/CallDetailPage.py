#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2017年5月12日

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
from .loginPage import login
import time


class CallDetailPage(Page):

    #呼叫详情页
    callDetail_frame_loc = '//*[@id="HomePage_ReMake_TPCltCall_Id"]'
    call_memo_loc = (By.ID,'txtCallMemo')
    call_detl_save_loc = (By.ID,'btnImgSave')
    close_win_loc = (By.XPATH,'//*[@id="tabs"]/div[1]/div[3]/ul/li[3]/a[2]')

    def fillCalldetail(self):
        '''填写呼叫详情'''
        self.switchToCurrentWindow()
        self.switchToOneFrameByXpath(self.callDetail_frame_loc)
        self.input_value(self.call_memo_loc,'自动化测试：呼叫备注详情')
        self.click_element(*self.call_detl_save_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.switchToParentFrame()
        self.click_element(*self.close_win_loc)

#=============================================================================================
# 拨打客户
#=============================================================================================
    clientCheckBox_loc = '//*[@id="datagrid-row-r3-2-0"]/td[1]'  # 客户列表中的checkbox
    def callClient(self):
        '''呼叫客户'''
        self.doubleClick('xpath',self.clientCheckBox_loc)
        self.setWaitTime(10)
        self.fillCalldetail()

    rigth_call_loc = (By.ID,'contextMenuId_wh')#列表右键【外呼】按钮
    def rigthClickCall(self):
        '''列表页右键外呼'''
        self.rightClick(self.clientCheckBox_loc)
        self.click_element(*self.rigth_call_loc)
        time.sleep(1)
        self.fillCalldetail()

    call_btn_loc = (By.XPATH,'//*[@id="datagrid-row-r3-2-0"]/td[5]')#列表呼叫按钮
    def callFromList(self):
        '''列表页呼叫'''
        self.click_element(*self.call_btn_loc)
        time.sleep(1)
        self.fillCalldetail()

    multiple_call_loc = (By.ID,'operateItems_plwh') #批量呼叫按钮
    def multCall(self):
        '''批量呼叫'''
        self.click_element(*self.multiple_call_loc)
        time.sleep(1)
        self.fillCalldetail()

#==========================================================================================
#打开呼叫页面公共方法
#==========================================================================================
    def openCallDetailPage(self):
        self.doubleClick('xpath',self.clientCheckBox_loc)
        time.sleep(2)
        self.switchToCurrentWindow()
        time.sleep(1)
        self.switchToOneFrameByXpath(self.callDetail_frame_loc)
