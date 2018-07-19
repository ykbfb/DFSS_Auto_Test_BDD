import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.ShareClientPage import ShareClientPage
from test_case.page_obj.createClientPage import createClient
from test_case.page_obj.CallDetailPage import CallDetailPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('创建共享客户{client_no}')
def step_createShareClient(context,client_no):
    context.client_no = client_no
    global nc
    nc = createClient(context.driver)
    nc.setWaitTime(2)
    nc.open_rapidOperation()
    nc.open_newClient()
    nc.switchToNewClientFrame()
    if client_no == '1':
        nc.inputMobile(Data.share_phone1)
    elif client_no == '2':
        nc.inputMobile(Data.share_phone2)
    elif client_no == '3':
        nc.inputMobile(Data.share_phone3)
    else:
        print('输入的客户编号错误，请确认输入的编号为： 1,2,3')
    nc.checkMobileIsDuplicate()
    time.sleep(1)
    assert_that(nc.check_num_isExist().strip(), equal_to('验证通过'))
    functions.insert_img(context.driver, "shareClient_isNotExist_" + current_time + ".png")
    time.sleep(1)
    nc.selectCltExeStatus()
    nc.selectLoanArea()
    nc.saveClient()
    time.sleep(1)
    functions.insert_img(context.driver, "shareClient_isCreateSuccess_" + current_time + ".png")  # 客户详情

@When('查询共享客户{client_no}')
def step_searchShareClient(context,client_no):
    context.client_no = client_no
    global  mc
    mc = myClient(context.driver)
    if client_no == '1':
        mc.gotoMyClientList_All(Data.share_phone1)
    elif client_no == '2':
        mc.gotoMyClientList_All(Data.share_phone2)
    elif client_no == '3':
        mc.gotoMyClientList_All(Data.share_phone3)
    else:
        print('输入的客户编号错误，请确认输入的编号为： 1,2,3')
    mc.setWaitTime(2)

@When('打开【客户管理】→【我的客户】，在客户列表页选择客户，单击鼠标【右键】，点击【共享】按钮，填写“共享原因”，将客户释放到公海')
def step_rigthClickShareClient(context):
    global  share_page
    share_page = ShareClientPage(context.driver)
    share_page.shareClientByRigthClick()
    functions.insert_img(context.driver, "rightClickShareClient_"+current_time+".png")

@When('打开【客户管理】→【我的客户】，在客户列表页选择客户，点击列表右上角【共享】按钮，填写“共享原因”，将客户释放到公海')
def step_listShareClient(context):
    share_page = ShareClientPage(context.driver)
    share_page.shareClientFromList()
    functions.insert_img(context.driver, "listShareClient_"+current_time+".png")

@When('打开【客户管理】→【我的客户】，在客户列表页选择客户，单击【呼叫】按钮，填写回访信息，点击【共享】填写“共享原因”，将客户释放到公海')
def step_callPageShare(context):
    call_page = CallDetailPage(context.driver)
    call_page.openCallDetailPage()  # 呼叫页面共享
    share_page = ShareClientPage(context.driver)
    share_page.shareClientFromCallPage()
    functions.insert_img(context.driver, "callDetailPageShareClient_"+current_time+".png")