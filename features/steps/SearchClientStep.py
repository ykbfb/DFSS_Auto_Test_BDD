import sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.page_obj.myClientsPage import myClient
from data.ReadTestData import Data
#from data.TestData import Data
from behave import *

data = Data()

@When('查询客户')
def step_searchClient(context):
    global  mc
    mc = myClient(context.driver)
    mc.gotoMyClientList_All(Data.lnk_moblie)
    mc.setWaitTime(2)

@When('查询销售订单客户')
def step_searchClient(context):
    global  mc
    mc = myClient(context.driver)
    mc.gotoMyClientList_All(data.getCaseInitClient('创建销售订单')['lnk_mobile'])
    mc.setWaitTime(2)