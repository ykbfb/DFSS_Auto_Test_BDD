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
# --==================================================================

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
import time



class SalesBargainPage(Page):
    workflow_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#流程管理
    moveto_newSalesOrderMng_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[16]/div/a/span[2]'
    newSalesOrderMng_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[16]/div/a/span[2]')#新销售订单管理
    salesOrderList_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    client_search_loc = (By.ID,'txtCmpName')#客户查询
    can_fill_sales_loc = (By.ID,'cbXibao')#可填喜报
    search_btn_loc = (By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[1]')#查询
    order_detail_loc = (By.XPATH,'//*[@id="164"]/td[2]/a/img')#详情


    def CreateSalesBargainResult(self,cmp_name):
        '''创建销售喜报'''
        self.cmp_name = cmp_name
        self.click_element(*self.workflow_manage_loc)
        self.scrollToElement('xpath',self.moveto_newSalesOrderMng_loc)
        self.click_element(*self.newSalesOrderMng_loc)
        self.setWaitTime(10)
        self.switchToOneFrameByXpath(self.salesOrderList_frame_loc)
        self.input_value(self.client_search_loc,cmp_name)
        self.click_element(*self.can_fill_sales_loc)
        self.click_element(*self.search_btn_loc)
        self.click_element(*self.order_detail_loc)
        self.switchToParentFrame()
        self.inputSalesBarginDetail()

    #==============================================================================================
    pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"#订单详情页主frame
    detail_frame_loc = 'iframe2'
    moveto_create_btn_loc = '//*[@id="OrderInfo"]/table/tbody/tr[7]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/div[2]/input'
    create_btn_loc = (By.XPATH,'//*[@id="OrderInfo"]/table/tbody/tr[7]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/div[2]/input')#新增
    input_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    act_recive_amt_loc = (By.ID,'txtCurrentCollection')#实际收款
    memo_loc = (By.ID,'txtMemo')#备注
    submit_loc = (By.ID,'tr1')#提交审核

    def inputSalesBarginDetail(self):
        '''弹出窗，填写喜报详情'''
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_frame_loc)
        self.switchToOneFrame(self.detail_frame_loc)
        self.scrollToElement('xpath',self.moveto_create_btn_loc)
        self.click_element(*self.create_btn_loc)
        self.switchToParentFrame()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.input_frame_loc)
        self.input_value(self.act_recive_amt_loc,100)
        self.input_value(self.memo_loc,'自动化测试：创建销售喜报')
        self.click_element(*self.submit_loc)


    # --===========================================================================================
    # 验证case的执行结果

