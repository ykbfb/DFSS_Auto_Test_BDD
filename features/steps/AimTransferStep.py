import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.AimTransferPage import AimTransPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))


@When('打开【我的客户】，列表中选择客户，在【合同管理】中点击【转业绩】按钮，并填写转业绩详情,提交')
def step_createAimTransfer(context):
    aim_trans = AimTransPage(context.driver)
    aim_trans.createAimTransfer()
    functions.insert_img(context.driver, "aim_transfer_"+current_time+".png")

@When('打开【综合管理】→【意向金转业绩审批】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮')
def step_approveAimAmtTransfer_SalesManager(context):
    aim_trans = AimTransPage(context.driver)
    aim_trans.approveAimTransfer(Data.lnk_moblie)
    functions.insert_img(context.driver, "approve_aim_transfer_SalesManager_"+current_time+".png")
    
@When('打开【销售管理】→【意向金转业绩审批-总监】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮')
def step_approveAimTransfer_Director(context):
    aim_trans = AimTransPage(context.driver)
    aim_trans.approveAimTransfer_Director(Data.lnk_moblie)    
    functions.insert_img(context.driver, "approve_aim_transfer_Director_"+current_time+".png")


@When('打开【销售管理】→【意向金转业绩审批-分总】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮')
def step_approveAimTransfer_DivManager(context):
    aim_trans = AimTransPage(context.driver)
    aim_trans.approveAimTransfer_DivManager(Data.lnk_moblie)
    functions.insert_img(context.driver, "approve_aim_transfer_DivManager_"+current_time+".png")
    
@When('打开【资源管理】→【意向金转业绩审批】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮，喜报详情页面点击【保存关闭并发送】按钮')
def step_approveAimTransfer_DataManager(context):
    aim_trans = AimTransPage(context.driver)
    aim_trans.approveAimTransfer_DataManager(Data.lnk_moblie)
    functions.insert_img(context.driver, "approve_aim_transfer_DataManager_"+current_time+".png")