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

class ChannalResultApprovalPage(Page):
    #融资订单管理
    loanmanage_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]') #融资管理
    channalresult_appr_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[6]/div/a/span[2]')#融资喜报审批
    chan_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    channalresult_cmpname_loc = (By.ID,'querycode')#按客户名称、联系人姓名
    chan_search_loc = (By.ID,'Button4')

    order_detail_loc = (By.XPATH,'//*[@id="contenthtml"]/table/tbody/tr[2]/td[1]/input[1]') #订单详情
    order_detal_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    chanl_apprv_memo_loc = (By.ID,"qudaoshenpiyijian")#审批已经
    moveto_chanl_apprv_memo_loc = "qudaoshenpiyijian"
    approve_pass_loc = (By.XPATH,'//*[@id="channelGMapproval"]/td/div/input[1]') #通过

    #放款喜报（总监）-待审批
    def approveChannalResult_Director(self,value):
        self.value = value
        self.click_element(*self.loanmanage_nav_loc)
        self.waitElmentUntill(10,self.channalresult_appr_loc)
        self.click_element(*self.channalresult_appr_loc)
        self.switchToOneFrameByXpath(self.chan_frame_loc)
        self.waitElmentUntill(20,self.channalresult_cmpname_loc)
        self.input_value(self.channalresult_cmpname_loc,value)
        self.click_element(*self.chan_search_loc)
        # time.sleep(10)
        self.waitElmentUntill(20,self.order_detail_loc)
        self.click_element(*self.order_detail_loc)
        self.switchToOneFrameByXpath(self.order_detal_frame_loc)
        self.scrollToElement('id',self.moveto_chanl_apprv_memo_loc)
        self.input_value(self.chanl_apprv_memo_loc,'自动化测试:融资喜报审批--融资总监')
        self.click_element(*self.approve_pass_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.close_alert()

    #放款喜报审批--分公司财务
    finance_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#财务
    fin_chanlresult_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[3]/div/a/span[2]')#融资喜报审批
    fin_chanl_resultlistframe_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    fin_clt_name_loc = (By.ID,'querycode')#客户名称
    fin_search_btn_loc = (By.ID,'Button4')#查询

    fin_order_result_loc = (By.XPATH,'//*[@id="contenthtml"]/table/tbody/tr[2]/td[1]/input[1]')#订单详情
    fin_order_detal_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    fin_apprv_memo_loc = (By.ID,'qudaoshenpiyijian')#审批意见
    fin_move_apprv_memo_loc = 'qudaoshenpiyijian'
    fin_apprv_pass_loc = (By.XPATH,'//*[@id="channelfinanceapproval"]/td/div/input[1]')#通过

    def approveChannalResult_Finance(self, value):
        self.value = value
        self.click_element(*self.finance_menu_loc)
        self.click_element(*self.fin_chanlresult_menu_loc)
        self.setWaitTime(10)
        self.switchToOneFrameByXpath(self.fin_chanl_resultlistframe_loc)
        self.input_value(self.fin_clt_name_loc,value)
        self.click_element(*self.fin_search_btn_loc)

        time.sleep(1)
        self.click_element(*self.fin_order_result_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.fin_order_detal_frame_loc)
        self.scrollToElement('id',self.fin_move_apprv_memo_loc)
        self.input_value(self.fin_apprv_memo_loc,'自动化测试：融资喜报审批--分公司财务')
        self.click_element(*self.fin_apprv_pass_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.close_alert()

    #放款喜报审批-数据专员
    dt_chanlresult_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[1]/div[2]/ul/li[9]/div/a/span[2]') #融资喜报审批
    dt_chanl_resultlistframe_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    dt_chanl_city_loc = 'citys_c'#城市
    dt_clt_name_loc = (By.ID,'querycode')#客户名称
    dt_search_loc = (By.ID,'Button4') #查询

    dt_order_detail_loc = (By.XPATH,'//*[@id="htmlcontent"]/table/tbody/tr[2]/td[2]/input[1]') #订单详情
    dt_order_detal_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_apprv_memo_loc = (By.ID,'qudaoshenpiyijian')#审批意见
    dt_move_apprv_memo_loc = 'qudaoshenpiyijian'
    dt_apprv_pass_loc = (By.XPATH,'//*[@id="channeldatalastcheck"]/td/div/input[1]')#通过

    dt_chanl_resultdetail_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_save_close_loc = (By.ID,'btnSaveClose')#保存关闭并发送
    dt_move_save_close_loc = 'btnSaveClose'

    dt_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确定

    dt_message_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_msg_send_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[4]/td[2]/input[1]') #发送
    dt_send_success_loc = (By.CLASS_NAME,'layui-layer-btn0')#发送成功

    def approveChannalResult_DataManager(self, value):
        self.value = value
        self.click_element(*self.dt_chanlresult_menu_loc)
        self.setWaitTime(20)
        self.switchToOneFrameByXpath(self.dt_chanl_resultlistframe_loc)
        self.getDropdownMenuById(self.dt_chanl_city_loc, 0)
        self.input_value(self.dt_clt_name_loc,value)
        self.click_element(*self.dt_search_loc)

        time.sleep(1)
        self.click_element(*self.dt_order_detail_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_order_detal_frame_loc)
        self.scrollToElement('id',self.dt_move_apprv_memo_loc)
        self.input_value(self.dt_apprv_memo_loc,'自动化测试：融资喜报审批--数据部')
        self.click_element(*self.dt_apprv_pass_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(3)

        #喜报详情页
        self.switchToParentFrame()
        self.switchWindow()
        time.sleep(2)
        self.switchToOneFrameByXpath(self.dt_chanl_resultdetail_frame_loc) #此处有问题：一个弹窗关闭，又出来一个弹窗，定位不到当前窗口
        self.scrollToElement('id',self.dt_move_save_close_loc)
        self.click_element(*self.dt_save_close_loc)
        time.sleep(1)

        #确认窗口
        self.switchWindow()
        self.click_element(*self.dt_confirm_loc)
        time.sleep(1)

        #QQ广播页面
        #self.switchToParentFrame()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_message_frame_loc)
        self.click_element(*self.dt_msg_send_loc)
        time.sleep(1)

        #发送成功确认
        self.switchWindow()
        self.click_element(*self.dt_send_success_loc)






