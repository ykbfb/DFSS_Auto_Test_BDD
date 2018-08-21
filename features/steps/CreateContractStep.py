import sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.createContractPage import NewContractPage
from data.ReadTestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
data = Data()

@When('查询合同客户')
def step_searchClient(context):
    global  mc
    mc = myClient(context.driver)
    mc.gotoMyClientList_All(data.getCaseInitClient('创建合同')['lnk_mobile'])
    mc.setWaitTime(2)

@When('进入【合同管理】页签点击【创建合同】按钮，选择【债权会员合同】并输入会员合同信息详情')
def step_inputVIPContractDetail(context):
    global cp
    cp = NewContractPage(context.driver)
    cp.createVIPContract()
    functions.insert_img(context.driver, "createVIPContract"+current_time+".png")

@Then('会员合同创建成功')
def step_verifyVIPContractCreateSucess(context):
    cp.gobackToContractlist()
    assert_that(cp.verifyContractCreateSucess(),equal_to('发票申请'))
    functions.insert_img(context.driver, "CheckCreateVIPContractSucess"+current_time+".png")

@When('进入【合同管理】页签点击【创建合同】按钮，选择【债权外包合同】并输入外包合同信息详情')
def step_inputBPOContractDetail(context):
    cp = NewContractPage(context.driver)
    cp.createBPOContract()
    functions.insert_img(context.driver, "createBPOContract_"+current_time+".png")

@Then('外包合同创建成功')
def step_verifyBPOContractCreateSucess(context):
    cp.gobackToContractlist()
    assert_that(cp.verifyContractCreateSucess(),equal_to('发票申请'))
    functions.insert_img(context.driver, "CheckCreateBPOContract"+current_time+".png")
    
@When('进入【合同管理】页签点击【转会员】按钮，选择【债权会员合同】并输入会员合同信息详情')
def step_inputBPOContractDetail(context):
    cp = NewContractPage(context.driver)
    cp.BPOContractTransToVIP()
    functions.insert_img(context.driver, "BPOContractChangeToVIP"+current_time+".png")

@Then('外包转会员合同创建成功')
def step_verifyBPOContractCreateSucess(context):
    cp.gobackToContractlist()
    assert_that(cp.verifyContractCreateSucess(),equal_to('发票申请'))
    functions.insert_img(context.driver, "CheckCreateVIP_to_BPOContract"+current_time+".png")