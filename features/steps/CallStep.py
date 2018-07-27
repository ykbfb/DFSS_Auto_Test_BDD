
import unittest, sys
sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.CallDetailPage import CallDetailPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

@When('进入【我的客户】列表页，选择客户双击，并在呼叫详情页输入呼叫详情，点击【保存】')
def step_dubleClickCall(context):
    global  call_page
    call_page = CallDetailPage(context.driver)
    call_page.callClient()
    functions.insert_img(context.driver, "DoubleClickCall_"+current_time+".png")

@When('进入【我的客户】列表页，选择客户鼠标右键，点击【呼叫】按钮，并在呼叫详情页输入呼叫详情，点击【保存】')
def step_rightClickCall(context):
    call_page.rigthClickCall()
    functions.insert_img(context.driver, "RightClickCall_"+current_time+".png")

@When('进入【我的客户】列表页，选择客户点击【呼叫】按钮，并在呼叫详情页输入呼叫详情，点击【保存】')
def step_callFromList(context):
    call_page.callFromList()
    functions.insert_img(context.driver, "CallFromList_" + current_time + ".png")

@When('进入【我的客户】列表页，选择客户点击【批量呼叫】按钮，并在呼叫详情页输入呼叫详情，点击【保存】')
def step_callFromList(context):
    call_page.multCall()
    functions.insert_img(context.driver, "MultCallFromList_" + current_time + ".png")
