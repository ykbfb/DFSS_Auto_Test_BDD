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

class RebatePage(Page):
#=========================================================================================================================
#返佣红冲(>-500): 融服经理 → 融服总监 → 分公司财务 → 数据部
#返佣红冲(<-500): 融服经理 → 融服总监 → 各条线事业部总经理 → 分公司财务 → 数据部
#=========================================================================================================================
    order_mng_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#融资订单管理
    rebate_mng_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[2]/div/a/span[2]')#喜报管理
    chann_result_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    chann_success_loc = (By.XPATH,'//*[@id="ulType"]/li[3]')#已成功
    sub_order_loc = (By.ID,'txt_SubOrderId')#子订单号
    search_btn_loc = (By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div')#查询


    #查询已成功的融资喜报
    def getSuccessChannlResult(self,suborder_no):
        self.suborder_no = suborder_no
        self.click_element(*self.order_mng_loc)
        self.click_element(*self.rebate_mng_loc)
        self.setWaitTime(10)
        self.switchToOneFrameByXpath(self.chann_result_list_frame_loc)
        time.sleep(1)
        self.click_element(*self.chann_success_loc)
        self.input_value(self.sub_order_loc,suborder_no)
        self.click_element(*self.search_btn_loc)
        time.sleep(2)

    #填写红冲详情
    red_refund_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[21]/input[4]')#红冲
    rebate_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    loan_time_loc = 'txtLendDateTime'#放款时间
    confirm_rbate_loc = (By.ID,'txt_SubmitFanyong')#核实返佣
    red_refund_memo_loc = (By.ID,'Memo')#备注
    rebate_attch_loc = (By.ID,'FanyongUploadInput')#附件
    upload_sucess_loc = (By.CLASS_NAME,'layui-layer-btn0')#上传成功
    submit_btn_loc = (By.XPATH,'//*[@id="main"]/div[1]/div/table/tbody/tr[2]/td[1]/input')#提交审核

    def inputRedRebateRefundDetail(self):
        self.click_element(*self.red_refund_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.rebate_frame_loc)
        self.getDateTimePicker(self.loan_time_loc,time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time())))
        self.input_value(self.confirm_rbate_loc,100)
        self.input_value(self.red_refund_memo_loc,'自动化测试：返佣红冲')
        self.scrollToElement_new(*self.submit_btn_loc)
        self.uploadFile2(self.rebate_attch_loc,settings.Other_file)
        time.sleep(2)
        self.switchWindow()
        self.click_element(*self.upload_sucess_loc)
        time.sleep(1)
        self.click_element(*self.submit_btn_loc)
        time.sleep(1)
        self.close_alert()

    #创建返佣红冲
    def createRedRebateRefund_Sales(self,suborder_no):
        self.suborder_no = suborder_no
        self.getSuccessChannlResult(suborder_no)
        self.inputRedRebateRefundDetail()

 #================================================================================================================================
 #  融服总监审批返佣红冲
 #================================================================================================================================
    service_mng_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#融资管理
    rebate_refund_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[10]/div/a/span[2]')#返佣喜报审批
    rebate_appvlist_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    dir_suborder_no_loc = (By.ID,'txt_SubOrderId')#子订单号
    dir_search_loc = (By.ID,'btncheck')#查询

    #获取待审批的返佣喜报
    def getNeedAppvRebate(self,suborder_no):
        self.suborder_no = suborder_no
        self.click_element(*self.service_mng_menu_loc)
        self.scrollToElement_new(*self.rebate_refund_menu_loc)
        self.click_element(*self.rebate_refund_menu_loc)
        self.switchToOneFrameByXpath(self.rebate_appvlist_frame_loc)
        self.input_value(self.sub_order_loc,suborder_no)
        self.click_element(*self.dir_search_loc)

    #输入审批详情
    rebate_appv_btn_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[16]/input')#审批
    appv_detail_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    appv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/div/table/tbody/tr/td[1]/input')#通过

    def inputRebateApproveDetail(self):
        self.click_element(*self.rebate_appv_btn_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.appv_detail_frame_loc)
        self.click_element(*self.appv_pass_loc)
        time.sleep(1)
        self.close_alert()

    #融资总监-审批返佣红冲
    def approveRebateRedRefund_Director(self,suborder_no):
        self.suborder_no = suborder_no
        self.getNeedAppvRebate(suborder_no)
        self.inputRebateApproveDetail()

#============================================================================================================================
#   返佣红冲审批--数据专员
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

    def approveRebateRedRefund_DataManager(self, value):
        self.value = value
        self.click_element(*self.dt_chanlresult_menu_loc)
        self.setWaitTime(20)
        self.switchToOneFrameByXpath(self.dt_chanl_resultlistframe_loc)
        self.getDropdownMenuById(self.dt_chanl_city_loc, 0)
        self.input_value(self.sub_order_loc,value)
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
        self.switchToOneFrameByXpath(self.dt_detail_frame_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_message_frame_loc)
        self.click_element(*self.dt_msg_send_loc)
        time.sleep(1)

        #发送成功确认
        self.switchWindow()
        self.click_element(*self.dt_send_success_loc)








