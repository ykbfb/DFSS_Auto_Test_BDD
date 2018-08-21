import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.ApproveIntviewPage import ApproveIntviewPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


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
