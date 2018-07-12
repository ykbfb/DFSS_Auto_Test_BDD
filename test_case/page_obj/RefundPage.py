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

class RefundPage(Page):
    # 合同管理
    contract_tab_loc = (By.XPATH,'//*[@id="bottomTabs_htgl"]/a')
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    def clickContractTab(self):
        self.click_element(*self.contract_tab_loc)
        self.scrollToElement('id',self.botom_frame_loc) # 页面跳转到底部【客户详情】所在的位置--相当于滚动条
        self.switchToOneFrame(self.botom_frame_loc) # 切换到底部【客户详情】的iframe

#=======================================================================================================================
#====                   新退费                                                                                 =========
#====        融资顾问→销售总监→分总→分公司财务→总部应收会计→CFO→总部付款出纳                             =========
#=======================================================================================================================
    # 退款
    member_refund_loc = (By.PARTIAL_LINK_TEXT,"退款") #会员费退款按钮
    pop_new_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    def openRefundPage(self):
        self.click_element(*self.member_refund_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.switchToOneFrameByXpath(self.pop_new_frame_loc)

    # 填写会员费退费
    refund_amt_loc = (By.ID,'refundAmount')#退款金额
    moveto_refund_amt_loc = 'refundAmount'
    bank_loc = (By.ID,'txtBank')#开户网点
    account_loc = (By.ID,'txtAccount')#银行账户
    material_loc = (By.ID,'ccb1')#资料
    refund_reason_loc = (By.ID,'txtRefundReason')#退款原因
    moveto_refund_reason_loc = 'txtRefundReason'
    submit_loc = (By.ID,'btnSub')#提交

    def inputRefundDetail(self):
        self.scrollToElement('id',self.moveto_refund_amt_loc)
        self.input_value(self.refund_amt_loc,100)
        self.input_value(self.bank_loc,'自动化测试：自动化测试银行茉莉花支行')
        self.input_value(self.account_loc,'8888888888888888888')
        self.click_element(*self.material_loc)
        self.scrollToElement('id',self.moveto_refund_reason_loc)
        self.input_value(self.refund_reason_loc,'自动化测试： 会员费退费')
        self.click_element(*self.submit_loc)
        time.sleep(1)
        self.close_alert()

    #顾问创建会员费退费
    def createRefund(self):
        self.clickContractTab()
        self.openRefundPage()
        self.inputRefundDetail()

#=====================================================================================================================
    #销售总监审批
    sales_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#销售管理
    refund_apprv_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[17]/div/a/span[2]')#新退费审批--总监
    moveto_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[17]/div/a/span[2]'
    refund_apprv_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    clt_name_loc = (By.ID,'clientOrLinkmanEq')#客户名称/联系人
    d_search_loc = (By.ID,'btnSearch')#查询
    approve_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[13]/input')#审批

    def approveRefund_Director(self,clt_name):
        self.clt_name = clt_name
        time.sleep(1)
        self.click_element(*self.sales_manage_loc)
        self.scrollToElement('xpath',self.moveto_refund_loc)
        self.click_element(*self.refund_apprv_loc)
        self.setWaitTime(5)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(2)
        self.click_element(*self.approve_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputApproveDetail_Dir()


    #审批详情页
    refund_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    apprv_memo_loc = (By.ID,'txtOpnion')#审批意见
    moveto_apprv_memo = 'txtOpnion'#审批意见
    dir_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[39]/td[2]/input[1]')#通过
    apprv_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')

    def inputApproveDetail_Dir(self):
        '''总监输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：审批新退费')
        self.click_element(*self.dir_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.apprv_confirm_loc)

#=================================================================================================================
    #分总审批新退费
    div_sales_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#分总--【销售管理】
    moveto_div_refund_loc = '//*[@id="wnav"]/div[2]/div[2]/ul/li[17]/div/a/span[2]'#新退费审批
    div_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[17]/div/a/span[2]')#

    def approveRefund_DivManager(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.div_sales_manage_loc)
        self.scrollToElement('xpath',self.moveto_div_refund_loc)
        self.click_element(*self.div_refund_loc)
        self.setWaitTime(5)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.approve_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputApproveDetail_Div()

    div_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[42]/td[2]/input[1]')#通过
    def inputApproveDetail_Div(self):
        '''分总输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：分总审批新退费')
        self.click_element(*self.div_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.apprv_confirm_loc)

#=================================================================================================================
    #分公司财务审批新退费
    casher_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#出纳
    moveto_fin_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[13]/div/a/span[2]'
    fin_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[13]/div/a/span[2]')#新退费审批
    fin_apprv_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[14]/input')#审批

    def approveRefund_Finance(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.casher_menu_loc)
        self.scrollToElement('xpath',self.moveto_fin_refund_loc)
        self.click_element(*self.fin_refund_loc)
        self.setWaitTime(5)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.fin_apprv_loc)
        time.sleep(2)
        self.switchWindow()
        self.inputApproveDetail_Fin()

    receipt_no_loc = (By.ID,'firstRefundToken') #收据编号
    moveto_receipt_no_loc = 'firstRefundToken'
    fin_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[46]/td[2]/input[1]')#通过
    def inputApproveDetail_Fin(self):
        '''分公司财务输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_receipt_no_loc)
        self.input_value(self.receipt_no_loc,'YYKK888')
        self.input_value(self.apprv_memo_loc,'自动化测试：分公司财务审批新退费')
        self.click_element(*self.fin_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #总部应收会计审批新退费
    accountant_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#付款专员
    moveto_acc_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[6]/div/a/span[2]'
    acc_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[3]/div[2]/ul/li[6]/div/a/span[2]')#新退费申请

    def approveRefund_Accountant(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.accountant_menu_loc)
        # self.scrollToElement('xpath',self.moveto_acc_refund_loc)
        self.click_element(*self.acc_refund_loc)
        self.setWaitTime(10)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(2)
        self.click_element(*self.fin_apprv_loc)
        time.sleep(2)
        self.switchWindow()
        self.inputApproveDetail_Acc()

    acc_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[48]/td[2]/input[1]')#通过
    def inputApproveDetail_Acc(self):
        '''总部应收会计输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：总部应收会计审批新退费')
        self.click_element(*self.acc_appvpass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #CFO审批新退费
    CFO_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[1]/div[1]')#CFO
    CFO_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[2]/ul/li[8]/div/a/span[2]')#新退费审批

    def approveRefund_CFO(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.CFO_menu_loc)
        self.click_element(*self.CFO_refund_loc)
        self.setWaitTime(5)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        time.sleep(2)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.approve_loc)
        time.sleep(2)
        self.switchWindow()
        self.inputApproveDetail_CFO()

    CFO_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[51]/td[2]/input[1]')#通过
    def inputApproveDetail_CFO(self):
        '''分总输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：CFO审批新退费')
        self.click_element(*self.CFO_appvpass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #总部付款出纳审批新退费
    center_cashier_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[5]/div[1]/div[1]')#钱智总部付款出纳
    cash_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[5]/div[2]/ul/li[6]/div/a/span[2]')#新退费申请

    def approveRefund_Cashier(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.center_cashier_menu_loc)
        self.click_element(*self.cash_refund_loc)
        self.setWaitTime(5)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        # self.waitElmentUntill(10,self.d_search_loc)
        self.click_element(*self.d_search_loc)
        time.sleep(2)
        self.click_element(*self.fin_apprv_loc)
        time.sleep(2)
        self.switchWindow()
        self.inputApproveDetail_Cash()

    cashier_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[54]/td[2]/input[1]')#通过
    def inputApproveDetail_Cash(self):
        '''总部付款出纳输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：总部付款出纳审批新退费')
        self.click_element(*self.cashier_appvpass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)


#=======================================================================================================================
#                   意向金退费                                                                                         =
#           融资顾问→销售总监→分总→分公司财务→总部应收会计→总部付款出纳                                           =
#=======================================================================================================================
    aimfee_refund_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[22]/div/a[1]') #退款
    pop_aim_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    moveto_aimAmt_loc = 'Amount'
    aim_refund_amt_loc = (By.ID,'Amount')#退款金额
    aim_bank_loc = (By.ID,'txtBank')#开户网点
    aim_account_loc = (By.ID,'txtAccount')#银行账户
    aim_material_loc = (By.ID,'ccb1')#资料情况
    moveto_aim_refund_reason_loc = 'txtReason'
    aim_refund_reason_loc = (By.ID,'txtReason')#意向金退款原因
    aim_submit_loc = (By.XPATH,'//*[@id="divShow"]/table/tbody/tr[10]/td[2]/input[1]')#提交


    def openAimRefundPage(self):
        '''打开意向金退费'''
        self.click_element(*self.aimfee_refund_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.switchToOneFrameByXpath(self.pop_aim_frame_loc)

    def inputAimRefundDetail(self):
        '''填写意向金退费详情'''
        self.scrollToElement('id',self.moveto_aimAmt_loc)
        self.input_value(self.aim_refund_amt_loc,10)
        self.input_value(self.bank_loc,'自动化测试银行花旗支行')
        self.input_value(self.account_loc,'8888888888888888888')
        self.click_element(*self.aim_material_loc)
        self.scrollToElement('id',self.moveto_aim_refund_reason_loc)
        self.input_value(self.aim_refund_reason_loc,'自动化测试： 意向金退费')
        self.click_element(*self.aim_submit_loc)
        time.sleep(1)
        self.close_alert()

    def createAimRefund_Sales(self):
        '''顾问创建意向金退费'''
        self.clickContractTab()
        self.openAimRefundPage()
        self.inputAimRefundDetail()

#==========================================================================================================
# 销售总监
    moveto_aim_refund_appv_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[9]/div/a/span[2]'
    aim_refund_appv_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[9]/div/a/span[2]')#外包意向金退费审批
    aim_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    aim_appv_btn_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[13]/input')#审批

    def openAimAppvPage(self):
        '''打开审批数据'''
        self.click_element(*self.sales_manage_loc)
        self.scrollToElement('xpath',self.moveto_aim_refund_appv_loc)
        self.click_element(*self.aim_refund_appv_loc)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.aim_list_frame_loc)
        self.click_element(*self.aim_appv_btn_loc)

    pop_aimappv_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    moveto_aim_appv_memo = 'txt'
    aim_appv_memo = (By.NAME,'txt')#审批意见
    aim_appv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[10]/td[2]/input[1]')
    aim_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')

    def inputAimAppvDetail_Dir(self):
        '''总监--输入意向金审批详情'''
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_aimappv_frame_loc)
        self.scrollToElement('name',self.moveto_aim_appv_memo)
        self.input_value(self.aim_appv_memo,'自动化测试：总监审批意向金退费')
        self.click_element(*self.aim_appv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.aim_confirm_loc)

    def approveAimRefund_Director(self):
        '''销售总监审批意向金退费'''
        self.openAimAppvPage()
        self.inputAimAppvDetail_Dir()

#=========================================================================================================================
# 分总审批意向金退费
    moveto_div_aim_refund_loc = '//*[@id="wnav"]/div[2]/div[2]/ul/li[10]/div/a/span[2]'
    div_aim_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[10]/div/a/span[2]')
    def div_openAimAppvPage(self):
        '''打开审批数据'''
        self.click_element(*self.div_sales_manage_loc)
        self.scrollToElement('xpath',self.moveto_div_aim_refund_loc)
        self.click_element(*self.div_aim_refund_loc)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.aim_list_frame_loc)
        self.click_element(*self.aim_appv_btn_loc)

    div_aim_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[13]/td[2]/input[1]')
    def inputAimAppvDetail_Div(self):
        '''分总--输入意向金审批详情'''
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_aimappv_frame_loc)
        self.scrollToElement('name',self.moveto_aim_appv_memo)
        self.input_value(self.aim_appv_memo,'自动化测试：分总审批意向金退费')
        self.click_element(*self.div_aim_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.aim_confirm_loc)

    def approveAimRefund_DivManager(self):
        '''分总审批意向金退费'''
        self.div_openAimAppvPage()
        self.inputAimAppvDetail_Div()

#===============================================================================================================
    #分公司财务审批新退费
    moveto_fin_aim_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[3]/div/a/span[2]'
    fin_aim_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[3]/div/a/span[2]')#意向金退费审批
    fin_aim_apprv_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[14]/input')#审批

    def approveAimRefund_Finance(self):
        self.click_element(*self.casher_menu_loc)
        self.scrollToElement('xpath',self.moveto_fin_aim_refund_loc)
        self.click_element(*self.fin_aim_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        time.sleep(1)
        self.click_element(*self.fin_aim_apprv_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputAimRefundApproveDetail_Fin()


    moveto_aim_recieptNo_loc = 'firstIntentionRefundToken'
    aim_recieptNo_loc = (By.ID, 'firstIntentionRefundToken')#退款收据号
    fin_aim_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[18]/td[2]/input[1]')#通过
    def inputAimRefundApproveDetail_Fin(self):
        '''分公司财务输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_aim_recieptNo_loc)
        self.input_value(self.aim_recieptNo_loc,'TEST888')
        self.input_value(self.aim_appv_memo,'自动化测试：分公司财务审批意向金退费')
        self.click_element(*self.fin_aim_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #总部应收会计审批意向金退费
    moveto_acc_aim_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[3]/div/a/span[2]'
    acc_aim_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[3]/div[2]/ul/li[3]/div/a/span[2]')#意向金退费审批

    def approveAimRefund_Accountant(self):
        self.click_element(*self.accountant_menu_loc)
        self.scrollToElement('xpath',self.moveto_acc_aim_refund_loc)
        self.click_element(*self.acc_aim_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        time.sleep(2)
        self.click_element(*self.fin_apprv_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputAimApproveDetail_Acc()

    acc_aim_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[19]/td[2]/input[1]')#通过
    def inputAimApproveDetail_Acc(self):
        '''总部应收会计输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('name',self.moveto_aim_appv_memo)
        self.input_value(self.aim_appv_memo,'自动化测试：总部应收会计审批新退费')
        self.click_element(*self.acc_aim_appvpass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #总部付款出纳审批意向金退费
    pay_aim_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[5]/div[2]/ul/li[3]/div/a/span[2]')#外包意向金退费审批

    def approveAimRefund_Cashier(self):
        self.click_element(*self.center_cashier_menu_loc)
        self.click_element(*self.pay_aim_refund_loc)
        self.setWaitTime(5)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.click_element(*self.fin_apprv_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputAimApproveDetail_Cash()

    cashier_aim_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[22]/td[2]/input[1]')#通过
    def inputAimApproveDetail_Cash(self):
        '''总部付款出纳输入意向金审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('name',self.moveto_aim_appv_memo)
        self.input_value(self.aim_appv_memo,'自动化测试：总部付款出纳审批意向金退费')
        self.click_element(*self.cashier_aim_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)

#=======================================================================================================================
#                   紧急退费                                                                                           =
#           分总→分公司财务→总部应收会计→CF0→总部付款出纳→销售经理→分公司财务                                    =
#=======================================================================================================================
# 分总发起紧急退费
    moveto_div_urgency_refund_loc = '//*[@id="wnav"]/div[2]/div[2]/ul/li[18]/div/a/span[2]'
    div_urgency_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[18]/div/a/span[2]')#紧急退费发起
    div_urgency_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    fuzzy_search_loc = (By.ID,'txtCheck')#模糊查询
    d_ur_search_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[2]/td/div/input[3]')#查询
    refund_btn_loc = (By.XPATH,'//*[@id="mytable"]/tbody/tr[2]/td[10]/input[2]')#退费

    def div_openCreateUrgencyRefundPage(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.div_sales_manage_loc)
        self.scrollToElement('xpath',self.moveto_div_urgency_refund_loc)
        self.click_element(*self.div_urgency_refund_loc)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.div_urgency_list_frame_loc)
        self.input_value(self.fuzzy_search_loc,clt_name)
        self.click_element(*self.d_ur_search_loc)
        self.setWaitTime(10)
        self.click_element(*self.refund_btn_loc)

    ur_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    finish_time_loc = 'txtPredictTime'#预计完成时间
    ur_refund_amt_loc = (By.ID,'refundAmount')#退款金额
    market_amt_loc = (By.ID,'txtOpRes')#市场业绩
    clt_bank_loc = (By.ID,'txtBank')#开户网点
    bank_account_loc = (By.ID,'txtAccount')#银行账户
    ur_material_loc = (By.ID,'ccb3')#特例退款承诺书
    moveto_ur_refund_reason_loc = 'txtReason'
    ur_refund_reason_loc = (By.ID,'txtReason')#退款原因
    ur_submit_loc = (By.ID,'btnSub')#提交

    def inputUrgencyRefundDetail(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.ur_pop_frame_loc)
        self.getDateTimePicker(self.finish_time_loc,str(time.strftime('%Y-%m-%d',time.localtime(time.time()))))
        self.input_value(self.ur_refund_amt_loc,100)
        #self.input_value(self.market_amt_loc,50)
        self.input_value(self.clt_bank_loc,'花旗银行湖心支行')
        self.input_value(self.bank_account_loc,'666666668888888')
        self.click_element(*self.ur_material_loc)
        self.scrollToElement('id',self.moveto_ur_refund_reason_loc)
        self.input_value(self.ur_refund_reason_loc,'自动化测试：紧急退费')
        self.click_element(*self.ur_submit_loc)
        time.sleep(1)
        self.close_alert()

    def createUrgencyRefund(self,clt_name):
        self.clt_name = clt_name
        self.div_openCreateUrgencyRefundPage(clt_name)
        self.inputUrgencyRefundDetail()


#=============================================================================================
# 分公司财务--紧急退费初审
    moveto_fin_ur_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[8]/div/a/span[2]'
    fin_ur_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[8]/div/a/span[2]')#紧急退费初审
    ur_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    ur_clt_name_loc = (By.ID,'txtCustomerNameOrLnkName')#客户名称、联系人
    ur_search_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[3]/td/input[5]')#查询
    ur_apprv_loc = (By.XPATH,'//*[@id="mytable"]/tbody/tr[2]/td[15]/input')#审批

    def approveUrgencyRefund_Finance(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.casher_menu_loc)
        self.scrollToElement('xpath',self.moveto_fin_ur_refund_loc)
        self.click_element(*self.fin_ur_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        time.sleep(1)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        self.click_element(*self.ur_apprv_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputUrgencyRefundApproveDetail_Fin()

    fin_ur_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    moveto_ur_apprv_memo_loc = 'txt'
    ur_apprv_memo_loc = (By.NAME,'txt')#审批意见
    ur_recieptNo_loc = (By.ID,'firstRefundToken')#退款收据号
    fin_ur_apprv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[14]/td[2]/input[1]')#通过
    ur_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')

    def inputUrgencyRefundApproveDetail_Fin(self):
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：紧急退费审批--分公司财务')
        self.input_value(self.ur_recieptNo_loc,'URGENCY')
        self.click_element(*self.fin_ur_apprv_pass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

    #=============================================================================================================
    #总部应收会计审批紧急退费
    moveto_acc_ur_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[4]/div/a/span[2]'
    acc_ur_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[3]/div[2]/ul/li[4]/div/a/span[2]')#紧急退费审批

    def approveUrgencyRefund_Accountant(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.accountant_menu_loc)
        self.scrollToElement('xpath',self.moveto_acc_ur_refund_loc)
        self.click_element(*self.acc_ur_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        time.sleep(1)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        self.click_element(*self.ur_apprv_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputUrgencyRefundApproveDetail_Acc()

    acc_ur_appv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[15]/td[2]/input[1]')
    def inputUrgencyRefundApproveDetail_Acc(self):
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：紧急退费审批--总部应收会计')
        self.click_element(*self.acc_ur_appv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#=====================================================================================================================
# CFO 紧急退费审批
    CFO_ur_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[2]/ul/li[7]/div/a/span[2]')#紧急退费审批

    def approveUrgencyRefund_CFO(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.CFO_menu_loc)
        self.click_element(*self.CFO_ur_refund_loc)
        self.setWaitTime(5)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        time.sleep(1)
        self.click_element(*self.ur_apprv_loc)
        time.sleep(1)
        self.switchWindow()
        self.inputUrgencyRefundApproveDetail_CFO()

    CFO_ur_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[18]/td[2]/input[1]')#通过
    def inputUrgencyRefundApproveDetail_CFO(self):
        '''CFO输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：紧急退费审批--CFO')
        self.click_element(*self.CFO_ur_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#=======================================================================================================================
  #总部付款出纳审批紧急退费
    pay_ur_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[5]/div[2]/ul/li[4]/div/a/span[2]')#紧急退费审批

    def approveUrgencyRefund_Cashier(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.center_cashier_menu_loc)
        self.click_element(*self.pay_ur_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        time.sleep(1)
        self.click_element(*self.ur_apprv_loc)
        self.switchWindow()
        self.inputUrgencyApproveDetail_Cash()

    cashier_ur_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[21]/td[2]/input')#通过
    def inputUrgencyApproveDetail_Cash(self):
        '''总部付款出纳输入紧急退费审批意见'''
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：紧急退费审批--总部付款出纳')
        self.click_element(*self.cashier_ur_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#=========================================================================================================================
# 销售经理审批紧急退费
    manage_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#综合管理
    moveto_sal_mager_ur_refund_loc = '//*[@id="wnav"]/div[2]/div[2]/ul/li[11]/div/a/span[2]/label'
    sal_mager_ur_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[11]/div/a/span[2]/label')#紧急退费审批

    def approveUrgencyRefund_SalesManager(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.manage_menu_loc)
        self.scrollToElement('xpath',self.moveto_sal_mager_ur_refund_loc)
        self.click_element(*self.sal_mager_ur_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        time.sleep(1)
        self.click_element(*self.ur_apprv_loc)
        self.switchWindow()
        self.inputUrgencyApproveDetail_SalesManager()

    salManager_ur_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[24]/td[2]/input[1]')#通过
    def inputUrgencyApproveDetail_SalesManager(self):
        '''总部付款出纳输入紧急退费审批意见'''
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：紧急退费审批--销售经理')
        self.click_element(*self.salManager_ur_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#=============================================================================================
# 分公司财务-紧急退费终审
    moveto_fin_final_ur_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[10]/div/a/span[2]'
    fin_final_ur_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[10]/div/a/span[2]')#紧急退费初审

    def final_ApproveUrgencyRefund_Finance(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.casher_menu_loc)
        self.scrollToElement('xpath',self.moveto_fin_final_ur_refund_loc)
        self.click_element(*self.fin_final_ur_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        time.sleep(1)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        self.click_element(*self.ur_apprv_loc)
        self.switchWindow()
        self.inputUrgencyRefundFinalApproveDetail_Fin()

    fin_final_ur_apprv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[27]/td[2]/input[1]')#通过
    def inputUrgencyRefundFinalApproveDetail_Fin(self):
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：紧急退费终审--分公司财务')
        self.click_element(*self.fin_final_ur_apprv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#====================================================================================================================================
#          投诉强制退费                                                                                                             =
#     客服→客服总监→分公司财务→总部应收会计→CF0→总部付款出纳（知会分总）                                                       =
#====================================================================================================================================

#=====================================================================================================================================
#   客服创建投诉强制退费

    force_refund_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#投诉强制退费
    create_forRefund_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[1]/div/a/span[2]')#强制退费发起
    for_refund_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    city_loc = 'selCity'#城市
    for_clt_name_loc = (By.ID,'txtCheck')#模糊查询
    for_search_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[2]/td/div/input[3]')#查询
    f_refund_btn_loc = (By.XPATH,'//*[@id="mytable"]/tbody/tr[2]/td[10]/input[2]')#退费

    def createForceRefund(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.force_refund_menu_loc)
        self.click_element(*self.create_forRefund_loc)
        self.setWaitTime(10)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.for_refund_list_frame_loc)
        self.getDropdownMenuById(self.city_loc,0)
        self.input_value(self.for_clt_name_loc,clt_name)
        self.click_element(*self.for_search_loc)
        time.sleep(1)
        self.click_element(*self.f_refund_btn_loc)
        self.inputForceRefundDetail()


    for_refund_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    for_refund_amt_loc = (By.ID,'refundAmount')#退费金额
    for_refund_reason_loc = (By.ID,'txtReason')#退费原因
    complain_content_loc = (By.ID,'txtComplant')#投诉内容
    moveto_for_submit_loc = '//*[@id="main"]/table/tbody/tr[12]/td/input[2]'
    for_submit_loc = (By.XPATH,'//*[@id="main"]/table/tbody/tr[12]/td/input[2]')#提交

    def inputForceRefundDetail(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.for_refund_pop_frame_loc)
        self.input_value(self.for_refund_amt_loc,100)
        self.input_value(self.for_refund_reason_loc,'自动化测试：强制退费创建--客服专员')
        self.input_value(self.complain_content_loc,'自动化测试：客户不满意，要求强制退费')
        self.scrollToElement('xpath',self.moveto_for_submit_loc)
        self.click_element(*self.for_submit_loc)
        time.sleep(1)
        self.close_alert()

#=================================================================================================================================
#   强制退费审批--客服

    for_refund_apprv_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[1]/div[2]/ul/li[3]/div/a/span[2]')#投诉强制退费审批
    for_refund_appv_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    for_appv_city_loc = 'selCity'#城市
    for_appv_clt_name_loc = (By.ID,'txtCustomerNameOrLnkName')#客户名称、联系人
    for_appv_search_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[3]/td/input[5]')#查询
    for_appv_btn_loc = (By.XPATH,'//*[@id="mytable"]/tbody/tr[2]/td[15]/input')#审批

    def approveForceRefund_CustomerScevice(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.for_refund_apprv_menu_loc)
        self.setWaitTime(10)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.for_refund_appv_list_frame_loc)
        self.getDropdownMenuById(self.for_appv_city_loc,1)
        self.input_value(self.for_appv_clt_name_loc,clt_name)
        self.click_element(*self.for_appv_search_loc)
        time.sleep(1)
        self.click_element(*self.for_appv_btn_loc)
        self.inputAppvForRefund_CS()

    for_refund_appv_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    for_refund_bank_loc = (By.ID,'txtBank')
    for_refund_accunt_loc = (By.ID,'txtAccount')
    for_refund_material_loc = (By.ID,'ccb1')
    moveto_for_appv_submit_loc = '//*[@id="main"]/table/tbody/tr[10]/td/input[2]'
    for_appv_submit_loc = (By.XPATH,'//*[@id="main"]/table/tbody/tr[10]/td/input[2]')

    def inputAppvForRefund_CS(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.for_refund_appv_pop_frame_loc)
        self.input_value(self.for_refund_bank_loc,'自动化测试银行罗山支行')
        self.input_value(self.for_refund_accunt_loc,'4565646464646454654')
        self.click_element(*self.for_refund_material_loc)
        self.scrollToElement('xpath',self.moveto_for_appv_submit_loc)
        self.click_element(*self.for_appv_submit_loc)
        time.sleep(1)
        self.close_alert()

#==========================================================================================================================
#    强制退费审批--客服总监

    d_for_refund_appv_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[1]/div[2]/ul/li/div/a/span[2]')
    def approveForceRefund_ServiceDirector(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.d_for_refund_appv_menu_loc)
        self.setWaitTime(10)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.for_refund_appv_list_frame_loc)
        self.getDropdownMenuById(self.for_appv_city_loc,1)
        self.input_value(self.for_appv_clt_name_loc,clt_name)
        self.click_element(*self.for_appv_search_loc)
        time.sleep(1)
        self.click_element(*self.for_appv_btn_loc)
        self.inputAppvForRefund_SD()

    moveto_for_refund_appv_memo_loc = 'txt'
    for_refund_appv_memo_loc = (By.NAME,'txt')
    for_refund_app_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[11]/td[2]/input[1]')
    for_refund_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')

    def inputAppvForRefund_SD(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.for_refund_appv_pop_frame_loc)
        self.scrollToElement('name',self.moveto_for_refund_appv_memo_loc)
        self.input_value(self.for_refund_appv_memo_loc,'自动化测试：客服总监审批')
        self.click_element(*self.for_refund_app_pass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.for_refund_confirm_loc)
#=============================================================================================
# 分公司财务-强制退费审批
    moveto_for_refund_menu_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[12]/div/a/span[2]'
    for_refund_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[12]/div/a/span[2]')#投诉强制退费审批

    def approveForceRefund_Finance(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.casher_menu_loc)
        self.scrollToElement('xpath',self.moveto_for_refund_menu_loc)
        self.click_element(*self.for_refund_menu_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.for_refund_appv_list_frame_loc)
        time.sleep(1)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        self.click_element(*self.ur_apprv_loc)
        self.inputForceRefundApproveDetail_Fin()

    for_refund_reciptNo_loc = (By.ID,'firstRefundToken')
    fin_for_apprv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[17]/td[2]/input[1]')#通过
    def inputForceRefundApproveDetail_Fin(self):
        self.switchWindow()
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.for_refund_reciptNo_loc,'No43650')
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：投诉强制退费--分公司财务')
        self.click_element(*self.fin_for_apprv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#====================================================================================================================================
#总部应收会计审批--强制退费
    acc_for_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[3]/div[2]/ul/li[5]/div/a/span[2]')#投诉强制退费审批

    def approveForceRefund_Accountant(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.accountant_menu_loc)
        self.click_element(*self.acc_for_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        time.sleep(1)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        self.click_element(*self.ur_apprv_loc)
        self.switchWindow()
        self.inputForceRefundApproveDetail_Acc()

    acc_for_appv_pass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[18]/td[2]/input[1]')
    def inputForceRefundApproveDetail_Acc(self):
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：投诉强制退费审批--总部应收会计')
        self.click_element(*self.acc_for_appv_pass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#=====================================================================================================================
# CFO 紧急退费审批
    CFO_for_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[2]/ul/li[5]/div/a/span[2]')#投诉强制退费审批

    def approveForceRefund_CFO(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.CFO_menu_loc)
        self.click_element(*self.CFO_for_refund_loc)
        self.setWaitTime(5)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        time.sleep(1)
        self.click_element(*self.ur_apprv_loc)
        self.inputForceRefundApproveDetail_CFO()

    CFO_for_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[21]/td[2]/input[1]')#通过
    def inputForceRefundApproveDetail_CFO(self):
        '''CFO输入审批意见'''
        self.switchWindow()
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：投诉强制退费审批--CFO')
        self.click_element(*self.CFO_for_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)

#=======================================================================================================================
  #总部付款出纳审批紧急退费
    pay_for_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[5]/div[2]/ul/li[5]/div/a/span[2]')#投诉强制退费审批

    def approveForceRefund_Cashier(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.center_cashier_menu_loc)
        self.click_element(*self.pay_for_refund_loc)
        self.setWaitTime(5)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.ur_list_frame_loc)
        self.input_value(self.ur_clt_name_loc,clt_name)
        self.click_element(*self.ur_search_loc)
        time.sleep(1)
        self.click_element(*self.ur_apprv_loc)
        self.inputForceApproveDetail_Cash()

    cashier_for_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[24]/td[2]/input[1]')#通过
    def inputForceApproveDetail_Cash(self):
        '''总部付款出纳输入紧急退费审批意见'''
        self.switchWindow()
        self.switchToOneFrameByXpath(self.fin_ur_pop_frame_loc)
        self.scrollToElement('name',self.moveto_ur_apprv_memo_loc)
        self.input_value(self.ur_apprv_memo_loc,'自动化测试：投诉强制退费审批--总部付款出纳')
        self.click_element(*self.cashier_for_appvpass_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.ur_confirm_loc)






































# ==================================================================================================
    # 验证case的执行结果：  未完待续
