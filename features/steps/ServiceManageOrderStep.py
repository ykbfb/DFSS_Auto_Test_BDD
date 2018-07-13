import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ServiceOrderManagePage import ServiceManageOrderPage
from test_case.page_obj.base import *
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))


#================================================================================================================
@When('打开【融资订单管理】→【我的订单】→【待处理】页签，选择相应的主订单并点击【接单】按钮进行接单')
def step_acceptOrder(context):
    b = Page(context.driver)
    time.sleep(1)
    b.close_alert()
    global my_order
    my_order = ServiceManageOrderPage(context.driver)
    my_order.acceptOrder(Data.cmp_name)
    my_order.setWaitTime(2)

@Then('融服接单成功')
def step_verifyAcceptOrderSuccess(context):
    assert_that(my_order.verifyOrderAcceptSucess().strip(), equal_to('暂无查询到任何数据...'))
    functions.insert_img(context.driver, "myOrder_verifyOrderAcceptSucess_"+current_time+".png")

#=================================================================================================================
@When('打开【融资订单管理】→【我的订单】→【贷前调查】页签，选择相应的主订单并点击【转入专家测评】按钮')
def step_movetoExpert(context):
    my_order.moveToExpert(Data.cmp_name)
    my_order.setWaitTime(2)

@Then('订单进入专家测评')
def step_verifymovetoExpertSucess(context):
    context.assertEqual(my_order.verifyOrderMovetoExprtSucess().strip(), '暂无查询到任何数据...')
    functions.insert_img(context.driver, "myOrder_movetoexpert_"+current_time+".png")

#=================================================================================================================
@When('打开【融资订单管理】→【我的订单】→【专家测评】页签，选择相应的主订单并点击【转入机构寻访】按钮')
def step_movetoAgency(context):
    my_order.moveToAgencySearch(Data.cmp_name)
    my_order.setWaitTime(2)

@Then('订单进入机构寻访')
def step_verifymovetoAgencySucess(context):
    assert_that(my_order.verifyOrderMovetoAgencyResearchSucess().strip(), equal_to('暂无查询到任何数据...'))
    functions.insert_img(context.driver, "myOrder_movetoAgency_"+current_time+".png")
    my_order.setWaitTime(2)

#==================================================================================================================
@When('打开【融资订单管理】→【我的订单】→【机构寻访】页签，选择主订单并点击【智能融顾】按钮，选择相应的产品点击【发送意向单】')
def step_createAimOrder(context):
    my_order.createAimOrder(Data.cmp_name, Data.org_name, Data.prd_name)
    my_order.setWaitTime(2)

@Then('意向单创建成功')
def step_verifymovetoAgencySucess(context):
    assert my_order.verifyAimOrderCreateSucess().strip() is not '0/0/0/0/0'
    functions.insert_img(context.driver, "myOrder_createAimOrder_"+current_time+".png")
    my_order.setWaitTime(2)

#=====================================================================================================================
@When('打开【融资订单管理】→【我的订单】→【机构寻访】页签，选择主订单并点击【意向单管理】按钮，选择相应的意向单，点击【创建子订单】按钮进行子订单创建')
def step_createSubOrder(context):
    my_order.createSubOrder(Data.cmp_name, Data.credit_manager, Data.org_name)
    my_order.setWaitTime(2)
    functions.insert_img(context.driver, "myOrder_createSubsOrder"+current_time+".png")

@When('打开【融资订单管理】→【我的订单】→【贷前辅导】页签，选择子订单并点击【转入机构审批】按钮')
def step_subOrderMovetoOrgApproval(context):
    my_order.moveToOrgApproval(Data.cmp_name)
    my_order.setWaitTime(2)
    functions.insert_img(context.driver, "myOrder_moveSubsOrderToOrgApproval_"+current_time+".png")

@When('打开【融资订单管理】→【我的订单】→【机构审批】页签，选择子订单并点击【评价】按钮对信贷经理进行评价')
def step_estimateCreditManager(context):
    my_order.estimateCreditManager(Data.cmp_name)
    my_order.setWaitTime(2)
    functions.insert_img(context.driver, "myOrder_moveSubsOrderToOrgApproval_"+current_time+".png")

@When('机构审批{appv_status}：打开【融资订单管理】→【我的订单】→【机构审批】页签，选择子订单并点击【机构审批结果】按钮记录审批详情')
def step_OrgApprove(context,appv_status):
    context.appv_status = appv_status
    if appv_status == '不通过':
        my_order.orgApproveReject(Data.cmp_name)
        my_order.setWaitTime(2)
        functions.insert_img(context.driver, "myOrder_OrgApprove_reject_"+current_time+".png")
    elif appv_status == '通过':
        my_order.orgApprovePass(Data.cmp_name)
        my_order.setWaitTime(2)
        functions.insert_img(context.driver, "myOrder_OrgApprov_pass_"+current_time+".png")

@When('打开【融资订单管理】→【我的订单】→【机构审批】页签，选择子订单并点击【填写处理】按钮,选择成交并填写喜报详情')
def step_submitChanelResult(context):
    my_order.submitChanelResult(Data.cmp_name)
    my_order.setWaitTime(2)
    functions.insert_img(context.driver, "myOrder_ChanelResultSubmitSucess_"+current_time+".png")
