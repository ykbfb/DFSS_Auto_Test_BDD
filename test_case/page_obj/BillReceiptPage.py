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

class NewOrderPage(Page):
    #出纳-》收款单管理
    finc_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]') #出纳
    bill_manage_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[18]/div/a/span[2]'#收款单管理
    bill_manage2_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[18]/div/a/span[2]')
    billList_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe' #收款单管理列表页frame

    #打开【收款单管理】
    def openBillReceiptPage(self):
        self.find_element(*self.finc_nav_loc).click()
        self.setWaitTime(10)
        self.scrollToElement('xpath',self.bill_manage_loc)
        self.find_element(*self.bill_manage2_loc).click()
        time.sleep(2)
        self.switchToDefaultContent()
        self.switchToOneFrameByXpath(self.billList_loc)

    #填写问款详情
    add_bill_loc = (By.ID,'btnAdd')
    new_bill_frame_loc =  "//iframe[contains(@id, 'layui-layer-iframe')]"
    contract_code_loc = (By.ID,'txtContractCode')#合同号
    select_contract_loc = (By.XPATH,'//*[@id="divShowSelectableList_txtContractCode_tbList"]/tr/td')
    billcode_loc = (By.ID,'fbillCode') #收据号
    billAmt_loc = (By.ID,'recAmount') #收款金额
    memo_loc = (By.ID,'memo') #备注
    bill_submit_loc = (By.ID,'btnSubmit') #提交收款单

    def inputBillDetail(self,contractCode):
        self.contractCode = contractCode
        self.find_element(*self.add_bill_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.new_bill_frame_loc)
        self.find_element(*self.contract_code_loc).clear()
        self.find_element(*self.contract_code_loc).send_keys(contractCode)
        time.sleep(1)
        self.find_element(*self.select_contract_loc).click()
        self.find_element(*self.billcode_loc).clear()
        self.find_element(*self.billcode_loc).send_keys('D10000123')
        self.find_element(*self.billAmt_loc).clear()
        self.find_element(*self.billAmt_loc).send_keys(20000)
        self.find_element(*self.memo_loc).clear()
        self.find_element(*self.memo_loc).send_keys('自动化测试-创建收款单')
        self.find_element(*self.bill_submit_loc).click()

    #收款单结算
    search_contract_code_loc = (By.ID,'contractCode') #查询条件合同号
    bill_status_loc = 'selCalcStatus'#结算状态
    search_loc = (By.ID,'btnCheck') #查询
    cacul_radio_loc = (By.ID,'cbxAll')#列表中选择收款单
    cacl_btn_loc = (By.ID,'btnCalc') #结算按钮
    pop_confirm__loc = (By.CLASS_NAME,'layui-layer-btn0')

    def searchBillReceipt(self,ContractCode,bill_status = '未结算'):
        self.ContractCode = ContractCode
        self.bill_status = bill_status
        self.find_element(*self.search_contract_code_loc).clear()
        self.find_element(*self.search_contract_code_loc).send_keys(ContractCode)
        if bill_status == '未结算':
            self.getDropdownMenuById(self.bill_status_loc, 1)
        else:
            self.getDropdownMenuById(self.bill_status_loc, 2)
        self.find_element(*self.search_loc).click()


#============================================================================================================
#创建收款单公共方法
#============================================================================================================
    def createBill(self,ContractCode = 'NHY05122017000072'):
        self.ContractCode = ContractCode
        self.openBillReceiptPage()
        self.inputBillDetail(ContractCode)
        time.sleep(1)
        self.close_alert()
        time.sleep(1)

    #创建后返回收款单列表
    def backtoBillList(self):
        self.switchToParentFrame()
#============================================================================================================
#收款单结算
#============================================================================================================
    def caculateBill(self,ContractCode):
        self.ContractCode = ContractCode
        self.openBillReceiptPage()
        self.searchBillReceipt(ContractCode)
        self.find_element(*self.cacul_radio_loc).click()
        self.find_element(*self.cacl_btn_loc).click()
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.pop_confirm__loc)

#============================================================================================================
#验证测试结果
#============================================================================================================
    bill_not_cal_loc = (By.XPATH,'//*[@id="mytable"]/tbody/tr[2]/td[4]')#列表页
    def verifyBillReceiptActionSucess(self):
        return self.find_element(*self.bill_not_cal_loc).text