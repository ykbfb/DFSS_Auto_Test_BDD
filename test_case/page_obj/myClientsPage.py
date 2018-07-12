#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

#--==================================================================
#By 函数的属性：
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
#--==================================================================

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
import time

class myClient(Page):            

    click_client_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]') #客户管理
    click_myClient_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[1]/div/a/span[2]')#我的客户
    client_lisit_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    mainframe_loc = '//*[@id="tabs"]/div[2]/div[1]/div/iframe'
    click_All_loc = (By.XPATH,'//*[@id="tabType"]/div[2]/ul/li[2]/a') #我的客户-全部
    search_contract_starttime_loc = (By.ID,"s_dealTimeBegin")
    search_contract_endtime_loc = (By.ID,"s_dealTimeEnd")    
    invit_status_loc= (By.XPATH,'//*[@id="div_cbXieYi"]/div/a')
    invit_status_select_loc= (By.XPATH,'//*[@id="div_cbXieYi"]/div/div/ul/li[1]')
      
    search_text_loc = (By.ID,"s_txtMyCltCheck")
    clientCheckBox_loc = (By.XPATH,'//*[@id="datagrid-row-r3-2-0"]/td[1]') #客户列表中的checkbox
    
    client_type_loc = (By.XPATH,'//*[@id="div_cmbMyCltType"]/div/a')
    client_type_select_loc = (By.XPATH,'//*[@id="div_cmbMyCltType"]/div/a/span')

    client_process_loc = (By.XPATH,'//*[@id="div_cmbExeRe"]/div/a')
    client_process_select_loc = (By.XPATH,'//*[@id="div_cmbExeRe"]/div/a/span')

    client_flag_loc = (By.XPATH,'//*[@id="div_keywords"]/div/a')
    client_flag_select_loc = (By.XPATH,'//*[@id="div_keywords"]/div/a/span') 
   
    client_grade_loc = (By.XPATH,'//*[@id="div_cmbCltGrade"]/div/a')
    client_grade_select_loc = (By.XPATH,'//*[@id="div_cmbCltGrade"]/div/a/span')  
    
    client_area_loc = (By.XPATH,'//*[@id="div_cmbMyCltArea"]/div/a')
    client_area_select_loc = (By.XPATH,'//*[@id="div_cmbMyCltArea"]/div/a/span')
    
    client_regist_starttime_loc = (By.ID,'s_webCreateTimeBegin')
    client_regist_endtime_loc = (By.ID,'s_webCreateTimeEnd')
    is_addwechat_loc = (By.ID,'s_cbIsWechatFriend')
    is_recall_loc = (By.ID,'s_cbNotHasRecall')
    client_search_loc = (By.ID,'cSearch')
    clear_search_loc = (By.ID,'cClear')
    move_to_client_loc = '//*[@id="datagrid-row-r4-2-0"]/td[3]/div'   #客户列表页
    
    duble_click_search_loc = (By.NAME, 'SelectAll')
    modify_loc = (By.XPATH,'//*[@id="contextMenuId_khxg"]/div')

#=======修改联系人=================================================================================================
    clt_lnk_loc = (By.ID,'bottomTabs_lxr') #联系人 菜单
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    modify_button_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[1]/div/div') #修改按钮
    lnk_name_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[3]/div/table/tbody/tr/td/input')#联系人姓名
    lnk_duty_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[6]/div/table/tbody/tr/td/input')#职务
    lnk_role_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[7]/div/table/tbody/tr/td/input')#角色
    lnk_extent_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[11]/div/table/tbody/tr/td/input')#传真
    lnk_email_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[12]/div/table/tbody/tr/td/input') #邮箱
    save_lnk_loc = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/div[1]')#保存


    #点击【客户管理菜单】
    def open_manageClient(self):
        self.find_element(*self.click_client_manage_loc).click()

    #点击我的客户
    def open_myClient(self):
        self.find_element(*self.click_myClient_nav_loc).click()

    def switchToBack(self):
        self.switchToDefaultContent()

    #切换到客户列表页
    def switchTomainPage(self):
        self.switchToOneFrameByXpath(self.mainframe_loc)
    def switchToClientList(self):
        self.switchToOneFrameByXpath(self.client_lisit_loc)

    def goto_allClient(self):
        self.find_element(*self.click_All_loc).click()
        self.driver.implicitly_wait(10)
    #合同开始时间建查询
    def search_contract_starttime(self,s_id,start_time_value):
        #将时间控件字段置为空
        jStr1 = "$('input[id=" 
        jStr2 = "]').attr('readonly',false)"
        js = jStr1 + s_id + jStr2      
        self.script(js)  
        self.find_element(*self.search_contract_starttime_loc).send_keys(start_time_value)
    #结束日期    
    def search_contract_endtime(self,e_id,end_time_value):
        #将时间控件字段置为空
        jStr1 = "$('input[id=" 
        jStr2 = "]').attr('readonly',false)"
        js = jStr1 + e_id + jStr2      
        self.script(js)  
        self.find_element(*self.search_contract_endtime_loc).send_keys(end_time_value)
    
    #线下邀约状态
    def search_invit_status(self):
        self.find_element(*self.invit_status_loc).click()
        self.find_element(*self.invit_status_select_loc).click()
    
    #模糊查询   
    def fuzzy_search(self,value):
        self.find_element(*self.search_text_loc).send_keys(value)
        
    #客户类型   
    def search_client_type(self):
        self.find_element(*self.client_type_loc).click() 
        self.find_element(*self.client_type_select_loc).click() 
        
    #客户进程    
    def search_process_status(self): 
#         self.find_element(*self.client_process_loc).select_by_index(process_status)
        self.find_element(*self.client_process_loc).click()
        self.find_element(*self.client_process_select_loc).click()        
        
    #客户标签    
    def search_client_flag(self): 
#         self.find_element(*self.client_flag_loc).select_by_index(client_flag)
        self.find_element(*self.client_flag_loc).click()
        self.find_element(*self.client_flag_select_loc).click()
    #客户等级    
    def search_client_grade(self): 
#         self.find_element(*self.client_grade_loc).select_by_index(client_grade)
        self.find_element(*self.client_grade_loc).click()
        self.find_element(*self.client_grade_select_loc).click()
    #客户地区    
    def search_client_area(self): 
#         self.find_element(*self.client_area_loc).select_by_index(client_area)
        self.find_element(*self.client_area_loc).click()
        self.find_element(*self.client_area_select_loc).click()
    
    def search_client_regist_starttime(self,rs_id,regist_start_time_value):
        #将时间控件字段置为空
        jStr1 = "$('input[id=" 
        jStr2 = "]').attr('readonly',false)"
        js = jStr1 + rs_id + jStr2      
        self.script(js)  
        self.find_element(*self.client_regist_starttime_loc).send_keys(regist_start_time_value)
    #结束日期    
    def search_client_regist_endtime(self,re_id,regist_end_time_value):
        #将时间控件字段置为空
        jStr1 = "$('input[id=" 
        jStr2 = "]').attr('readonly',false)"
        js = jStr1 + re_id + jStr2      
        self.script(js)  
        self.find_element(*self.client_regist_endtime_loc).send_keys(regist_end_time_value)
        
    #是否添加微信
    def search_isAddWechat(self):
        self.find_element(*self.is_addwechat_loc).click()
    
    #无回访记录
    def search_is_recall(self):
        self.find_element(*self.is_recall_loc).click()  
    
    #查询
    def action_search(self):
        self.find_element(*self.client_search_loc).click()
    
    #清空记录
    def clear_search(self):
        self.find_element(*self.clear_search_loc).click()

    #移动元素
    def moveToClient(self):
        self.scrollToElement('xpath',self.move_to_client_loc)

     #客户列表中选择指定客户
    def selectClient(self):
        self.find_element(*self.clientCheckBox_loc).click()

    #移动frame切换到客户列表
    def switchToClientListFrame(self):
        self.switchToOneFrameByXpath(self.client_lisit_loc)
    
    #双击选中的客户: 打开拨打详情
    def dubleClickClient(self):
        clt_call_detail=self.find_element(*self.duble_click_search_loc)
        ActionChains(self.driver).double_click(clt_call_detail).perform()  #双击

    #修改客户
    def modifyClient(self):
        modify = self.find_element(*self.duble_click_search_loc) 
        ActionChains(self.driver).context_click(modify).perform() #右击
        self.find_element(*self.modify_loc).click()

#==============================修改联系人=======================================================================
    #点击【联系人】
    def gotoLnkMan(self):
        self.find_element(*self.clt_lnk_loc).click()
    #切换到底部客户详情
    def clientDetailTable(self):
        self.scrollToElement('id', self.botom_frame_loc)  # 页面跳转到底部【客户详情】所在的位置--相当于滚动条
        self.switchToOneFrame(self.botom_frame_loc)  # 切换到底部【客户详情】的iframe
    # 点击修改按钮
    def modifyClientLnkButton(self):
        self.find_element(*self.modify_button_loc).click()
    #输入联系人姓名
    def inputLnkName(self,value):
        self.value = value
        self.find_element(*self.lnk_name_loc).clear()
        self.find_element(*self.lnk_name_loc).send_keys(value)

    #输入联系人职务
    def inputLnkDuty(self,value):
        self.value = value
        self.find_element(*self.lnk_duty_loc).clear()
        self.find_element(*self.lnk_duty_loc).send_keys(value)
    #输入联系人角色
    def inputLnkRole(self,value):
        self.value = value
        self.find_element(*self.lnk_role_loc).clear()
        self.find_element(*self.lnk_role_loc).send_keys(value)
    #输入联系人传真
    def inputLnkExtent(self,value):
        self.value = value
        self.find_element(*self.lnk_extent_loc).clear()
        self.find_element(*self.lnk_extent_loc).send_keys(value)
    #输入联系人邮箱
    def inputLnkEmail(self,value):
        self.value = value
        self.find_element(*self.lnk_email_loc).clear()
        self.find_element(*self.lnk_email_loc).send_keys(value)
    #保存联系人信息
    def saveLnkManDetail(self):
        self.find_element(*self.save_lnk_loc).click()

    #返回上一frame
    def backMainPage(self):
        self.switchToParentFrame()
        # self.switchToDefaultContent()
    def switchToClientList2(self):
        self.switchToOneFrameByXpath(self.client_lisit_loc)

    clt_mng_nenu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')
    def gobackToMyClient(self):
        self.switchToDefaultContent()
        #self.click_element(*self.clt_mng_nenu_loc)

#--===========================================================================================
#'''打开客户列表-【全部】通过模糊查询查询指定客户的公共方法'''
    def gotoMyClientList_All(self,searchValue):
        self.searchValue = searchValue
        self.open_myClient()
        time.sleep(1)
        self.switchToClientList()
        self.goto_allClient()
        self.fuzzy_search(self.searchValue) #模糊查询
        self.action_search()
        self.moveToX(800, 300)
        self.selectClient()
        time.sleep(1)

    #修改联系人公共方法
    def modifyLnkMan(self,name,duty,role,extent,email):
        self.name = name
        self.duty = duty
        self.role = role
        self.extent = extent
        self.email = email

        self.gotoLnkMan()
        self.clientDetailTable()
        self.modifyClientLnkButton()
        self.inputLnkName(name)
        self.inputLnkDuty(duty)
        self.inputLnkRole(role)
        self.inputLnkExtent(extent)
        self.inputLnkEmail(email)
        self.saveLnkManDetail()

    #划转至大项目部
    move_bigproj_loc = (By.ID,'operateItems_hzzdxmb')#划转至大项目部
    pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    select_emp_loc = 'sltEmployee'#接收人员
    move_memo_loc = (By.ID,'txtRemark')#划转备注
    save_btn_loc = (By.ID,'btnSave')#保存

    def moveClientToBigProject(self):
        self.click_element(*self.move_bigproj_loc)
        time.sleep(1)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_frame_loc)
        self.getDropdownMenuById(self.select_emp_loc,1)
        self.input_value(self.move_memo_loc,'自动化测试：客户划转至大客户项目部')
        self.click_element(*self.save_btn_loc)
        time.sleep(1)
        self.close_alert()

 #============================================================================================
    #验证case的执行结果    
    user_login_success_loc = (By.XPATH,'//*[@id="Main_Page"]/div[1]/div/div/span[2]/label') 
    link_name_loc = (By.XPATH,'//*[@id="datagrid-row-r2-2-0"]/td[5]/div')
    fuzzy_search_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[1]/td/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[4]/div') #列表页客户名称

    regist_time_loc = (By.XPATH,'//*[@id="datagrid-row-r14-2-0"]/td[5]/div')
    addWeChat_loc = (By.XPATH,'//*[@id="datagrid-row-r15-2-0"]/td[5]/div')
    noRecall_loc = (By.XPATH,'//*[@id="datagrid-row-r16-2-0"]/td[5]/div')

    modify_lnk_name_loc = (By.XPATH,'//*[@id="LnkManList"]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[3]/div') #修改联系人页面--姓名
    
    #登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
    #合同归档时间查询成功
    def search_by_conAchiveTime(self):
        return self.find_element(*self.link_name_loc).text

    #模糊查查成功
    def search_by_fuzzy(self):
        return self.find_element(*self.fuzzy_search_loc).text

    #注册时间
    def search_by_registTime(self):
        return self.find_element(*self.regist_time_loc).text

    
    #已添加微信查询成功
    def search_by_addWechat(self):
        return self.find_element(*self.addWeChat_loc).text

        
    #无回访记录查询成功
    def search_by_noRecall(self):
        return self.find_element(*self.noRecall_loc).text


    #校验修改联系人
    def verify_modify_lnkMan(self):
        return self.find_element(*self.modify_lnk_name_loc).text
        