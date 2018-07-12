import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from test_case.models import functions
from test_case.page_obj import loginPage, base
from test_case.models import myunit,functions,driver
from data.TestData import Data
from behave import *
from hamcrest import assert_that, equal_to
from selenium import webdriver
import time

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