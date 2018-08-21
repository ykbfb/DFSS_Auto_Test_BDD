

import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.createClientPage import createClient
from data.ReadTestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
data=Data()

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
    nc.inputMobile(data.getCaseInitClient('新增客户')['lnk_mobile'])
    nc.checkMobileIsDuplicate()
    time.sleep(1)

@When('输入系统中不存在的手机号:{lnk_mobile}')
def step_inputClientDetail(context,lnk_mobile):
    context.lnk_mobile = lnk_mobile
    global nc
    nc = createClient(context.driver)
    nc.setWaitTime(2)
    nc.open_rapidOperation()
    nc.open_newClient()
    nc.switchToNewClientFrame()
    nc.inputMobile(lnk_mobile)
    # nc.inputMobile(Data.lnk_moblie)
    nc.checkMobileIsDuplicate()
    time.sleep(1)

@Then('校验客户已经存在')
def step_checkClientIsExist(context):
    assert_that(nc.check_num_isExist().strip(), equal_to('该客户已经存在，如有必要可进入冲突查询界面查询'))
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

@Then('客户创建成功:{lnk_mobile}')
def step_clientCreateSucess(context,lnk_mobile):
    context.lnk_mobile = lnk_mobile
    nc.checkClientCreateSuccess(lnk_mobile)
    functions.insert_img(context.driver, "CheckClient_isCreateSuccess_"+current_time+".png")
    assert_that(nc.check_client_createSucess(), equal_to(''))

@Then('客户创建成功')
def step_clientCreateSucess(context):
    nc.checkClientCreateSuccess(data.getCaseInitClient('新增客户')['lnk_mobile'])
    functions.insert_img(context.driver, "CheckClient_isCreateSuccess_"+current_time+".png")
    assert_that(nc.check_client_createSucess(), equal_to(''))



