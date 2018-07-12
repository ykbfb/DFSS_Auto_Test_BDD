import unittest, sys
sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ApproveChannelResultPage import ChannalResultApprovalPage
from test_case.page_obj.base import *
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@Given('融资总监登录融管系统')
def step_serviceDirctorlogin(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.ser_director_manager,'123456','suzhou')

@When('')
def step_(context):
    pass


