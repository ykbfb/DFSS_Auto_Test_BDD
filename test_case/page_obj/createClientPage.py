# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

# --==================================================================
# By 函数的属性：
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
# --==================================================================

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from data.TestData import Data
from .base import Page
from .loginPage import login
import time



class createClient(Page):
    click_rapid_nav_loc = (By.XPATH, '//*[@id="wnav"]/div[1]/div[1]/div[1]') #快捷操作
    click_createNew_loc = (By.XPATH, '//*[@id="wnav"]/div[1]/div[2]/ul/li[3]/div/a/span[2]') #新增客户
    newClient_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe' #新增页面的frame
    clientMobile_loc = (By.ID,'cell_input') #手机号码输入框
    checkMobile_loc = (By.XPATH,'//*[@id="divmobilevali"]/input[2]') #查重
    save_loc = (By.ID,'addCustomerAndAddRzsqsBtn') #保存按钮
    clt_exe_status_loc = '//*[@id="CLT_EXE_STATUS"]' #客户进程
    loan_area_loc = (By.XPATH,'//*[@id="area_1area"]/input[1]')#借款地区
    close_createPage_loc = (By.XPATH,'//*[@id="tabs"]/div[1]/div[3]/ul/li[2]/a[2]')

#==================================================================================================================
    # 打开【快捷操作】
    def open_rapidOperation(self):
        self.find_element(*self.click_rapid_nav_loc).click()
    #打开新增客户
    def open_newClient(self):
        self.find_element(*self.click_createNew_loc).click()
        self.driver.implicitly_wait(10)
    #切换frame
    def switchToNewClientFrame(self):
        self.switchToOneFrameByXpath(self.newClient_frame_loc)
    #输入手机号
    def inputMobile(self,mobile='10000000011'):
        self.mobile = mobile
        # self.find_element(*self.clientMobile_loc).clear()
        self.find_element(*self.clientMobile_loc).send_keys(mobile)
    #手机号码查重
    def checkMobileIsDuplicate(self):
        self.find_element(*self.checkMobile_loc).click()
    #保存客户
    def saveClient(self):
        self.find_element(*self.save_loc).click()
    #选择客户进程
    def selectCltExeStatus(self):
        self.getDropdownMenuByXpath(self.clt_exe_status_loc, 1)
    #选择借款地区
    def selectLoanArea(self):
        self.find_element(*self.loan_area_loc).click()
    #关闭创建页面
    def closeClientDetailPage(self):
        self.find_element(*self.close_createPage_loc).click()

    #验证客户是否创建成功
    client_mng_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#客户管理
    my_client_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[1]/div/a/span[2]/label')#我的订单
    clt_list_frame_loc = '//*[@id="tabs"]/div[2]/div[3]/div/iframe'
    clt_check_loc = (By.ID,'s_txtMyCltCheck')#模糊查询
    search_btn_loc = (By.XPATH,'//*[@id="cSearch"]')#查询按钮
    def checkClientCreateSuccess(self,phone):
        self.phone = phone
        self.switchToDefaultContent()
        self.click_element(*self.client_mng_loc)
        self.click_element(*self.my_client_loc)
        self.setWaitTime(10)
        self.switchToOneFrameByXpath(self.clt_list_frame_loc)
        self.input_value(self.clt_check_loc,phone)
        self.click_element(*self.search_btn_loc)

    #============================================================================================== 
    #创建客户
    def createNewClient(self,phone): #phone 新建客户手机号
        self.phone = phone
        self.open_rapidOperation()
        self.setWaitTime(10)
        self.open_newClient()
        self.switchToNewClientFrame()
        self.inputMobile(phone)
        self.checkMobileIsDuplicate()
        self.selectCltExeStatus()
        self.selectLoanArea()
        self.saveClient()
        time.sleep(1)

    # --===========================================================================================
    # 验证case的执行结果
    user_login_success_loc = (By.XPATH, '//*[@id="Main_Page"]/div[1]/div/div/span[2]/label')
    client_CheckExist_loc = (By.ID, 'vildatewords') #验证通过，手机号不存在： 验证通过； 该客户已经归属当前登录用户；
    clt_create_success_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[1]/td/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[3]/div') #列表页客户名称

    # 登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

    # 查询客户号码是否已存在
    def check_num_isExist(self):
        return self.find_element(*self.client_CheckExist_loc).text

    #验证客户是否创建成功
    def check_client_createSucess(self):
        return self.find_element(*self.clt_create_success_loc).text

