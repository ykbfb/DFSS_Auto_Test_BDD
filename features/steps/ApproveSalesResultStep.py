import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ApproveSalesResultPage import SalesResultApprovalPage
from test_case.page_obj.base import *
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('打开【财务】→【销售喜报审批】页面，选择指定的销售喜报，点击【详情】按钮，输入“审批意见”点击【通过】按钮')
def step_finApproveSalesResult(context):
    chan_appr_page = SalesResultApprovalPage(context.driver)
    chan_appr_page.approveSalesResult_Finance(Data.sal_clt_name)
    functions.insert_img(context.driver, "sales_result_approve_Finance_"+current_time+".png")
    
@When('打开【资源管理】→【销售业绩审批】页面，选择指定销售喜报，点击【详情】按钮，输入“审批意见”点击【通过】按钮，修改喜报详情，点击【保存关闭并发送】')
def step_dataApproveSalesResult(context):
    chan_appr_page = SalesResultApprovalPage(context.driver)
    chan_appr_page.approveSalesResult_DataManager(Data.sal_clt_name)
    functions.insert_img(context.driver, "sales_result_approve_DataManager_"+current_time+".png")
