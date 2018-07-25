import sys
sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.createClientPage import createClient
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@When('创建大项目新客户')
def step_createNewClient(context):
    create_client = createClient(context.driver)
    create_client.createNewClient(Data.move_client_phone)

@When('打开【客户管理】→【我的客户】，列表页选择客户，点击有上角【划转至大项目部】按钮，选择【接收人员】，填写“划转备注”并点击【保存】按钮')
def step_moveToBigProject(context):
    my_client = myClient(context.driver)
    my_client.gotoMyClientList_All(Data.move_client_phone)
    my_client.moveClientToBigProject()
    functions.insert_img(context.driver, "deleteClientByRightClick_"+current_time+".png")