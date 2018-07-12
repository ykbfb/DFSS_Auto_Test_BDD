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

class SalesResultApprovalPage(Page):
    #流程管理
    process_manage_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]') #流程管理
    order_manage_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[8]/div/a/span[2]')#订单管理
    sal_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    clt_name_loc = (By.ID,'txtCmpName')#客户姓名
    submit_start_time_loc = 'txtSubmitStart'#提交日期
    search_loc = (By.ID,'btnCheck')#查询
    order_tetail_local = (By.XPATH,'//*[@id="table"]/tbody/tr[2]//td[2]/a')#详情

    def createSalesResult_Sales(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.process_manage_nav_loc)
        self.click_element(*self.order_manage_nav_loc)
        self.setWaitTime(10)
        self.switchToOneFrameByXpath(self.sal_list_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.getDateTimePicker(self.submit_start_time_loc,'')
        self.click_element(*self.search_loc)
        time.sleep(1)
        self.click_element(*self.order_tetail_local)
        self.inputSalesResultDetail_Sales()

    sal_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    moveto_create_loc = 'SeeOrderDetails'
    create_loc = (By.CLASS_NAME,'SeeOrderDetails')#新增
    input_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    act_recive_loc = (By.ID,'txtCurrentCollection')#实际收款
    memo_loc = (By.ID,'txtMemo')#备注
    submit_loc = (By.ID,'tr1')#提交
    confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')

    def inputSalesResultDetail_Sales(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.sal_pop_frame_loc)
        self.scrollToElement('class_name',self.moveto_create_loc)
        self.click_element(*self.create_loc)
        time.sleep(1)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.input_pop_frame_loc)
        self.input_value(self.act_recive_loc,100)
        self.input_value(self.memo_loc,'自动化测试：顾问提交销售喜报')
        self.click_element(*self.submit_loc)










