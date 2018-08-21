import sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj.SalseManagerAsignOrderPage import SaleseOrderAsignPage
from data.ReadTestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
data = Data()

@When('打开【销售管理】→【销售订单处理操作】→【待接单】点击【接单】按钮进行接单')
def step_acceptSalesOrder(context):
    global  salse_order
    salse_order = SaleseOrderAsignPage(context.driver)
    salse_order.acceptSalseOrder(data.getCaseInitClient('销售订单派单')['cmp_name'])
    salse_order.setWaitTime(2)
    functions.insert_img(context.driver, "SalesOrderAccept"+current_time+".png")

@Then('销售订单接单成功')
def step_verifySalesOrderAcceptSucess(context):
    assert_that(salse_order.verifySalesOrderAcceptSucess().strip(), equal_to('暂无查询到任何数据...'))
    functions.insert_img(context.driver, current_time + "__VerifySalesOrderAccept.png")

@When('打开【销售管理】→【销售订单处理操作】→【待派单】点击【派单】按钮并选择相应的产品线进行派单')
def step_asignSalseOrder(context):
    salse_order.asignSalesOrder(data.getCaseInitClient('销售订单派单')['cmp_name'])
    salse_order.setWaitTime(2)
    functions.insert_img(context.driver, "myClient_fuzzysearch"+current_time+".png")

@Then('销售订单派单成功')
def step_verifySalesOrderAsignSucess(context):
    assert str(salse_order.verifySalesOrderAsignedSuccess().strip()).split('.')[0] in data.getCaseInitClient('销售订单派单')['cmp_name']
    functions.insert_img(context.driver,"VerifySalesOrderAsignedSucess"+current_time+".png")
