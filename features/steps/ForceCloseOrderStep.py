import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ForceCloseOrderPage import ForceCloseOrderPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


@step("融资中心总经理登录融管")
def step_impl(context):
    lg = login(context.driver)
    lg.user_login_verify('zhangyu1087', '123456', 'shanghai')

@step("打开【其他】→【订单强制结案】页面，选择城市，选择需要结案的主订单，点击【结案】按钮")
def step_impl(context):
    close_order_page = ForceCloseOrderPage(context.driver)
    close_order_page.forceCloseOrder(Data.cmp_name)
    functions.insert_img(context.driver, "force_close_order_"+current_time+".png")