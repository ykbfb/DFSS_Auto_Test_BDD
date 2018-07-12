import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.BillReceiptPage import NewOrderPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('进入【出纳】-【收款单管理】点击【新增】按钮创建收款单')
def step_createBillReceipt(context):
    global  bill
    bill = NewOrderPage(context.driver)
    bill.createBill(Data.ContractCode)
    bill.setWaitTime(2)

@Then('收款单创建成功')
def step_verifyBillReceiptCreateSucess(context):
    bill.backtoBillList()
    bill.searchBillReceipt(Data.ContractCode)
    assert_that(bill.verifyBillReceiptActionSucess().strip(),equal_to("未结算"))
    functions.insert_img(context.driver, "BillReceiptCreateSucess_"+current_time+".png")

@When('进入【出纳】-【收款单管理】输入合同号查询收款单，点击【结算】按钮结算收款单')
def step_caculateBillReceipt(context):
    bill.caculateBill(Data.ContractCode)
    bill.setWaitTime(2)
    functions.insert_img(context.driver, "caculateBill_"+current_time+".png")

@Then('收款单结算成功')
def step_BillCaculateSucess(context):
    bill.searchBillReceipt(Data.ContractCode, '已结算')
    assert_that(bill.verifyBillReceiptActionSucess().strip(),equal_to("已结算"))
    functions.insert_img(context.driver, "VerifyCaculateBillSucess_"+current_time+".png")
    bill.setWaitTime(2)