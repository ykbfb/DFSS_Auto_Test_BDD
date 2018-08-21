import sys
sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.createIntviewPage import NewIntviewPage
from test_case.page_obj.myClientsPage import myClient
from data.ReadTestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
data = Data()

@When('查询邀约客户')
def step_searchClient(context):
    global  mc
    mc = myClient(context.driver)
    mc.gotoMyClientList_All(data.getCaseInitClient('邀约')['lnk_mobile'])
    mc.setWaitTime(2)

@When('输入DC邀约详情')
def step_inputIntviewDetail_DC(context):
    global intview
    intview = NewIntviewPage(context.driver)
    intview.createIntview_DC()
    functions.insert_img(context.driver, "createDCIntview_"+current_time+".png")

@Then('DC邀约创建成功')
def step_verifyIntviewCreateSucess_DC(context):
    intview.gobacktoDraftIntviewList()
    assert_that(intview.verifyDCIntviewCreateSucess(),equal_to('修改'))
    functions.insert_img(context.driver, "CheckCreateDCIntviewSucess"+current_time+".png")

@When('修改输入邀约详情')
def step_modifyIntviewDetail(context):
    intview = NewIntviewPage(context.driver)
    intview.modifyIntview()
    functions.insert_img(context.driver, "modifyIntview"+current_time+".png")

@Then('邀约修改成功')
def step_intviewModifySucess(context):
    intview.gobacktoIntviewList()
    assert_that(intview.verifyIntviewCreateSucess().strip(),equal_to('自动化测试：修改邀约'))
    functions.insert_img(context.driver, "CheckModifyIntviewSucess"+current_time+".png")

@When('输入邀约详情')
def step_inputIntviewDetail(context):
    intview = NewIntviewPage(context.driver)
    intview.createIntview()
    functions.insert_img(context.driver, "createIntview_"+current_time+".png")

@Then('邀约创建成功')
def step_verifyIntViewCreateSucess(context):
    intview = NewIntviewPage(context.driver)
    intview.gobacktoIntviewList()
    assert_that(intview.verifyIntviewCreateSucess().strip(),equal_to('自动化测试：创建邀约'))
    functions.insert_img(context.driver, "CheckCreateIntviewSucess"+current_time+".png")
