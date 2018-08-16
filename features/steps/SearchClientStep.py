import sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.page_obj.myClientsPage import myClient
from data.TestData import Data
from behave import *

@When('查询客户')
def step_searchClient(context):
    global  mc
    mc = myClient(context.driver)
    mc.gotoMyClientList_All(Data.lnk_moblie)
    mc.setWaitTime(2)