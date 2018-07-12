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

from selenium.webdriver.common.by import By
from .base import Page
import time
import random

class NewIntviewPage(Page):
    #邀约记录
    clt_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    intview_tab_loc = (By.XPATH,'//*[@id="bottomTabs_yyjl"]/a')
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    def clickIntviewTab(self):
        self.find_element(*self.intview_tab_loc).click()
        self.scrollToElement('id',self.botom_frame_loc) # 页面跳转到底部【邀约记录】所在的位置
        self.switchToOneFrame(self.botom_frame_loc) # 切换到底部【客户详情】的iframe

#=================================================================================================================
    # 创建邀约详情
    newIntview_loc = (By.XPATH,'//*[@id="btnAddView"]/span/span')    #新增邀约
    inview_result_loc = (By.ID,'rdCome')#邀约结果--已来访
    finbook_code_loc = (By.ID,'txtBook')#需求书编号
    act_time_loc = 'txtShiji'#时间来访时间
    start_time_loc = 'txtStart'#开始时间
    end_time_loc = 'txtEnd'#结束时间
    # main_person_loc = 'txtMain'#主谈人
    main_person_loc = (By.XPATH,'//*[@id="tbMemo"]/tbody/tr[3]/td[1]/img')#主谈人
    mov_main_person_loc = '//*[@id="main"]/div[1]/table/tbody/tr[3]/td[1]'
    pop_main_person1_loc =(By.XPATH, '//*[@id="main"]/div[1]/table/tbody/tr[3]/td[1]')
    sel_main_person_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[3]/td[1]/input')
    # sub_person_loc = 'txtSub'#辅谈人
    sub_person_loc = (By.XPATH,'//*[@id="tbMemo"]/tbody/tr[3]/td[2]/img')#辅谈人

    pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"#弹窗frame
    frazzy_search_loc = (By.ID,'txt')#模糊查询
    search_btn_loc = (By.ID,'btnCheck')#查询

    talk_result_loc = 'selMain'#邀约结果
    sub_talk_result_loc = 'selS'
    ss_sub_talk_result_loc = 'selF'

    # evelu_expert_loc = 'txtEvalExpert'#测评专家
    # proj_maneger_loc = 'txtProManager'#项目经理
    evelu_expert_loc = (By.XPATH,'//*[@id="tbMemo"]/tbody/tr[4]/td[1]/img')#测评专家
    proj_maneger_loc = (By.XPATH,'//*[@id="tbMemo"]/tbody/tr[4]/td[2]/img')#项目经理


    inview_place_loc = 'selViewPlace'#面谈地点
    intview_memo_loc = (By.ID,'txtViewMemo')#面谈记录
    save_intview_loc = (By.ID,'btnSave')#保存

    #创建已来访邀约
    def createIntview(self):
        self.clickIntviewTab()
        self.click_element(*self.newIntview_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.inview_result_loc)
        self.input_value(self.finbook_code_loc,random.randint(1000000, 9999999))
        self.getDateTimePicker(self.act_time_loc,'2018-03-10 10:00:00')
        self.getDateTimePicker(self.start_time_loc,'2018-03-10 11:00:00')
        self.getDateTimePicker(self.end_time_loc,'2018-03-10 12:00:00')
        # self.inputForReadonlyEle(self.main_person_loc,'颜芳[AA5771]')
        # self.inputForReadonlyEle(self.sub_person_loc,'颜芳[AA5771]')
        self.click_element(*self.main_person_loc)
        self.selectEmp('AA5771')
        self.click_element(*self.sub_person_loc)
        self.selectEmp('AA4218')

        self.getDropdownMenuById(self.talk_result_loc,1)
        self.getDropdownMenuById(self.sub_talk_result_loc,1)
        self.getDropdownMenuById(self.ss_sub_talk_result_loc,1)

        # self.inputForReadonlyEle(self.evelu_expert_loc,'颜芳[AA5771]')
        # self.inputForReadonlyEle(self.proj_maneger_loc,'李伟伟[AA2966]')
        self.click_element(*self.evelu_expert_loc)
        self.selectEmp('AA1128')
        self.click_element(*self.proj_maneger_loc)
        self.selectEmp('AA0284')


        self.getDropdownMenuById(self.inview_place_loc,1)
        self.input_value(self.intview_memo_loc,'自动化测试：创建邀约')
        self.click_element(*self.save_intview_loc)

     #选择谈单人--弹出窗口
    def selectEmp(self,emp_code):
        self.emp_code = emp_code
        self.switchToParentFrame()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_frame_loc)
        self.input_value(self.frazzy_search_loc, emp_code)
        self.scrollToElement('xpath', self.mov_main_person_loc)
        self.click_element(*self.pop_main_person1_loc)
        self.setWaitTime(10)
        self.click_element(*self.sel_main_person_loc)
        time.sleep(1)
        #关闭弹窗，切回原来窗口
        self.switchToOneFrameByXpath(self.clt_list_frame_loc) #跳转到列表页iframe 位置
        self.scrollToElement('id', self.botom_frame_loc) # 页面跳转到底部【邀约记录】所在iframe的位置
        self.switchToOneFrame(self.botom_frame_loc)

#================================================================================================================
    #创建DC邀约
    def createIntview_DC(self):
        self.clickIntviewTab()
        self.click_element(*self.newIntview_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.save_intview_loc)

#=================================================================================================================
    #编辑DC过的邀约
    modify_intview_loc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[1]/div/div[2]')#修改
    def modifyIntview(self):
        self.clickIntviewTab()
        self.click_element(*self.modify_intview_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.inview_result_loc)
        self.input_value(self.finbook_code_loc,random.randint(1000000, 9999999))
        self.getDateTimePicker(self.act_time_loc,'2018-03-10 10:00:00')
        self.getDateTimePicker(self.start_time_loc,'2018-03-10 11:00:00')
        self.getDateTimePicker(self.end_time_loc,'2018-03-10 12:00:00')
        # self.inputForReadonlyEle(self.main_person_loc,'颜芳[AA5771]')
        # self.inputForReadonlyEle(self.sub_person_loc,'颜芳[AA5771]')
        self.click_element(*self.main_person_loc)
        self.selectEmp('AA5771')
        self.click_element(*self.sub_person_loc)
        self.selectEmp('AA4218')


        self.getDropdownMenuById(self.talk_result_loc,1)
        self.getDropdownMenuById(self.sub_talk_result_loc,1)
        self.getDropdownMenuById(self.ss_sub_talk_result_loc,1)

        # self.inputForReadonlyEle(self.evelu_expert_loc,'颜芳[AA5771]')
        # self.inputForReadonlyEle(self.proj_maneger_loc,'李伟伟[AA2966]')
        self.click_element(*self.evelu_expert_loc)
        self.selectEmp('AA1128')
        self.click_element(*self.proj_maneger_loc)
        self.selectEmp('AA0284')
        self.getDropdownMenuById(self.inview_place_loc,1)
        self.input_value(self.intview_memo_loc,'自动化测试：修改邀约')
        self.click_element(*self.save_intview_loc)

    #创建完之后， 返回邀约【待审】页面
    iv_append_approve_loc = (By.ID,'1')#待审
    def gobacktoIntviewList(self):
        self.switchToParentFrame()
        self.clickIntviewTab()
        self.click_element(*self.iv_append_approve_loc)
        time.sleep(1)

    #DC邀约创建完之后， 返回邀约【草稿】页面
    iv_draft_loc = (By.ID,'0')#草稿
    def gobacktoDraftIntviewList(self):
        self.switchToParentFrame()
        self.clickIntviewTab()
        self.click_element(*self.iv_draft_loc)
        time.sleep(1)

# ============================================================================================
    # 验证case的执行结果：  未完待续
    book_info_memo_loc = (By.XPATH,'//*[@id="ViewList"]/div/div[3]/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[16]/div')#备注
    #校验已来访邀约是否创建成功
    def verifyIntviewCreateSucess(self):
        return  self.find_element(*self.book_info_memo_loc).text

    #校验DC邀约是否创建成功
    modify_btn_loc = (By.XPATH,'//*[@id="datagrid-row-r2-2-0"]/td[1]/div/div[2]')#修改
    def verifyDCIntviewCreateSucess(self):
        #return  self._isElementExist(self.modify_btn_loc)
        return  self.find_element(*self.modify_btn_loc).text

