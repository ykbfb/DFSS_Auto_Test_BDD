import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ApproveIntviewPage import ApproveIntviewPage
from test_case.page_obj.base import *
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@Given('销售经理登录融管系统')
def step_loginSystem(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.sales_manager,'123456','suzhou')

@When('审批邀约')
def step_appvIntview(context):
    global appv_intview
    appv_intview = ApproveIntviewPage(context.driver)
    appv_intview.approveIntview()
    functions.insert_img(context.driver, "intview_approve_sucess_"+current_time+".png")

@Then('邀约审批成功')
def step_verifyIntviewAppvSucess(context):
    # 校验邀约是否审批成功
    appv_intview.gotoIntviewCompleteList()
    assert_that(appv_intview.verfifyIntviewAppvSuccess().strip(),equal_to(Data.cmp_name))
    functions.insert_img(context.driver, "verify_intview_approve_success_"+current_time+".png")
    appv_intview.close()

@When('邀约进行DC')
def step_IntviewDC(context):
    intview_appr_page = ApproveIntviewPage(context.driver)
    intview_appr_page.intview_DC()
    functions.insert_img(context.driver, "verify_intview_DC_sucess_"+current_time+".jpg")
