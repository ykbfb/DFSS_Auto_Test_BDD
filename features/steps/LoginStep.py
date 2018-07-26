import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj import loginPage, base
from test_case.models import myunit,functions,driver
from data.TestData import Data
from behave import *
from hamcrest import assert_that, equal_to
import time
from test_case.page_obj.loginPage import login
from data.TestData import Data

current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

@Given('打开登录页面: {loginurl}')
def step_openLoginPage(context,loginurl):
    context.loginurl = loginurl
    context.driver.get(loginurl)

@When('输入用户信息')
def step_enterLoginInfo(context):
    global  po
    po = loginPage.login(context.driver)
    po.user_login_verify(Data.sales,'123456','suzhou')

@Then('登录成功')
def step_loginSucess(context):
    functions.insert_img(context.driver,'LoginSucess_'+ current_time+'.png')
    assert_that(po.user_login_success().strip(),'颜芳')

@Then('关闭浏览器')
def quitBrowser(context):
    context.driver.quit()

#===============================================================================================================================
#   各角色登录
#===============================================================================================================================
@Given('销售顾问登录融管系统')
def step_loginSystem(context): #融资顾问登录融管系统
    lg = login(context.driver)
    lg.user_login_verify(Data.sales,'123456',Data.city)

@Given('销售经理登录融管系统')
def step_loginSystem(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.sales_manager,'123456',Data.city)

@Given('销售总监登录融管系统')
def step_loginSystem(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.sales_director,'123456',Data.city)

@Given('分公司财务登录融管系统')
def step_finLogin(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.finance_name,'123456',Data.city)

@Given('融服登录融管系统')
def step_serviceLogin(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.service_manager,'123456',Data.city)
    time.sleep(1)

@Given('融服总监登录融管')
def step_serviceDirctorLogin(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.ser_director_manager,'123456',Data.city)

@Given('分公司总经理登录融管')
def step_serviceDirctorLogin(context):
    lg = login(context.driver)
    lg.user_login_verify(Data.div_manager,'123456',Data.city)

@Given('数据专员登录融管')
def step_dataManagerLogin(context):
    lg = login(context.driver)
    lg.user_login_verify('longlixia', '123456', 'shanghai')

@Given('融资中心总经理登录融管')
def step_dataManagerLogin(context):
    lg = login(context.driver)
    lg.user_login_verify('zhangyu1087', '123456', 'shanghai')


@Given("总部应收会计登录融管系统")
def step_impl(context):
    lg = login(context.driver)
    lg.user_login_verify('duanxuesa', '123456', 'shanghai')


@Given("CFO登录融管系统")
def step_impl(context):
    lg = login(context.driver)
    lg.user_login_verify('lingju', '123456', 'shanghai')


@Given("总部付款出纳登录融管系统")
def step_impl(context):
    lg = login(context.driver)
    lg.user_login_verify('yangshuai', '123456', 'shanghai')

@Given("客服专员登录融管系统")
def step_impl(context):
    lg = login(context.driver)
    lg.user_login_verify('chenxiang5134', '123456', 'shanghai')

@Given("客服总监登录融管系统")
def step_impl(context):
    lg = login(context.driver)
    lg.user_login_verify('liujianlin', '123456', 'shanghai')










