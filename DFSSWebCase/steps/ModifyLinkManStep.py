import sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from data.TestData import Data
import time
from selenium import webdriver
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('查询客户')
def step_searchClient(context):
    global  mc
    mc = myClient(context.driver)
    mc.gotoMyClientList_All(Data.lnk_moblie)
    mc.setWaitTime(2)

@When('输入联系人详情')
def step_modifyLnkMan(context):
    mc.modifyLnkMan('坤坤测试','测试总经理','创始人','8888888','yk@test.com')

@Then('联系人修改成功')
def step_veryLnkManModifySucess(context):
    assert_that(mc.verify_modify_lnkMan(), equal_to('坤坤测试'))
    functions.insert_img(context.driver, "myClient_modifyLnkMan_"+current_time+".png")

@When('模糊查询客户')
def step_fuzzySearch(context):
    mc.gotoMyClientList_All(Data.lnk_moblie)
    mc.setWaitTime(2)

@Then('客户查询成功')
def step_verifySearchSucess(context):
    assert_that(mc.search_by_fuzzy(), '坤坤测试')
    functions.insert_img(context.driver, "myClient_fuzzysearch_"+current_time+".png")
    mc.close()

