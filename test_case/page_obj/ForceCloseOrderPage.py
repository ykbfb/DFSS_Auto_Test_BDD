# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

# --==================================================================
# By 函数的属性：
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
#---------------------------------------------------------------------
#定位动态id、name元素
# driver.find_element_by_xpath("//iframe[contains(@id, 'layui-layer-iframe')]")
# driver.find_element_by_xpath("//div[starts-with(@id, 'btn-attention')]")
# driver.find_element_by_xpath("//div[ends-with(@id, 'btn-attention')]")
# --==================================================================

from selenium.webdriver.common.by import By
from .base import Page
import time

class ForceCloseOrderPage(Page):
    #订单强制结案
    other_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]') #其他
    force_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[1]/div/a/span[2]')#强制结案
    f_orderlist_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    city_loc = 'sel_City'#城市
    client_name_loc = (By.ID,'CusName')#客户名称
    order_search_loc = (By.ID,'btn_Search')#查询
    close_order_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[10]/input')#结案


    #强制结案
    def forceCloseOrder(self,client_name):
        self.client_name = client_name
        self.click_element(*self.other_nav_loc)
        self.click_element(*self.force_menu_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.f_orderlist_frame_loc)
        self.getDropdownMenuById(self.city_loc,1)
        self.input_value(self.client_name_loc,client_name)
        self.click_element(*self.order_search_loc)
        self.click_element(*self.close_order_loc)
        self.inputOrderCloseDetail()

    #结案报告页面
    pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    close_type1_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input')#退费结案
    close_type2_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input')#满意结案
    close_type3_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[6]/td[2]/label[3]/input')#异常结案
    memo1_loc = (By.XPATH,'//*[@id="tdFinishWords"]/div[1]/textarea') #结案总结
    memo2_loc = (By.XPATH,'//*[@id="tdFinishWords"]/div[2]/textarea')
    memo3_loc = (By.XPATH,'//*[@id="tdFinishWords"]/div[3]/textarea')
    force_close_loc = (By.ID,'tdForceToCloseOrder')#提交
    move_to_closebtn_loc = 'tdForceToCloseOrder'

    def inputOrderCloseDetail(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_frame_loc)
        self.scrollToElement('id',self.move_to_closebtn_loc)
        self.click_element(*self.close_type1_loc)
        self.input_value(self.memo1_loc,'自动化测试：1. 融资中心总经理强制结案！！！')
        self.input_value(self.memo2_loc,'自动化测试：2. 融资中心总经理强制结案！！！')
        self.input_value(self.memo3_loc,'自动化测试：3. 融资中心总经理强制结案！！！')
        self.click_element(*self.force_close_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.close_alert()


