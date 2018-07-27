import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.createSalesBragainResultPage import SalesBargainPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

@When('打开【流程管理】→【新销售订单管理】，选择“可填喜报”的销售订单，打开订单详情，点击【新增】按钮创建销售喜报')
def step_createSalesResult(context):
    sales_results = SalesBargainPage(context.driver)
    sales_results.CreateSalesBargainResult(Data.sal_clt_name)
    functions.insert_img(context.driver, "create_Sales_Result_"+current_time+".png")