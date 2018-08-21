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

from selenium.webdriver.common.by import By
from .base import Page
import time

class NewOrderPage(Page):
    # 订单管理
    order_tab_loc = (By.XPATH,'//*[@id="bottomTabs_ddgl"]/a')
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    def clickOrderTab(self):
        self.find_element(*self.order_tab_loc).click()
        self.scrollToElement('id',self.botom_frame_loc) # 页面跳转到底部【客户详情】所在的位置--相当于滚动条
        self.switchToOneFrame(self.botom_frame_loc) # 切换到底部【客户详情】的iframe

    # 订单创建详情
    createOrderBtn_loc = (By.XPATH,'//*[@id="btnAddOrder"]/span/span') #创建销售订单
    new_order_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    sel_contract_loc = 'contractsselections' # 合同选择

    #企业主、个体户订单详情
    moveto_cmp_area_loc = 'CMP_AREA'
    cmp_area_loc =(By.NAME,'CMP_AREA')  # 公司所在地
    year_income_loc = 'txtAllRuing' # 近一年总流水
    loan_useFor_loc = 'txtUseWay'# 借款用途
    paybackSource_loc = 'Select1' # 还款来源
    fundDate_loc = 'cmpsg_time_van' # 公司成立时间

    def inputOrderDetail_CMP(self):
        self.click_element(*self.createOrderBtn_loc)
        self.switchToParentFrame()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.new_order_frame_loc)
        self.getDropdownMenuById(self.sel_contract_loc, 1)
        time.sleep(1)
        self.scrollToElement('name',self.moveto_cmp_area_loc)
        self.click_element(*self.cmp_area_loc)
        self.getDateTimePicker(self.fundDate_loc, '2012-06-18')
        self.getDropdownMenuById(self.year_income_loc, 6)
        self.getDropdownMenuById(self.loan_useFor_loc, 7)
        self.getDropdownMenuById(self.paybackSource_loc, 1)
        self.inputProductDetail()

    #工薪族、其他 订单详情
    person_loanAmt_loc = (By.ID,'txtLan') # 借款额度
    person_loanPriod_loc = (By.ID,'Text1') # 借款期限
    person_useDuration_loc = 'useDuration_'# 用款时间
    person_cridit_loc = 'in24yuqicount'# 个人信用

    def inputOrderDetail_Personal(self):
        self.find_element(*self.createOrderBtn_loc).click()
        self.switchToParentFrame()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.new_order_frame_loc)
        self.getDropdownMenuById(self.sel_contract_loc, 1)
        self.find_element(*self.person_loanAmt_loc).clear()
        self.find_element(*self.person_loanAmt_loc).send_keys(55)
        self.find_element(*self.person_loanPriod_loc).click()
        self.getDateTimePicker(self.person_useDuration_loc, '2012-06-18')
        self.getDropdownMenuById(self.loan_useFor_loc, 7)
        self.getDropdownMenuById(self.paybackSource_loc, 1)
        self.getDropdownMenuById(self.person_cridit_loc, 1)
        self.inputProductDetail()

    #输入产品明细
    productName_loc = (By.ID,'ProductName') #产品名称
    productRate_loc = (By.ID,'MoneyRate') #利率
    loan_amt_loc = (By.ID,'LoanLimit') #额度
    repayWay_loc = 'RepaymentType'#还款方式
    loan_startTime_loc = 'ExpectedLoanStr'#预计放款时间从
    loan_endTime_loc = 'ExpectedLoadEnd'#预计放款时间到
    add_prd_loc = (By.XPATH,'//*[@id="tableRegex"]/tbody/tr[1]/td[7]/div')# 添加产品

    def inputProductDetail(self):
        self.find_element(*self.productName_loc).clear()
        self.find_element(*self.productName_loc).send_keys('菠萝菠萝蜜')
        self.find_element(*self.productRate_loc).clear()
        self.find_element(*self.productRate_loc).send_keys('1.5')
        self.find_element(*self.loan_amt_loc).clear()
        self.find_element(*self.loan_amt_loc).send_keys(30)
        self.getDropdownMenuById(self.repayWay_loc, 1)
        self.getDateTimePicker(self.loan_startTime_loc,'2017-06-18')
        self.getDateTimePicker(self.loan_endTime_loc,'2017-07-18')
        self.find_element(*self.add_prd_loc).click()

    #提交主订单
    moveto_submit_order_loc = '//*[@id="main"]/form/table/tbody/tr[6]/td/input'
    submit_order_loc = (By.XPATH,'//*[@id="main"]/form/table/tbody/tr[6]/td/input')
    confirm_btn_loc = (By.CLASS_NAME,'layui-layer-btn0')
    close_win_loc = (By.XPATH,'//*[@id="layui-layer2"]/span[1]/a[3]')
    def submitOrder(self):
        self.scrollToElement('xpath',self.moveto_submit_order_loc)
        self.find_element(*self.submit_order_loc).click()
        self.setWaitTime(2)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.confirm_btn_loc)

#============================================================================================================
#创建主订单公共方法
#============================================================================================================
    def createOrderForCMP(self):
        '''企业主、个体户订单'''
        self.clickOrderTab()
        self.inputOrderDetail_CMP()
        self.submitOrder()

    def createOrderForPerson(self):
        '''工薪族、其他订单'''
        self.clickOrderTab()
        self.inputOrderDetail_Personal()
        self.submitOrder()

#================================================================================================================
#校验测试用例是否成功
#================================================================================================================
    sales_order_clt_name_loc = (By.XPATH,'//*[@id="main"]/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[3]/div')#客户名称
    def verifySalesOrderCreateSucess(self):
        return self.find_element(*self.sales_order_clt_name_loc).text

