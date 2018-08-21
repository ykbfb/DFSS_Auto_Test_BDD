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
from test_case.models import settings
import time

class LoanRefundPage(Page):

#=========================================================================================================================
# 放款红冲：  质检（提交申请）→债权中心总经理→分公司财务→数据部→发喜报
#=========================================================================================================================
    quality_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[1]/div[1]')#质检系统
    loan_redrefund_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[2]/ul/li[3]/div/a/span[2]')#放款红冲
    loan_redlist_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    all_channalresult_loc = (By.XPATH,'//*[@id="ulType"]/li[1]')#所有放款喜报
    city_loc = (By.XPATH,'//*[@id="divHtml_AllHappy"]/a[1]')#城市 '
    suborder_no_loc = (By.ID,'txt_SubOrderId')#子订单
    search_btn_loc = (By.XPATH,'//*[@id="main"]/table[1]/tbody/tr[10]/td/div[2]')#查询

    #打开待红冲的融资喜报
    def getChannResult(self,suborder_no):
        self.suborder_no = suborder_no
        self.click_element(*self.quality_menu_loc)
        self.click_element(*self.loan_redrefund_menu_loc)
        self.setWaitTime(20)
        self.switchToOneFrameByXpath(self.loan_redlist_frame_loc)
        self.click_element(*self.all_channalresult_loc)
        time.sleep(1)
        self.click_element(*self.city_loc)
        time.sleep(1)
        self.input_value(self.suborder_no_loc,suborder_no)
        self.click_element(*self.search_btn_loc)
        time.sleep(1)


    red_refund_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[22]/input[4]')#红冲
    red_refund_detail_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    lendtotal_amt_loc = (By.ID,'LendingTotal')#放款额度
    lend_time_loc = 'txtLendDateTime'#放款时间
    info_confirm_attach_loc = (By.XPATH,'//*[@id="pickerInfoServiceFile"]/div[2]/input')#信息确认书
    info_confirm_upload_loc = (By.ID,'btnUpload_pickerInfoServiceFile')#上传
    red_refund_memo_loc = (By.ID,'Memo')#备注
    red_refund_submit_loc = (By.XPATH,'//*[@id="main"]/div[1]/div/table/tbody/tr[2]/td[1]/input')#提交审核

    #输入放款红冲详情
    def inputRedRefundDetail(self):
        self.scrollToElement_new(*self.red_refund_loc)
        self.click_element(*self.red_refund_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.red_refund_detail_frame_loc)
        self.input_value(self.lendtotal_amt_loc,100)
        self.getDateTimePicker(self.lend_time_loc,time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))
        self.uploadFile2(self.info_confirm_attach_loc,settings.Other_file)
        time.sleep(1)
        self.click_element(*self.info_confirm_upload_loc)
        time.sleep(3)
        self.scrollToElement_new(*self.red_refund_memo_loc)
        self.input_value(self.red_refund_memo_loc,'自动化测试：放款红冲')
        self.click_element(*self.red_refund_submit_loc)
        time.sleep(1)
        self.close_alert()

    #创建放款红冲
    def createLoanRedRefund(self,suborder_no):
        self.suborder_no = suborder_no
        self.getChannResult(suborder_no)
        self.inputRedRefundDetail()

#===================================================================================================================================
#  审批放款红冲--债权中心总经理
#===================================================================================================================================
    appv_redrefund_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[1]/div[2]/ul/li[2]/div/a/span[2]')#放款红冲审批
    appv_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    appv_city_loc = (By.XPATH,'//*[@id="divHtml"]/a[1]')#城市
    appv_search_btn_loc = (By.ID,'Button4')#查询

    #查询待审批的放款红冲喜报
    def getNeedAppvRedRefund(self,suborder_no):
        self.suborder_no = suborder_no
        self.click_element(*self.appv_redrefund_menu_loc)
        self.switchToOneFrameByXpath(self.appv_list_frame_loc)
        self.click_element(*self.appv_city_loc)
        self.input_value(self.suborder_no_loc,suborder_no)
        self.click_element(*self.appv_search_btn_loc)
        time.sleep(1)

    order_detail_loc = (By.XPATH,'//*[@id="contenthtml"]/table/tbody/tr[2]/td[1]/input[1]')#订单详情
    redrefund_appv_detail_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    redrefund_appv_memo_loc = (By.ID,'qudaoshenpiyijian')
    redrefund_appv_pass_loc = (By.XPATH,'//*[@id="channelGMapproval"]/td/div/input[1]')

    #输入审批详情
    def inputRedRefundAppvDetail(self):
        self.click_element(*self.order_detail_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.redrefund_appv_detail_frame_loc)
        self.scrollToElement_new(*self.redrefund_appv_memo_loc)
        self.input_value(self.redrefund_appv_memo_loc,'自动化测试：放款红冲审批')
        self.click_element(*self.redrefund_appv_pass_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.close_alert()

    #审批放款红冲--债权中心总经理
    def approveRedRefund(self,suborder_no):
        self.suborder_no = suborder_no
        self.getNeedAppvRedRefund(suborder_no)
        self.inputRedRefundAppvDetail()

#============================================================================================================================
#   放款红冲审批--数据专员
#============================================================================================================================
    dt_chanlresult_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[1]/div[2]/ul/li[9]/div/a/span[2]') #融资喜报审批
    dt_chanl_resultlistframe_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    dt_chanl_city_loc = 'citys_c'#城市
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

    dt_detail_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    dt_message_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_msg_send_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[4]/td[2]/input[1]') #发送
    dt_send_success_loc = (By.CLASS_NAME,'layui-layer-btn0')#发送成功

    def approveRedLoanRedRefund_DataManager(self, value):
        self.value = value
        self.click_element(*self.dt_chanlresult_menu_loc)
        self.setWaitTime(20)
        self.switchToOneFrameByXpath(self.dt_chanl_resultlistframe_loc)
        self.getDropdownMenuById(self.dt_chanl_city_loc, 0)
        self.input_value(self.suborder_no_loc,value)
        self.click_element(*self.dt_search_loc)

        time.sleep(1)
        self.click_element(*self.dt_order_detail_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_order_detal_frame_loc)
        self.scrollToElement('id',self.dt_move_apprv_memo_loc)
        self.input_value(self.dt_apprv_memo_loc,'自动化测试：返佣红冲审批--数据部')
        self.click_element(*self.dt_apprv_pass_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(2)

        #喜报详情页
        self.switchToParentFrame()
        self.switchWindow()
        time.sleep(1)
        self.switchToOneFrameByXpath(self.dt_chanl_resultdetail_frame_loc) #此处有问题：一个弹窗关闭，又出来一个弹窗，定位不到当前窗口
        self.scrollToElement('id',self.dt_move_save_close_loc)
        self.click_element(*self.dt_save_close_loc)
        time.sleep(1)

        #确认窗口
        self.switchWindow()
        self.click_element(*self.dt_confirm_loc)
        time.sleep(1)

        #QQ广播页面
        self.switchToOneFrameByXpath(self.dt_detail_frame_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_message_frame_loc)
        self.click_element(*self.dt_msg_send_loc)
        time.sleep(1)

        #发送成功确认
        self.switchWindow()
        self.click_element(*self.dt_send_success_loc)


