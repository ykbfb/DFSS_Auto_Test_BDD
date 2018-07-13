import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.CreateOrderPage import NewOrderPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('创建{order_type}销售订单：打开【销售订单管理】点击【创建销售订单】按钮，输入销售订单详情并提交')
def step_createSalesOrder(context,order_type):
    context.order_type = order_type
    global order
    order = NewOrderPage(context.driver)

    if order_type == '企业主' or order_type == '个体户':
        order.createOrderForCMP()
        functions.insert_img(context.driver, "myClient_orderCreateCMP"+current_time+".png")
    elif order_type == '工薪族' or order_type == '其他':
        order.createOrderForPerson()
        functions.insert_img(context.driver, "myClient_orderCreatePerson"+current_time+".png")
    else:
        print('销售订单类型错误')

@Then('销售订单创建成功')
def step_verifySalesOrderCreateSucess(context):
    order.clickOrderTab()
    order.setWaitTime(2)
    assert_that(order.verifySalesOrderCreateSucess().strip(), equal_to( Data.cmp_name))
    functions.insert_img(context.driver,"myClient_verifySalesOrderCreateSucess_"+current_time+".png")

