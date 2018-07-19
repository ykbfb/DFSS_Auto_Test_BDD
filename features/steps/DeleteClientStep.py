# language: zh-CN
import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.ShareClientPage import ShareClientPage
from test_case.page_obj.createClientPage import createClient
from test_case.page_obj.DeleteClientPage import DeleteClientPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))


@When('选择客户，点击鼠标右键，选择【删除】按钮删除客户')
def step_deleteClientByRightClieck(context):
    del_page = DeleteClientPage(context.driver)
    del_page.deleteClientByRigthClick()
    functions.insert_img(context.driver, "deleteClientByRightClick_"+current_time+".png")

@When('选择客户，点击列表页右上角的【删除】按钮删除客户')
def step_deleteClientFromList(context):
    del_page = DeleteClientPage(context.driver)
    del_page.deleteClientFromList()
    functions.insert_img(context.driver, "deleteClientFromList_"+current_time+".png")
