

import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.createClientPage import createClient
from data.TestData import Data
import time
from selenium import webdriver
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('输入已存在的手机号')
def step_inputClientDetail(context):
    global nc
    nc = createClient(context.driver)
    nc.setWaitTime(2)
    nc.open_rapidOperation()
    nc.open_newClient()
    nc.switchToNewClientFrame()
    nc.inputMobile('12589756835')
    nc.checkMobileIsDuplicate()

@When('输入系统中不存在的手机号')
def step_inputClientDetail(context):
    global nc
    nc = createClient(context.driver)
    nc.setWaitTime(2)
    nc.open_rapidOperation()
    nc.open_newClient()
    nc.switchToNewClientFrame()
    nc.inputMobile(Data.lnk_moblie)
    nc.checkMobileIsDuplicate()
    time.sleep(1)

@Then('校验客户已经存在')
def step_checkClientIsExist(context):
    assert_that(nc.check_num_isExist().strip(), equal_to('该客户已经归属当前登录用户'))
    functions.insert_img(context.driver, "Client_isExist_"+current_time+".png")

@Then('校验客户不存在')
def step_checkClientIsNotExist(context):
    assert_that(nc.check_num_isExist().strip(), equal_to('验证通过'))
    functions.insert_img(context.driver, "Client_isNotExist_"+current_time+".png")



@When('输入客户详情')
def step_createNewClient(context):
    time.sleep(1)
    functions.insert_img(context.driver, current_time + "Client_isNotExist_" +current_time+".png")
    nc.selectCltExeStatus()
    nc.selectLoanArea()
    nc.saveClient()
    time.sleep(1)
    functions.insert_img(context.driver, "Client_isCreateSuccess_"+current_time+".png")  # 客户详情

@Then('客户创建成功')
def step_clientCreateSucess(context):
    nc.checkClientCreateSuccess(Data.lnk_moblie)
    functions.insert_img(context.driver, "CheckClient_isCreateSuccess_"+current_time+".png")
    assert_that(nc.check_client_createSucess(), equal_to(''))
    nc.close()




