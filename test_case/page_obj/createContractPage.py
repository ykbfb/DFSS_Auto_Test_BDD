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

class NewContractPage(Page):
    # 合同管理
    contract_tab_loc = (By.XPATH,'//*[@id="bottomTabs_htgl"]/a')
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    def clickContractTab(self):
        self.find_element(*self.contract_tab_loc).click()
        self.scrollToElement('id',self.botom_frame_loc) # 页面跳转到底部【客户详情】所在的位置--相当于滚动条
        self.switchToOneFrame(self.botom_frame_loc) # 切换到底部【客户详情】的iframe

    # 创建及输入合同详情
    newContract_loc = (By.ID,'span4')    #新合同
    createNewContract_loc = (By.ID,'btnCreateContract')  #创建合同
    contract_frame_loc = '//*[@id="layui-layer-iframe3"]' #创建合同页面的frame
    def openNewContractPage(self):
        self.find_element(*self.newContract_loc).click()
        self.setWaitTime(20)
        self.find_element(*self.createNewContract_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.contract_frame_loc)

    #输入合同详情
    VIP_contract_type_loc = (By.ID,'contractType1') #债权会员合同
    BPO_contract_type_loc = (By.ID,'contractType2') #债权外包合同
    contract_code_loc = 'selContract'#合同号
    def inputContractDetail_VIP(self,index=0):
        self.index = index
        self.find_element(*self.VIP_contract_type_loc).click()
        self.getDropdownMenuById(self.contract_code_loc, index)

    def inputContractDetail_BPO(self,index=0):
        self.index = index
        self.find_element(*self.BPO_contract_type_loc).click()
        self.getDropdownMenuById(self.contract_code_loc, index)

    #选择合同客户名称
    contract_name_loc = 'selType'
    def selectContractName(self,index=0):
        self.index = index
        self.getDropdownMenuById(self.contract_name_loc, index)

    #预估额度
    predit_loanAmt_loc = (By.ID,'txtPreditAmount')
    moveTo_predit_loanAmt_loc =  'txtPreditAmount'
    def inputPreLoanAmt(self,value=100):
        self.value = value
        self.find_element(*self.predit_loanAmt_loc).clear()
        self.find_element(*self.predit_loanAmt_loc).send_keys(value)

    #意向金
    intention_Amt_loc = (By.ID,'txtFee')
    def inputIntentionAmt(self,value=5000):
        self.value = value
        self.find_element(*self.intention_Amt_loc).clear()
        self.find_element(*self.intention_Amt_loc).send_keys(value)

    #输入合同起始日期
    contract_startDate_loc = 'txtServiceStart'
    def selectConStartDate(self,value='2018-01-20'):
        self.value = value
        self.getDateTimePicker(self.contract_startDate_loc,value)

    #输入代扣协议
    isassigned_loc = '//*[@id="form1"]/table/tbody/tr[12]/th/span'
    bank1_loc = (By.ID,'bankCard')#银行卡号1
    phone1_loc = (By.ID,'bankCardPhone')#银行卡对应手机号1
    bank2_loc = (By.ID,'bankCard2')#银行卡号2
    phone2_loc = (By.ID,'bankCardPhone2')#银行卡对应手机号2
    bank3_loc = (By.ID,'bankCard3')#银行卡号3
    phone3_loc = (By.ID,'bankCardPhone3')#银行卡对应手机号3
    def inputAgreementDetail(self):
        self.scrollToElement('xpath',self.isassigned_loc)
        self.input_value(self.bank1_loc,'6225142536475869000')
        self.input_value(self.phone1_loc,'13247586921')
        self.input_value(self.bank2_loc,'6225142536475869001')
        self.input_value(self.phone2_loc,'13247586922')
        self.input_value(self.bank3_loc,'6225142536475869002')
        self.input_value(self.phone3_loc,'13247586923')

    #备注
    contract_memo_loc = (By.ID,'txtMemo')
    moveTo_contract_memo_loc = 'txtMemo'
    def inputContractMo(self,value='测试创建新合同!'):
        self.value = value
        self.scrollToElement('id',self.moveTo_contract_memo_loc)
        self.find_element(*self.contract_memo_loc).clear()
        self.find_element(*self.contract_memo_loc).send_keys(value)

    #上传合同附件
    get_elem_way = 'xpath'
    # elem1 = 'btnUpFile'
    # elem2 = 'btnUpFile2'
    # elem3 = 'btnUpFile3'

    elem1 =(By.XPATH, '//*[@id="picker1"]/div[2]/input')
    elem2 = (By.XPATH,'//*[@id="picker2"]/div[2]/input')
    elem3 = (By.XPATH,'//*[@id="picker3"]/div[2]/input')
    elem4 = (By.XPATH,'//*[@id="pickerSignFile"]/div[2]/input')
    elem5 = (By.XPATH,'//*[@id="pickerIdCardFile"]/div[2]/input')
    elem6 = (By.XPATH,'//*[@id="pickerBankCardFile"]/div[2]/input')
    elem7 = (By.XPATH,'//*[@id="pickerContractPaperFile"]/div[2]/input')
    file_path = 'F:\PyhtonTest\girl.jpg'


    # uploadBtn = (By.ID,'btnUp')
    # uploadBtn2 = (By.ID, 'btnUp2')
    # uploadBtn3 = (By.ID, 'btnUp3')

    uploadBtn = (By.ID,'btnUpload_picker1')
    uploadBtn2 = (By.ID, 'btnUpload_picker2')
    uploadBtn3 = (By.ID, 'btnUpload_picker3')
    uploadBtn4 = (By.ID,'btnUpload_pickerSignFile')
    uploadBtn5 = (By.ID,'btnUpload_pickerIdCardFile')
    uploadBtn6 = (By.ID,'btnUpload_pickerBankCardFile')
    uploadBtn7 = (By.ID,'btnUpload_pickerContractPaperFile')
    moveto_btn3_loc = 'btnUpload_picker3'


    # def uploadContractFile(self):
    #     self.uploadFile(self.getWay,self.elem1,self.file_path)  # 特批事项附件
    #     self.find_element(*self.uploadBtn).click()
    #     self.setWaitTime(30)
    #     self.uploadFile(self.getWay,self.elem2,self.file_path)  # 营业执照/法人资料附件
    #     self.find_element(*self.uploadBtn2).click()
    #     self.setWaitTime(30)
    #     self.uploadFile(self.getWay,self.elem3,self.file_path)  # 合同原件附件
    #     self.find_element(*self.uploadBtn3).click()
    #     self.setWaitTime(30)

    def uploadContractFile(self):
        self.uploadFile2(self.elem1,self.file_path)
        self.click_element(*self.uploadBtn)
        self.waitElmentUntill(50,self.elem2)
        time.sleep(2)
        self.uploadFile2(self.elem2,self.file_path)
        self.waitElmentUntill(20,self.uploadBtn2)
        time.sleep(1)
        self.click_element(*self.uploadBtn2)
        self.uploadFile2(self.elem3,self.file_path)
        self.waitElmentUntill(20,self.uploadBtn3)
        time.sleep(1)
        self.click_element(*self.uploadBtn3)
        self.scrollToElement('id',self.moveto_btn3_loc)
        self.uploadFile2(self.elem4,self.file_path)
        self.waitElmentUntill(20,self.uploadBtn4)
        time.sleep(1)
        self.click_element(*self.uploadBtn4)
        self.uploadFile2(self.elem5,self.file_path)
        self.waitElmentUntill(20,self.uploadBtn5)
        time.sleep(1)
        self.click_element(*self.uploadBtn5)
        self.uploadFile2(self.elem6,self.file_path)
        self.waitElmentUntill(20,self.uploadBtn6)
        time.sleep(1)
        self.click_element(*self.uploadBtn6)
        self.uploadFile2(self.elem7,self.file_path)
        self.waitElmentUntill(20,self.uploadBtn7)
        time.sleep(1)
        self.click_element(*self.uploadBtn7)
        time.sleep(1)



    #提交合同
    moveto_save_btn_loc = 'btnSave'
    save_loc = (By.ID,'btnSave')
    def submitContract(self):
        self.find_element(*self.save_loc).click()


#=============================================================================================================================================
#转会员
    popWinMax_loc = (By.XPATH,'//*[@id="layui-layer3"]/span[1]/a[2]')
    change_VIPContract_loc = (By.PARTIAL_LINK_TEXT,"转会员") #转会员按钮
    pop_new_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    def openChangeToVIPContract(self):
        self.find_element(*self.newContract_loc).click()
        time.sleep(1)
        self.find_element(*self.change_VIPContract_loc).click()
        self.switchWindow()
        # self.maxWindowByJs()
        time.sleep(1)
        self.switchToOneFrameByXpath(self.pop_new_frame_loc)


#==============================================================================================================================================
    # 创建会员合同
    def createVIPContract(self):
        self.clickContractTab()
        self.openNewContractPage()
        time.sleep(1)
        self.inputContractDetail_VIP()
        self.selectContractName()
        self.selectConStartDate()
        self.inputPreLoanAmt()
        self.inputAgreementDetail()
        self.inputContractMo()
        self.uploadContractFile()
        self.submitContract()
        time.sleep(3)
        self.close_alert()
        time.sleep(3)

    #合同创建完毕回到合同列表页
    def gobackToContractlist(self):
        self.switchToParentFrame()

#=======================================================================================================================
    # 创建外包合同
    def createBPOContract(self):
        self.clickContractTab()
        self.openNewContractPage()
        time.sleep(1)
        self.inputContractDetail_BPO()
        self.selectContractName()
        self.selectConStartDate()
        self.inputPreLoanAmt()
        self.inputIntentionAmt()
        self.inputContractMo()
        self.inputAgreementDetail()
        self.scrollToElement('id',self.moveto_save_btn_loc)
        self.uploadContractFile()
        self.submitContract()
        time.sleep(3)
        self.close_alert()
        time.sleep(1)
        #self.close_alert()

#====================================================================================================================
    # 外包合同转会员
    def BPOContractTransToVIP(self):
        self.clickContractTab()
        self.openChangeToVIPContract()
        self.scrollToElement('id',self.moveTo_predit_loanAmt_loc)
        self.inputPreLoanAmt()
        self.scrollToElement('id',self.moveTo_contract_memo_loc)
        self.inputContractMo()
        self.uploadContractFile()
        self.submitContract()
        time.sleep(3)
        self.close_alert()

# ============================================================================================
    # 验证case的执行结果：  未完待续
    fapo_btn_loc = (By.XPATH,'//*[@id="main"]/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[1]/div/div')
    def verifyContractCreateSucess(self):
        return self.find_element(*self.fapo_btn_loc).text