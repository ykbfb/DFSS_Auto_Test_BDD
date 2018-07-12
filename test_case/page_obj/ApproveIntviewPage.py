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
from .base import Page
import time

class ApproveIntviewPage(Page):
    # 销售经理邀约审批
    intview_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]') #综合管理
    intview_appv_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[2]/div/a/span[2]')#邀约审批
    intview_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    intview_status_loc = (By.ID,'Radio1') #待审批
    need_appv_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[1]') #未归档
    intview_appv_btn_loc = (By.XPATH,'//*[@id="div_audit"]/a')#邀约审批

    intview_appr_memo_loc = (By.ID,'txtOpinion')#审批页面批注
    confirm_btn_loc = (By.CLASS_NAME,'layui-layer-btn0')#确定
    pop_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确定


    def gotoNeedApproveList(self):
        '''到邀约待审批列表页'''
        time.sleep(2)
        self.click_element(*self.intview_nav_loc)
        self.click_element(*self.intview_appv_menu_loc)
        self.setWaitTime(20)
        time.sleep(2)
        self.switchToOneFrameByXpath(self.intview_list_frame_loc)
        self.click_element(*self.intview_status_loc)
        time.sleep(2)

#================================================================================
    def approveIntview(self):
        '''邀约审批'''
        self.gotoNeedApproveList()
        self.click_element(*self.need_appv_loc)
        time.sleep(2)
        self.click_element(*self.intview_appv_btn_loc)
        self.switchWindow()
        self.input_value(self.intview_appr_memo_loc,'自动化测试：邀约审批')
        self.click_element(*self.confirm_btn_loc)
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.pop_confirm_loc)

    appv_complete_loc = (By.ID,'Radio2')#完成
    submit_starttime_loc = 'txtStartTime'#开始时间
    submit_endtime_loc = 'txtEndTime'#结束时间
    search_btn_loc = (By.ID,'btnSearch')#查询
    def gotoIntviewCompleteList(self):
        '''审批完成页'''
        self.click_element(*self.appv_complete_loc)
        time.sleep(1)
        self.getDateTimePicker(self.submit_endtime_loc,time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.getDateTimePicker(self.submit_endtime_loc,time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.click_element(*self.search_btn_loc)

# ============================================================================================
    intview_DC_loc = 'btnDoubleCalling'
    intview_DC_btn_loc = (By.ID,'btnDoubleCalling')#DC按钮
    pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    DC_success_loc = (By.ID,'doubleCalling')#DC成功
    DC_memo_loc = (By.ID,'txtDoubleCallingMemo')#DC备注
    DC_save_loc = (By.XPATH,'//*[@id="divSupplyCall"]/input[2]')#保存DC结果


    def intview_DC(self):
        '''DC邀约'''
        self.gotoNeedApproveList()
        self.scrollToElement('id',self.intview_DC_loc)
        self.click_element(*self.intview_DC_btn_loc)
        time.sleep(1)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_frame_loc)
        self.click_element(*self.DC_success_loc)
        self.input_value(self.DC_memo_loc,'自动化测试：DC备注')
        self.click_element(*self.DC_save_loc)



# ============================================================================================
    # 验证case的执行结果：  未完待续
    clt_name_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[3]')
    def verfifyIntviewAppvSuccess(self):
        '''校验邀约是否审批成功'''
        return self.find_element(*self.clt_name_loc).text

