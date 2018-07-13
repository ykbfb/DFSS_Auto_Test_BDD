import sys
sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.FinceBookInfoPage import finceBookInfo
from data.TestData import Data
import time
from selenium import webdriver
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('修改需求书并保存')
def step_saveFinceBookInfo(context):
    global fb
    fb = finceBookInfo(context.driver)  # 打开需求书
    fb.saveFinancBookInfo()
    fb.setWaitTime(2)
    functions.insert_img(context.driver, "financeBookInfo_afterSave_"+current_time+".png")

@When('修改需求书并提交')
def step_submitFinceBookInfo(context):
    fb.submitFinanceBookInfo()
    fb.setWaitTime(2)
    functions.insert_img(context.driver, "financeBookInfo_afterSubmit_"+current_time+".png")

@Then('需求书保存成功')
def step_verifyFinceBoookInfoSaveSucess(context):
    # 校验需求书是否保存成功
    assert_that(fb.verify_finceBookInfo_save_success(),equal_to('自动化测试有限公司'))
    functions.insert_img(context.driver, "myClient_verifyFinBookSave"+current_time+".png")

@Then('需求书提交成功')
def step_verifyFinceBoookInfoSubmitSucess(context):
    # 校验需求书是否保存成功
    assert_that(fb.verify_finceBookInfo_save_success(),equal_to(Data.cmp_name))
    functions.insert_img(context.driver, "myClient_verifyFinBookSave"+current_time+".png")

