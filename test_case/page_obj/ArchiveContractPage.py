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

class ArchiveContractPage(Page):
    # 分公司出纳合同归档
    finc_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]') #财务
    contract_achiv_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[1]/div/a/span[2]')#合同审批发放
    contract_frame_loc = '//*[@id="tabs"]/div[2]/div[1]/div/iframe'
    contract_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    need_achiv_loc = (By.XPATH,'//*[@id="li2"]') #未归档
    contractName_loc = (By.ID,'nameOrLink') #客户名称
    search_loc = (By.ID,'btnCheck') #查询按钮

    def gotoNeedAchiveList(self,contract_name):
        time.sleep(1)
        self.contract_name = contract_name
        self.find_element(*self.finc_nav_loc).click()
        self.find_element(*self.contract_achiv_menu_loc).click()
        self.setWaitTime(10)
        time.sleep(1)
        self.switchFrame(self.contract_frame_loc,self.contract_list_frame_loc)
        self.find_element(*self.need_achiv_loc).click()

        self.find_element(*self.contractName_loc).clear()
        self.find_element(*self.contractName_loc).send_keys(contract_name)
        self.find_element(*self.search_loc).click()
        time.sleep(1)


    #合同归档
    radio_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td')#列表页选择未归档合同
    archive_loc = (By.ID,'btnDoUpdate') #归档按钮
    signForCompany_loc = (By.ID,'rdSignCompany') #公司名义签订
    signForPerson_loc = (By.ID,'rdSignPerson') #个人名义签订
    archive_btn_loc = (By.ID,'btnGui') #归档按钮
    archive_btn = 'btnGui'

    #公司名义签订
    def archiveContractForCMP_VIP(self):
        '''会员合同归档'''
        self.find_element(*self.radio_loc).click()
        self.find_element(*self.archive_loc).click()
        self.switchWindow()
        time.sleep(1)
        self.find_element(*self.signForCompany_loc).click()
        self.scrollToElement('id',self.archive_btn)
        self.find_element(*self.archive_btn_loc).click()
        # time.sleep(1)
        # self.close_alert()

    def archiveContractForCMP_BPO(self):
        '''外包合同归档'''
        self.find_element(*self.radio_loc).click()
        self.find_element(*self.archive_loc).click()
        self.switchWindow()
        time.sleep(1)
        self.find_element(*self.signForCompany_loc).click()
        self.scrollToElement('id',self.archive_btn)
        self.find_element(*self.archive_btn_loc).click()
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.close_alert()

#--------------------------------------------------------------------------------------------------
    #个人名义签订
    def archiveContractForPerson_VIP(self):
        '''会员合同归档'''
        self.find_element(*self.radio_loc).click()
        self.find_element(*self.archive_loc).click()
        self.switchWindow()
        time.sleep(1)
        self.find_element(*self.signForPerson_loc).click()
        self.scrollToElement('id',self.archive_btn)
        self.find_element(*self.archive_btn_loc).click()
        time.sleep(2)
        self.close_alert()
        time.sleep(2)

    def archiveContractForPerson_BPO(self):
        '''外包合同归档'''
        self.find_element(*self.radio_loc).click()
        self.find_element(*self.archive_loc).click()
        self.switchWindow()
        time.sleep(1)
        self.find_element(*self.signForPerson_loc).click()
        self.scrollToElement('id',self.archive_btn)
        self.find_element(*self.archive_btn_loc).click()
        time.sleep(2)
        self.close_alert()
        time.sleep(2)
        self.close_alert()
#---------------------------------------------------------------------------------------------
    archived_tab_loc = (By.XPATH,'//*[@id="main"]/ul/li[3]')#已归档
    clt_name_loc = (By.ID,'nameOrLink')#客户名称
    search_btn_loc = (By.ID,'btnCheck')#查询
    #归档完合同，返回【已归档】页面
    def gotoArchivedContractList(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.archived_tab_loc)
        time.sleep(1)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.search_btn_loc)
        time.sleep(2)


#=============================================================================================
    #合同打回
    reject_loc = (By.ID,'btnDoSetBackToSales')#打回按钮
    rej_check1_loc = (By.ID,'ckdhyy1') #打回原因
    rej_check2_loc = (By.ID,'ckdhyy2')
    rej_check3_loc = (By.ID,'ckdhyy3')
    rej_check4_loc = (By.ID,'ckdhyy4')
    rej_check5_loc = (By.ID,'ckdhyy5')
    rej_memo_loc = (By.ID,'ttdhbz') #打回备注
    rej_confirm_loc = (By.ID,'btnOk')#确定

    def rejectContract(self,memo):
        self.memo = memo
        self.find_element(*self.radio_loc).click()
        self.find_element(*self.reject_loc).click()
        self.setWaitTime(10)
        self.switchWindow()
        self.find_element(*self.rej_check1_loc).click()
        self.find_element(*self.rej_check2_loc).click()
        self.find_element(*self.rej_check3_loc).click()
        self.find_element(*self.rej_check4_loc).click()
        self.find_element(*self.rej_check5_loc).click()
        self.find_element(*self.rej_memo_loc).clear()
        self.find_element(*self.rej_memo_loc).send_keys(memo)
        self.find_element(*self.rej_confirm_loc).click()
        time.sleep(2)
        self.close_alert()

    ctr_other_tab_loc = (By.ID,'liO')#其他页签
    def gotoOtherTab(self,clt_name):
        '''返回【其他】页签'''
        self.clt_name = clt_name
        self.click_element(*self.ctr_other_tab_loc)
        time.sleep(1)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.search_btn_loc)
        time.sleep(2)

    #合同作废
    discar_loc = (By.ID,'btnDoNoUse1')
    dis_reason_loc = (By.ID,'cb8')
    dis_memo_loc = (By.ID,'txtMemo')
    dis_confirm_loc = (By.ID,'btnOK')

    def discarContract(self,memo):
        self.memo = memo
        self.find_element(*self.radio_loc).click()
        self.find_element(*self.discar_loc).click()
        self.setWaitTime(10)
        self.switchWindow()
        self.find_element(*self.dis_reason_loc).click()
        self.find_element(*self.dis_memo_loc).clear()
        self.find_element(*self.dis_memo_loc).send_keys(memo)
        self.find_element(*self.dis_confirm_loc).click()
        time.sleep(2)
        self.close_alert()

    #归档完合同，返回【已归档】页面查询作废合同
    archive_status_loc = '//*[@id="tdContractStatus"]/div/a/span'#归档状态
    def gotoDiscaredContractList(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.archived_tab_loc)
        time.sleep(1)
        self.input_value(self.clt_name_loc,clt_name)
        self.getDropdownMenuByXpath(self.archive_status_loc,2) #作废
        self.click_element(*self.search_btn_loc)
        time.sleep(2)

# ============================================================================================
    # 验证case的执行结果：  未完待续
    list_clt_name_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[6]')#列表客户名称
    def verifyContractArchivedSucess(self):
        '''校验合同归档成功'''
        return self.find_element(*self.list_clt_name_loc).text
        print(self.find_element(*self.list_clt_name_loc).text)

    def verifyContractRejecteddSucess(self):
        '''校验合同打回成功'''
        return self.find_element(*self.list_clt_name_loc).text
        print(self.find_element(*self.list_clt_name_loc).text)

    def verifyContractDiscardSucess(self):
        '''校验合同作废成功'''
        return self.find_element(*self.list_clt_name_loc).text
        print(self.find_element(*self.list_clt_name_loc).text)