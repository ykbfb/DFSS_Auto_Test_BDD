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
#    pop_new_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
import time

class AimRefundTransPage(Page):
    # 合同管理
    contract_tab_loc = (By.XPATH,'//*[@id="bottomTabs_htgl"]/a')
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    def clickContractTab(self):
        self.click_element(*self.contract_tab_loc)
        self.scrollToElement('id',self.botom_frame_loc) # 页面跳转到底部【客户详情】所在的位置--相当于滚动条
        self.switchToOneFrame(self.botom_frame_loc) # 切换到底部【客户详情】的iframe

#=======================================================================================================================
#                   意向金专业绩                                                                                      ==
#        融资顾问→销售经理→总监→分总→出纳→数据专员                                                               ==
#=======================================================================================================================
    # 意向金转业绩
    aim_trans_loc = (By.PARTIAL_LINK_TEXT,"转业绩") #【转业绩】按钮
    pop_new_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    def openAimTransPage(self):
        self.click_element(*self.aim_trans_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.switchToOneFrameByXpath(self.pop_new_frame_loc)

    # 填写会员费退费
    aim_amt_rest_loc = (By.ID,'AmountRest')#意向金余额
    aim_trans_amt_loc = (By.ID,'Amount')#意向金转业绩金额
    moveto_aim_trans_amt_loc = 'Amount'
    market_perform_amt_loc = (By.ID,'txtOpRes')#市场业绩
    aim_trans_reason_loc = (By.ID,'txtReason')#意向金转业绩原因
    submit_btn_loc = (By.XPATH,'//*[@id="divShow"]/table/tbody/tr[12]/td[2]/input[1]')#提交

    def inputAimTransDetail(self):
        aim_rest_amt = self.find_element(*self.aim_amt_rest_loc).text
        self.scrollToElement('id',self.moveto_aim_trans_amt_loc)
        self.input_value(self.aim_trans_amt_loc,aim_rest_amt)
        self.input_value(self.market_perform_amt_loc,100)
        self.input_value(self.aim_trans_reason_loc,'自动化测试：意向金转业绩')
        self.click_element(*self.submit_btn_loc)
        time.sleep(1)
        self.close_alert()

    #顾问意向金转业绩
    def createAimTransfer(self):
        self.clickContractTab()
        self.openAimTransPage()
        self.inputAimTransDetail()

  #==============================================================================================================
  # 销售经理审批意向金转业绩
  #==============================================================================================================
    general_management_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#综合管理
    aim_trans_appv_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[7]/div/a/span[2]')#意向金转业绩审批
    aim_appv_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    lnk_man_loc = (By.ID,'txtlnknamelnkmobile')#联系人
    seach_btn_loc = (By.ID,'btnSearch')#查询
    aim_appv_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[13]/input')#审批

    #意向金转业绩待审批
    def openNeedAppvPage(self,lnk_man):
        self.lnk_man = lnk_man
        self.click_element(*self.general_management_loc)
        self.scrollToElement_new(*self.aim_trans_appv_loc)
        self.click_element(*self.aim_trans_appv_loc)
        self.switchToOneFrameByXpath(self.aim_appv_list_frame_loc)
        self.input_value(self.lnk_man_loc,lnk_man)
        time.sleep(1)
        self.waitElmentUntill(10,self.seach_btn_loc)
        self.click_element(*self.seach_btn_loc)
        self.waitElmentUntill(20,self.aim_appv_loc)
        time.sleep(1)
        self.click_element(*self.aim_appv_loc)

    #销售经理审批详情页
    pop_aim_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    approve_memo_loc = (By.NAME,'txt')#审批意见
    sale_appv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[8]/td[2]/input[1]')#通过
    confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确认

    def inputAppvDetail(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_aim_frame_loc)
        self.scrollToElement_new(*self.approve_memo_loc)
        self.input_value(self.approve_memo_loc,'自动化测试：意向金转业绩审批--销售经理')
        self.click_element(*self.sale_appv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.confirm_loc)

    def approveAimTransfer(self,lnk_mobile):
        '''销售经理审批意向金转业绩'''
        self.lnk_mobile = lnk_mobile
        self.openNeedAppvPage(lnk_mobile)
        self.inputAppvDetail()

#===========================================================================================================================
# 销售总监审批意向金转业绩
#===========================================================================================================================
    sales_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#销售管理
    aim_trans_appv_dirctor_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[2]/div/a/span[2]')#意向金转业绩审批-总监

    def openNeedAppvPage_Director(self,lnk_man):
        self.lnk_man = lnk_man
        self.click_element(*self.sales_manage_loc)
        self.click_element(*self.aim_trans_appv_dirctor_loc)
        self.switchToOneFrameByXpath(self.aim_appv_list_frame_loc)
        self.input_value(self.lnk_man_loc,lnk_man)
        time.sleep(1)
        self.waitElmentUntill(10,self.seach_btn_loc)
        self.click_element(*self.seach_btn_loc)
        self.waitElmentUntill(20,self.aim_appv_loc)
        time.sleep(1)
        self.click_element(*self.aim_appv_loc)

    # 销售总监审批详情页
    director_appv_pass_loc = (By.XPATH, '//*[@id="main"]/div[1]/table/tbody/tr[12]/td[2]/input[1]')  # 通过
    def inputAppvDetail_Director(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_aim_frame_loc)
        self.scrollToElement_new(*self.approve_memo_loc)
        self.input_value(self.approve_memo_loc, '自动化测试：意向金转业绩审批--销售总监')
        self.click_element(*self.director_appv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.confirm_loc)


    def approveAimTransfer_Director(self, lnk_mobile):
        '''销售总监审批意向金转业绩'''
        self.lnk_mobile = lnk_mobile
        self.openNeedAppvPage_Director(lnk_mobile)
        self.inputAppvDetail_Director()

#=========================================================================================================================
#     分总审批意向金转业绩
#=========================================================================================================================
    div_sales_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#销售管理
    aim_trans_appv_divsionManager_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[2]/div/a/span[2]')#意向金转业绩审批-分总

    def openNeedAppvPage_DivManager(self,lnk_man):
        self.lnk_man = lnk_man
        self.click_element(*self.div_sales_manage_loc)
        self.click_element(*self.aim_trans_appv_divsionManager_loc)
        self.switchToOneFrameByXpath(self.aim_appv_list_frame_loc)
        self.input_value(self.lnk_man_loc,lnk_man)
        time.sleep(1)
        self.waitElmentUntill(10,self.seach_btn_loc)
        self.click_element(*self.seach_btn_loc)
        self.waitElmentUntill(20,self.aim_appv_loc)
        time.sleep(1)
        self.click_element(*self.aim_appv_loc)

    # 分总审批详情页
    div_appv_pass_loc = (By.XPATH, '//*[@id="main"]/div[1]/table/tbody/tr[15]/td[2]/input[1]')  # 通过
    def inputAppvDetail_DivManager(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_aim_frame_loc)
        self.scrollToElement_new(*self.approve_memo_loc)
        self.input_value(self.approve_memo_loc, '自动化测试：意向金转业绩审批--销售总监')
        self.click_element(*self.div_appv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.confirm_loc)


    def approveAimTransfer_DivManager(self, lnk_mobile):
        '''分总审批意向金转业绩'''
        self.lnk_mobile = lnk_mobile
        self.openNeedAppvPage_DivManager(lnk_mobile)
        self.inputAppvDetail_DivManager()

#================================================================================================================================
#  数据部审批意向金转业绩
#================================================================================================================================
    data_aim_trans_appv_loc = (By.XPATH,'//*[@id="wnav"]/div[1]/div[2]/ul/li[11]/div/a/span[2]')#意向金转业绩审批
    city_loc = 'selCity'
    dt_aim_resultdetail_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_save_close_loc = (By.ID,'btnSaveClose')#保存关闭并发送
    dt_move_save_close_loc = 'btnSaveClose'

    dt_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确定

    dt_message_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_msg_send_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[4]/td[2]/input[1]') #发送
    dt_send_success_loc = (By.CLASS_NAME,'layui-layer-btn0')#发送成功

    def openNeedAppvPage_DataManager(self,lnk_man):
        self.lnk_man = lnk_man
        self.scrollToElement_new(*self.data_aim_trans_appv_loc)
        self.click_element(*self.data_aim_trans_appv_loc)
        self.switchToOneFrameByXpath(self.aim_appv_list_frame_loc)
        self.getDropdownMenuById(self.city_loc,1)
        self.input_value(self.lnk_man_loc,lnk_man)
        time.sleep(1)
        self.waitElmentUntill(10,self.seach_btn_loc)
        self.click_element(*self.seach_btn_loc)
        self.waitElmentUntill(20,self.aim_appv_loc)
        time.sleep(1)
        self.click_element(*self.aim_appv_loc)

    # 分总审批详情页
    data_appv_pass_loc = (By.XPATH, '//*[@id="main"]/div[1]/table/tbody/tr[21]/td[2]/input[1]')  # 通过
    def inputAppvDetail_DataManager(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_aim_frame_loc)
        self.scrollToElement_new(*self.approve_memo_loc)
        self.input_value(self.approve_memo_loc, '自动化测试：意向金转业绩审批--数据部')
        self.click_element(*self.data_appv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.confirm_loc)

        # 喜报详情页
        self.switchToParentFrame()
        self.switchWindow()
        time.sleep(2)
        self.switchToOneFrameByXpath(self.dt_aim_resultdetail_frame_loc)
        self.scrollToElement('id', self.dt_move_save_close_loc)
        self.click_element(*self.dt_save_close_loc)
        time.sleep(1)

        # 确认窗口
        self.switchWindow()
        self.click_element(*self.dt_confirm_loc)
        time.sleep(1)

        # QQ广播页面
        self.switchToParentFrame()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_message_frame_loc)
        self.click_element(*self.dt_msg_send_loc)
        time.sleep(1)

        # 发送成功确认
        self.switchWindow()
        self.click_element(*self.dt_send_success_loc)

    def approveAimTransfer_DataManager(self, lnk_mobile):
        '''分总审批意向金转业绩'''
        self.lnk_mobile = lnk_mobile
        self.openNeedAppvPage_DataManager(lnk_mobile)
        self.inputAppvDetail_DataManager()





























