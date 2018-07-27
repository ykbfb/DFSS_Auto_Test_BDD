import unittest, sys
sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ApproveChannelResultPage import ChannalResultApprovalPage
from test_case.page_obj.base import *
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

@Given('融资总监登录融管系统')
def step_serviceDirctorlogin(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.ser_director_manager,'123456','suzhou')

@When('打开【融资管理】→【融资喜报审批】→【待审批】页签选择相应的喜报并点击【订单详情】、点击【通过】按钮进行喜报审批')
def step_dirctorApprvChannalResult(context):
    global chan_appr_page
    chan_appr_page = ChannalResultApprovalPage(context.driver)
    chan_appr_page.approveChannalResult_Director(Data.cmp_name)
    functions.insert_img(context.driver, "chanl_result_approve_Director_"+current_time+".png")


@When('打开【财务】→【融资喜报审批】→【待审批】页签选择相应的喜报并点击【订单详情】、点击【通过】按钮进行喜报审批')
def step_finceApprvChannalResult(context):
    chan_appr_page.approveChannalResult_Finance(Data.cmp_name)
    functions.insert_img(context.driver, "chanl_result_approve_Finance_"+current_time+".png")

@When('打开【资源管理】→【融资业绩审批】→【待审批】页签选择相应的喜报并点击【订单详情】、点击【通过】按钮进行喜报审批')
def step_dataMngrApprvChanalResult(context):
    chan_appr_page.approveChannalResult_DataManager(Data.cmp_name)
    functions.insert_img(context.driver, "chanl_result_approve_DataManager_"+current_time+".png")
