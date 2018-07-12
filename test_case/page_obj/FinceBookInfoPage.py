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
from data.TestData import Data

class finceBookInfo(Page):

    #客户列表右键打开需求书编辑页面
    edit_fincebookInfo_loc = '//*[@id="datagrid-row-r3-2-0"]/td[1]'
    edit_loc = (By.XPATH,'//*[@id="contextMenuId_rzsqsbj"]/div') #右键编辑需求书
    def openFinceBookPage(self):
        self.rightClick(self.edit_fincebookInfo_loc)
        self.setWaitTime(2)
        self.find_element(*self.edit_loc).click()
        time.sleep(1)
        self.switchWindow()
#=============================================================================================================================================
#基本信息

    # 编辑需求书
    finceBookInfo_frame_loc = 'layui-layer-iframe4'
    def switchToFinceBookFrame(self):
        self.switchToOneFrame(self.finceBookInfo_frame_loc)

    #需求书详情
    clt_type_loc = (By.ID,'rdCltType1') #选择客户类型--企业主
    def setCltType(self):
        self.find_element(*self.clt_type_loc).click()

    #输入姓名
    lnk_name_loc = (By.ID,'txtLnkName')#姓名
    def inputCltName(self,value='大坤哥自动化'):
        self.value = value
        self.find_element(*self.lnk_name_loc).clear()
        self.find_element(*self.lnk_name_loc).send_keys(value)
    #选择性别
    clt_sex_loc = (By.ID,'rdMan') #性别
    def setCltSex(self):
        self.find_element(*self.clt_sex_loc).click()
    #选择婚姻
    clt_isMarry_loc = (By.ID,'rdMarry1') #婚姻
    def setCltMarry(self):
        self.find_element(*self.clt_isMarry_loc).click()

    #选择证件类型
    clt_IDCard_loc = 'selCertificateType' #证件类型
    def setCltID(self,index = '0'):
        self.index = index
        self.getDropdownMenuById(self.clt_IDCard_loc, index)

    #输入身份证号
    lnk_IDCardNo_loc = (By.ID,'txtLnkID')#身份证
    def inputCltIDNo(self,value='142536198511251369'):
        self.value = value
        self.find_element(*self.lnk_IDCardNo_loc).clear()
        self.find_element(*self.lnk_IDCardNo_loc).send_keys(value)

    #选择学历
    clt_education_loc = 'selEducation' #学历
    def selectCltEducation(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.clt_education_loc, index)
    #选择省份
    clt_live_provence_loc = 'selLnkProvince' #户籍—省份
    def selectCltLiveProvence(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.clt_live_provence_loc, index)
    #选择城市
    clt_live_city_loc = 'selLnkCity' #户籍—城市
    def selectCltLiveCity(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.clt_live_city_loc, index)

    #选择本市居住时长
    clt_currcity_livetime_loc = 'selLocalLivedTime' #本市居住时长
    def selectCltLiveTime(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.clt_currcity_livetime_loc, index)

#=====================================================================================================================================================
# 需求信息
    require_frame_loc = '//*[@id="tableMain"]/tbody/tr[5]/td'
    def gotoReqDetail(self,getWay = 'xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay,self.require_frame_loc)

    #输入贷款金额
    loan_amt_loc = (By.ID,'txtRqrAmount')#贷款金额
    def inputLoanAmt(self,value='100'):
        self.value = value
        self.find_element(*self.loan_amt_loc).clear()
        self.find_element(*self.loan_amt_loc).send_keys(value)

    #输入贷款期限
    loan_duration_loc = (By.ID,'txtRqrDuration')#贷款期限
    def inputLoanDuration(self,value='24'):
        self.value = value
        self.find_element(*self.loan_duration_loc).clear()
        self.find_element(*self.loan_duration_loc).send_keys(value)

    #用款时间
    rqr_date_loc = 'txtRqrDate' #用款时间
    def selectRqrDate(self,rqrdate = '2017-08-25'):
        self.rqrdate = rqrdate
        self.getDateTimePicker(self.rqr_date_loc,rqrdate)

    #贷款用途
    clt_RqrReason_loc = 'selRqrReason' #贷款用途
    def selectRqrReason(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.clt_RqrReason_loc, index)

    #还款来源
    clt_ReturnSource_loc = 'selReturnSource' #还款来源
    def selectReturnSource(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.clt_ReturnSource_loc, index)

    #最高可接受月利率
    MaxAcceptMonthRate_loc = (By.ID,'txtMaxAcceptMonthRate')#最高可接受月利率
    def inputMaxAcceptMonthRate(self,value='10.25'):
        self.value = value
        self.find_element(*self.MaxAcceptMonthRate_loc).clear()
        self.find_element(*self.MaxAcceptMonthRate_loc).send_keys(value)

    #最高可以接受服务费率
    MaxAcceptServiceRate_loc = (By.ID,'txtMaxAcceptServiceRate')
    def inputMaxAcceptServiceRate(self,value='24.25'):
        self.value = value
        self.find_element(*self.MaxAcceptServiceRate_loc).clear()
        self.find_element(*self.MaxAcceptServiceRate_loc).send_keys(value)

    #紧急程度
    LoanEmergencyDegrees_loc = 'selLoanEmergencyDegrees' #紧急程度
    def selectLoanEmergency(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.LoanEmergencyDegrees_loc, index)

#================================================================================================================================================
# 企业信息
    cmp_frame_loc = '//*[@id="tableMain"]/tbody/tr[13]/td[1]/div'
    def gotoCmpDetail(self,getWay = 'xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay,self.cmp_frame_loc)

    #是否法人代表
    rbRepresentative_loc = (By.ID,'rbRepresentative1')
    def selectRepresentative(self):
        self.find_element(*self.rbRepresentative_loc).click()

    #持股比例
    selShares_loc = 'selShares'
    def selectShares(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.selShares_loc, index)

    #企业经营地
    rbCompanyLocation_loc = (By.ID,'rbCompanyLocation1')
    def selectCmpLocation(self):
        self.find_element(*self.rbCompanyLocation_loc).click()

    #企业性质
    selCompanyNature_loc = 'selCompanyNature'
    def selectCmpNatture(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.selCompanyNature_loc, index)

    #企业名称
    cmpName_loc = (By.ID,'txtCmpName')
    def inputCmpName(self,value='自动化测试有限公司'):
        self.value = value
        self.find_element(*self.cmpName_loc).clear()
        self.find_element(*self.cmpName_loc).send_keys(value)

    #所属行业
    selTrade_loc = 'selTrade'
    def selectCmpRadeArea(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.selTrade_loc, index)

    #详细地址
    cmpAddress_loc = (By.ID,'txtCmpAddr')
    def inputCmpAdress(self,value='企业主-某市上大路1000号中银大厦'):
        self.value = value
        self.find_element(*self.cmpAddress_loc).clear()
        self.find_element(*self.cmpAddress_loc).send_keys(value)

    #公司规模
    cmpEmpAmt_loc = (By.ID,'txtScale')
    def inputCmpEmpAmt(self,value='1000'):
        self.value = value
        self.find_element(*self.cmpEmpAmt_loc).clear()
        self.find_element(*self.cmpEmpAmt_loc).send_keys(value)

    #企业类型
    cmpType_loc = 'selEnterpriseType'
    def selectCmpType(self,index = '5'):
        self.index = index
        self.getDropdownMenuById(self.cmpType_loc, index)

    #全年开票额
    cmpYearBill_loc = 'selYearBill'
    def selectCmpYearBill(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.cmpYearBill_loc, index)

    #月对私流水
    cmpToPrivate_loc = 'selToPrivate'
    def selectCmpToPrivate(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.cmpToPrivate_loc, index)

    #月对公流水
    cmpToPublic_loc = 'selToPublic'
    def selectCmpToPublic(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.cmpToPublic_loc, index)

    #年净利润
    cmp_RetainedProfits_loc = 'selYearSalary'
    def selectCmpRetainedProfits(self,index = '5'):
        self.index = index
        self.getDropdownMenuById(self.cmp_RetainedProfits_loc, index)

    #资产负责率
    cmp_LiabilityRate_loc = 'selLiabilityRate'
    def selectCmpLiabilityRate(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.cmp_LiabilityRate_loc, index)

    #营业执照年限
    cmp_license_loc = 'selOPYears'
    def selectCmpLicense(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.cmp_license_loc, index)

    #注册资金
    cmp_SignAmount_loc = 'txtSignAmount'
    def selectCmpSignAmount(self,index = '4'):
        self.index = index
        self.getDropdownMenuById(self.cmp_SignAmount_loc, index)

    #年营业额
    cmpYearTurnOverAmount_loc = (By.ID,'txtYearAmount')
    def inputCmpYearTurnOverAmount(self,value='555'):
        self.value = value
        self.find_element(*self.cmpYearTurnOverAmount_loc).clear()
        self.find_element(*self.cmpYearTurnOverAmount_loc).send_keys(value)
    #年营业收入
    cmp_IncomeAmount_loc = 'selYearInCome'
    def selectCmpIncomeAmount(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.cmp_IncomeAmount_loc, index)

#===========================================================================================================================================]
# 股权信息
    equty_frame_loc = '//*[@id="tableMain"]/tbody/tr[16]/td'
    def gotoEqutyDetail(self,getWay = 'xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay,self.cmp_frame_loc)

    #是否为员工缴纳社保
    paiedSecurityForEmp_loc = (By.ID,'rbIsPaiedSecurityForEmployees1')
    def selectPaiedSecurityForEmp(self):
        self.find_element(*self.paiedSecurityForEmp_loc).click()

    #创始人背景
    FounderBackground_loc = 'selFounderBackground'
    def selectCmpFounderBackground(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.FounderBackground_loc, index)

    #是否有机构股东
    InstShareholders_loc = (By.ID,'rbInstitutionalShareholders1')
    def selectCmpInstShareholders(self):
        self.find_element(*self.InstShareholders_loc).click()

    #是否为高新企业
    HighTechEnterprises_loc = (By.ID,'rbHighTechEnterprises1')
    def selectCmpHighTechEnter(self):
        self.find_element(*self.HighTechEnterprises_loc).click()

    #营业额增长率
    cmpYearInComeRate_loc = (By.ID,'txtStockYearInComeRate')
    def inputCmpYearInComeRate(self,value='20.58'):
        self.value = value
        self.find_element(*self.cmpYearInComeRate_loc).clear()
        self.find_element(*self.cmpYearInComeRate_loc).send_keys(value)

    #所属细分行业
    IndustrySg_loc = 'selIndustrySegmentation'
    def selectCmpIndustrySg(self,index = '5'):
        self.index = index
        self.getDropdownMenuById(self.IndustrySg_loc, index)

#=======================================================================================================================================
# 信用及负责信息
    cridit_frame_loc = '//*[@id="tableMain"]/tbody/tr[25]/td'
    def gotoCriditDetail(self,getWay = 'xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay,self.cridit_frame_loc)

    #行用卡总额度
    creditAmt_loc = 'selCreditTotal'
    def selectCreditCardAmt(self,index = '6'):
        self.index = index
        self.getDropdownMenuById(self.creditAmt_loc, index)

    #信用卡张数
    CreditCount_loc = (By.ID,'txtCreditCount')
    def inputCreditCount(self,value='3'):
        self.value = value
        self.find_element(*self.CreditCount_loc).clear()
        self.find_element(*self.CreditCount_loc).send_keys(value)

    #单张信用卡最高额度
    PrecreditCardMaxAmt_loc = 'selCreditCardMaxAmount'
    def selectPerCreditCardMaxAmt(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.PrecreditCardMaxAmt_loc, index)

    #信用卡已用额度
    creditCardUsedAmt_loc = 'selCreditUsed'
    def selectCreditCardUsedAmt(self,index = '4'):
        self.index = index
        self.getDropdownMenuById(self.creditCardUsedAmt_loc, index)

    #选择银行
    bank1_loc = 'CreditBank2'
    def selectBanks1(self):
        self.getCheckbox(self.bank1_loc)

    bank2_loc = 'CreditBank8192'
    def selectBanks2(self):
        self.getCheckbox(self.bank2_loc)

    bank3_loc = 'CreditBank32'
    def selectBanks3(self):
        self.getCheckbox(self.bank3_loc)

    #其他银行
    otherBank_loc = 'CreditBankOthers'
    def selectOtherBanks(self):
        self.getCheckbox(self.otherBank_loc)

    txt_bank_loc = (By.ID,'CreditBankOthersText')
    def inputOtherBank(self,value='花旗银行'):
        self.value = value
        self.find_element(*self.txt_bank_loc).clear()
        self.find_element(*self.txt_bank_loc).send_keys(value)

    #个人信用情况
    personCredit_loc = 'selMasterCredit'
    def selectPersonCredit(self,index = '6'):
        self.index = index
        self.getDropdownMenuById(self.personCredit_loc, index)

    # 个人逾期1个月次数
    person_overtime1_loc = (By.ID,'txtMasterOver1monthCount')
    def inputOverTime1(self,value='2'):
        self.value = value
        self.find_element(*self.person_overtime1_loc).clear()
        self.find_element(*self.person_overtime1_loc).send_keys(value)

    # 个人逾期2个月次数
    person_overtime2_loc = (By.ID,'txtMasterOver2monthCount')
    def inputOverTime2(self,value='3'):
        self.value = value
        self.find_element(*self.person_overtime2_loc).clear()
        self.find_element(*self.person_overtime2_loc).send_keys(value)

    # 个人逾期3个月次数
    person_overtime3_loc = (By.ID,'txtMasterOver3monthCount')
    def inputOverTime3(self,value='4'):
        self.value = value
        self.find_element(*self.person_overtime3_loc).clear()
        self.find_element(*self.person_overtime3_loc).send_keys(value)

    # 个人逾期4个月次数
    person_overtime4_loc = (By.ID,'txtMasterOver4monthCount')
    def inputOverTime4(self,value='6'):
        self.value = value
        self.find_element(*self.person_overtime4_loc).clear()
        self.find_element(*self.person_overtime4_loc).send_keys(value)

    # 个人近2年内逾期次数
    person_year_overtime_count_loc = (By.ID,'txtMasterOverCountIn2Years')
    def inputTwoOverTime(self,value='10'):
        self.value = value
        self.find_element(*self.person_year_overtime_count_loc).clear()
        self.find_element(*self.person_year_overtime_count_loc).send_keys(value)

    # 配偶信用情况
    pair_credit_loc = 'selSpouceCredit'
    def selectPairCredit(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.pair_credit_loc, index)

    # 企业信用情况
    cmp_credit_loc = 'selEnterpriseCredit'
    def selectCmpCredit(self,index = '5'):
        self.index = index
        self.getDropdownMenuById(self.cmp_credit_loc, index)

    # 企业逾期总次数
    cmp_overtime_count_loc = (By.ID,'txtEnterpriseOverdueCount')
    def inputCmpOverTimeCount(self,value='5'):
        self.value = value
        self.find_element(*self.cmp_overtime_count_loc).clear()
        self.find_element(*self.cmp_overtime_count_loc).send_keys(value)

    # 企业逾期最长时间
    cmp_max_overtime_loc = (By.ID,'txtEnterpriseMaxOverMonth')
    def inputCmpMaxOverTimes(self,value='4'):
        self.value = value
        self.find_element(*self.cmp_max_overtime_loc).clear()
        self.find_element(*self.cmp_max_overtime_loc).send_keys(value)

    #个人欠款情况
    person_debt_loc = 'LoanStatus1'
    def selectPersonDebt(self):
        self.getCheckbox(self.person_debt_loc)

    #企业欠款情况
    cmp_debt_loc = 'CompanyDebtStatus1'
    def selectCmpDebt(self):
        self.getCheckbox(self.cmp_debt_loc)

#==========================================================================================================================================
# 房产信息
    house_frame_loc = '//*[@id="tableMain"]/tbody/tr[35]/td'
    def gotoHouseDetail(self,getWay = 'xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay,self.cridit_frame_loc)

    #名下房产情况
    isHasHouse_loc = 'rdHaveHouse1'
    def setIsHasHouse(self):
        self.getRadioButton(self.isHasHouse_loc)

    #是否有备用房
    isHasBackupHouse_loc = 'rdsubhou1'
    def setIsHasBackupHouse(self):
        self.getRadioButton(self.isHasBackupHouse_loc)

    # 企业信用情况
    house_type_loc = 'selHouType'
    def selectHouseType(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.house_type_loc, index)

    # 房产性质
    house_property_loc = 'selHouseProperty'
    def selectHouseProperty(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.house_property_loc, index)

    # 房产位置
    house_location_loc = 'selHouArea'
    def selectHouseLocation(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.house_location_loc, index)

    # 房产面积
    house_square_loc = 'selHouSquare'
    def selectHouseSqure(self,index = '4'):
        self.index = index
        self.getDropdownMenuById(self.house_square_loc, index)

    # 房产地址
    house_address_loc = (By.ID,'txtHouAddr')
    def inputHouseAddress(self,value='上海市黄兴花园15栋601室'):
        self.value = value
        self.find_element(*self.house_address_loc).clear()
        self.find_element(*self.house_address_loc).send_keys(value)

    #能否提供房产证
    isHasHouseLicense_loc = 'rdHouseLicense1'
    def setIsHasHouseLicense(self):
        self.getRadioButton(self.isHasHouseLicense_loc)

    # 房产总价
    house_amt_loc = (By.ID,'txtHouAmout')
    def inputHouseAmout(self,value='150'):
        self.value = value
        self.find_element(*self.house_amt_loc).clear()
        self.find_element(*self.house_amt_loc).send_keys(value)

    # 房产估值
    house_evaluate_loc = 'txtHouAssessment'
    def selectHouseEvalution(self,index = '5'):
        self.index = index
        self.getDropdownMenuById(self.house_evaluate_loc, index)

    # 房龄
    house_age_loc = (By.ID,'txtHouseAge')
    def inputHouseAge(self,value='50'):
        self.value = value
        self.find_element(*self.house_age_loc).clear()
        self.find_element(*self.house_age_loc).send_keys(value)

    # 抵押、按揭状态
    house_impawn_loc = 'selHouMortgage'
    def selectHouseImpawn(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.house_impawn_loc, index)

    # 贷款余额
    house_loanBalance_loc = (By.ID,'txtHouLoanBalance')
    def inputHouseLoanBlance(self,value='123.5'):
        self.value = value
        self.find_element(*self.house_loanBalance_loc).clear()
        self.find_element(*self.house_loanBalance_loc).send_keys(value)

    # 抵押、按揭月还款额
    house_repayAmt_loc = 'selHouMonthRepay'
    def selectHouseRepayAmt(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.house_repayAmt_loc, index)

    # 抵押、按揭已还款月数
    house_returnAmt_loc = 'selHouReturnMonth'
    def selectHouseReturnAmt(self,index = '4'):
        self.index = index
        self.getDropdownMenuById(self.house_returnAmt_loc, index)

    #是否有共权人
    isHasHouseOtherOwner_loc = 'rdHavePublicRightPerson1'
    def setIsHasHouseOtherOwner(self):
        self.getRadioButton(self.isHasHouseOtherOwner_loc)

    #共有权人是否包含未成年人、老人
    isHasHouseChildOwner_loc = 'rdChildrenAndOlder1'
    def setIsHasHouseChildOwner(self):
        self.getRadioButton(self.isHasHouseChildOwner_loc)

    #所有权利人能否签字
    isAllHouseOwnerSigned_loc = 'rdCanSign1'
    def setIsAllHouseOwnerSigned(self):
        self.getRadioButton(self.isAllHouseOwnerSigned_loc)

#=============================================================================================================================
# 车产信息
    car_frame_loc = '//*[@id="tableMain"]/tbody/tr[41]/td'
    def gotoCarDetail(self,getWay = 'xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay,self.car_frame_loc)

    #名下车产情况
    isHasCar_loc = 'rdHasCar1'
    def setIsHasCar(self):
        self.getRadioButton(self.isHasCar_loc)

    #是否二手车
    isSecondHandCar_loc = 'rdIsSecondHand2'
    def setIsSecondCar(self):
        self.getRadioButton(self.isSecondHandCar_loc)

    # 牌照归属地--省
    car_Province_loc = 'selCarBrandProvince'
    def selectCarProvince(self,index = 3):
        self.index = index
        self.getDropdownMenuById(self.car_Province_loc, index)

    # 牌照归属地--市
    car_city_loc = 'selCarBrandCity'
    def selectCarCity(self,index = 1):
        self.index = index
        self.getDropdownMenuById(self.car_city_loc, index)

    # 车辆购买价格
    car_buyAmt_loc = (By.ID,'txtCarBuyAmout')
    def inputCarBuyAmt(self,value='200'):
        self.value = value
        self.find_element(*self.car_buyAmt_loc).clear()
        self.find_element(*self.car_buyAmt_loc).send_keys(value)

    # 车龄
    car_age_loc = 'selCarAge'
    def selectCarAge(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.car_age_loc, index)

    # 行驶里程
    car_distance_loc = 'selCarDistance'
    def selectCarDistance(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.car_distance_loc, index)

    # 车产估值
    car_assesment_loc = 'selCarAssessment'
    def selectCarAssesment(self,index = '4'):
        self.index = index
        self.getDropdownMenuById(self.car_assesment_loc, index)

    # 抵押、按揭状态
    car_loanStatus_loc = 'selCarLoan'
    def selectCarLoanStatus(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.car_loanStatus_loc, index)

    # 抵押、按揭月还款额
    car_perMPayment_loc = 'selCarLoanMonthlyPaymentsAmount'
    def selectCarPerMouthPayAmt(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.car_perMPayment_loc, index)

    # 抵押、按揭已还款月数
    car_paidMouth_loc = 'selCarLoanPaymentsMonths'
    def selectCarPaiedMouth(self,index = '3'):
        self.index = index
        self.getDropdownMenuById(self.car_paidMouth_loc, index)

    # 贷款余额
    car_restAmt_loc = (By.ID,'txtCarLoadRest')
    def inputCarRestLoanAmt(self,value='20'):
        self.value = value
        self.find_element(*self.car_restAmt_loc).clear()
        self.find_element(*self.car_restAmt_loc).send_keys(value)

#===============================================================================================================================================
# 设备信息
    equip_frame_loc = '//*[@id="tableMain"]/tbody/tr[45]/td'
    def gotoEquipDetail(self,getWay = 'xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay,self.car_frame_loc)

    #名下设备情况
    isHasEquip_loc = 'rdIsHaveEquipment1'
    def setIsHasEquipment(self):
        self.getRadioButton(self.isHasEquip_loc)

    # 设备年限
    equip_age_loc = (By.ID,'txtEquipmentYearLimit')
    def inputEquipAge(self,value='40'):
        self.value = value
        self.find_element(*self.equip_age_loc).clear()
        self.find_element(*self.equip_age_loc).send_keys(value)

    # 设备目前净值
    equip_nowAmt_loc = (By.ID,'txtEquipmentNowAmount')
    def inputEquipNowAmt(self,value='220'):
        self.value = value
        self.find_element(*self.equip_nowAmt_loc).clear()
        self.find_element(*self.equip_nowAmt_loc).send_keys(value)

    # 设备购买价格
    equip_buyAmt_loc = (By.ID,'txtEquipmentBuyAmount')
    def inputEquipBuyAmt(self,value='1000'):
        self.value = value
        self.find_element(*self.equip_buyAmt_loc).clear()
        self.find_element(*self.equip_buyAmt_loc).send_keys(value)

    #是否有发票
    isHasInvoice_loc = 'rdIsHaveInvoice1'
    def setIsHasInvoice(self):
        self.getRadioButton(self.isHasInvoice_loc)

    # 设备抵押状态
    equip_Mortgage_loc = 'selEquipmentIsMortgage'
    def selectEquipMortgage(self,index = '2'):
        self.index = index
        self.getDropdownMenuById(self.equip_Mortgage_loc, index)

#================================================================================================================================================
# 保单信息
    insurance_frame_loc = '//*[@id="tableMain"]/tbody/tr[48]/td'
    def gotoInsuranceDetail(self, getWay='xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay, self.insurance_frame_loc)

    # 名下保单情况
    isHasInsurance_loc = 'rdInsuranceInfo1'
    def setIsHasInsurance(self):
        self.getRadioButton(self.isHasInsurance_loc)

    # 保单类型
    insure_type_Mortgage_loc = 'selInsuranceType'
    def selectInsureTpye(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.insure_type_Mortgage_loc, index)

    # 有无中断过缴纳
    isInsureStopPay_loc = 'rdIsInterrupted2'
    def setIsInsureStopPay(self):
        self.getRadioButton(self.isInsureStopPay_loc)

    # 缴费类型
    insure_payType_loc = 'selPaymentType'
    def selectInsurePayTpye(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.insure_payType_loc, index)

    # 已生效年限
    insure_effectTime_loc = (By.ID,'txtPolicyEffectedTime')
    def inputInsureEffectTime(self,value='20'):
        self.value = value
        self.find_element(*self.insure_effectTime_loc).clear()
        self.find_element(*self.insure_effectTime_loc).send_keys(value)

    # 已缴纳月数
    insure_PaiedMonths_loc = (By.ID,'txtPolicyPaiedMonths')
    def inputInsurePaiedMonths(self,value='10'):
        self.value = value
        self.find_element(*self.insure_PaiedMonths_loc).clear()
        self.find_element(*self.insure_PaiedMonths_loc).send_keys(value)

    # 保单每月缴纳金额
    insure_PerMonthAmt_loc = (By.ID,'txtPolicyAmountPaiedPerMonth')
    def inputInsurePerMounthAmt(self,value='2500'):
        self.value = value
        self.find_element(*self.insure_PerMonthAmt_loc).clear()
        self.find_element(*self.insure_PerMonthAmt_loc).send_keys(value)

    # 是否满缴保费
    isInsurePayOff_loc = 'rdPayOff1'
    def setIsInsurePayOff(self):
        self.getRadioButton(self.isInsurePayOff_loc)

    # 投保人
    insure_person_loc = 'selInsurancePerson'
    def selectInsurePerson(self,index = '1'):
        self.index = index
        self.getDropdownMenuById(self.insure_person_loc, index)

    # 保险公司
    insure_cmp_loc = 'selInsuranceCompany'
    def selectInsureCmp(self,index = '5'):
        self.index = index
        self.getDropdownMenuById(self.insure_cmp_loc, index)

#==============================================================================================================================================
# 其他资产
    otherAsset_frame_loc = '//*[@id="tableMain"]/tbody/tr[52]/td'
    def gotoOtherAssetDetail(self, getWay='xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay, self.otherAsset_frame_loc)

    #证券资产
    OtherAsset1_loc = 'OtherAssetsInfo2'
    def selectOtherAsset1(self):
        self.getCheckbox(self.OtherAsset1_loc)

    #艺术资产
    OtherAsset2_loc = 'OtherAssetsInfo4'
    def selectOtherAsset2(self):
        self.getCheckbox(self.OtherAsset2_loc)

#===========================================================================================================================================
# 担保信息
    guarant_frame_loc = '//*[@id="tableMain"]/tbody/tr[54]/td'
    def gotoGurantDetail(self, getWay='xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay, self.guarant_frame_loc)

    #名下设备情况
    isHasGuarantee_loc = 'rdIsGuarantee1'
    def setIsHasGuarantee(self):
        self.getRadioButton(self.isHasGuarantee_loc)

    # 担保人优势：有信誉
    GuarantorAdvantage1_loc = 'GuarantorAdvantage1'
    def selectGuarantorAdvantage1(self):
        self.getCheckbox(self.OtherAsset1_loc)

    # 担保人优势：有企业
    GuarantorAdvantage2_loc = 'GuarantorAdvantage2'
    def selectGuarantorAdvantage2(self):
        self.getCheckbox(self.GuarantorAdvantage2_loc)

    #配偶能否担保
    isSpouseSign_loc = 'rdSpouseSign1'
    def setIsSpouseSign(self):
        self.getRadioButton(self.isSpouseSign_loc)

#========================================================================================================================================
# 补充信息
    additionInfo_frame_loc = '//*[@id="tableMain"]/tbody/tr[58]/td'
    def gotoAdditionInfoDetail(self, getWay='xpath'):
        self.getWay = getWay
        self.scrollToElement(getWay, self.additionInfo_frame_loc)

    # 疑难杂症：信用不良
    otherInfo1_loc = 'dr_4'
    def selectOtherInfo1(self):
        self.getCheckbox(self.otherInfo1_loc)

    # 疑难杂症：产权人不签字
    otherInfo2_loc = 'dr_4096'
    def selectOtherInfo2(self):
        self.getCheckbox(self.otherInfo2_loc)

    # 疑难杂症：外籍人士
    otherInfo3_loc = 'dr_128'
    def selectOtherInfo3(self):
        self.getCheckbox(self.otherInfo3_loc)

    # 疑难杂症：近期重大变更
    otherInfo4_loc = 'dr_8192'
    def selectOtherInfo4(self):
        self.getCheckbox(self.otherInfo4_loc)

#===========================================================================================================================================
    # 保存需求书
    save_loc =(By.ID,'btnSave')
    def saveFinceBookInfo(self):
        self.find_element(*self.save_loc).click()
    #提交需求书
    submit_loc = (By.ID,'btnSubmit')
    def submitFinceBookInfo(self):
        self.find_element(*self.submit_loc).click()
#==============================================================================================================================================
#==============================================================================================================================================

    # 修改需求书---【保存】'''
    def saveFinancBookInfo(self):
        time.sleep(2)
        self.openFinceBookPage()
        self.switchToFinceBookFrame()
        self.setCltType()
        self.inputCltName(value='大坤哥自动化')
        self.gotoReqDetail(getWay='xpath')
        self.inputLoanAmt(value='100')
        self.inputLoanDuration(value='24')
        self.gotoCmpDetail(getWay='xpath')
        self.inputCmpName(value='自动化测试有限公司')
        self.selectCmpRadeArea(index=2)
        self.inputCmpAdress(value='企业主-某市上大路1000号中银大厦')
        self.gotoAdditionInfoDetail(getWay='xpath')
        self.saveFinceBookInfo()
        time.sleep(2)
        self.close_alert()


    # 需求书---【提交】
    def submitFinanceBookInfo(self):
        self.openFinceBookPage()
        self.switchToFinceBookFrame()
        '''基础信息'''
        self.setCltType()
        self.inputCltName(value=Data.lnk_name)
        self.setCltSex()
        self.setCltMarry()
        self.setCltID(index=0)
        self.inputCltIDNo(value='142536198511251369')
        self.selectCltEducation(index=1)
        self.selectCltLiveProvence(index=1)
        self.selectCltLiveCity(index=1)
        self.selectCltLiveTime(index=2)

        '''需求信息'''
        self.gotoReqDetail(getWay='xpath')
        self.inputLoanAmt(value='100')
        self.inputLoanDuration(value='24')
        self.selectRqrDate(rqrdate='2017-08-25')
        self.selectRqrReason(index=1)
        self.selectReturnSource(index=2)
        self.inputMaxAcceptMonthRate(value='10.25')
        self.inputMaxAcceptServiceRate(value='24.25')
        self.selectLoanEmergency(index=2)

        '''企业信息'''
        self.gotoCmpDetail(getWay='xpath')
        self.selectRepresentative()
        self.selectShares(index=2)
        self.selectCmpLocation()
        self.selectCmpNatture(index=2)
        self.inputCmpName(value=Data.cmp_name)
        self.selectCmpRadeArea(index=2)
        self.inputCmpAdress(value='企业主-某市上大路1000号中银大厦')
        self.inputCmpEmpAmt(value='1000')
        self.selectCmpType(index=5)
        self.selectCmpYearBill(index=3)
        self.selectCmpToPrivate(index=3)
        self.selectCmpToPublic(index=3)
        self.selectCmpRetainedProfits(index=5)
        self.selectCmpLiabilityRate(index=2)
        self.selectCmpLicense(index=2)
        self.selectCmpSignAmount(index=4)
        self.inputCmpYearTurnOverAmount(value='555')
        self.selectCmpIncomeAmount(index=3)

        '''股权信息'''
        self.gotoEqutyDetail(getWay='xpath')
        self.selectPaiedSecurityForEmp()
        self.selectCmpFounderBackground(index=3)
        self.selectCmpInstShareholders()
        self.selectCmpHighTechEnter()
        self.inputCmpYearInComeRate(value='20.58')
        self.selectCmpIndustrySg(index=5)

        '''信用和负债信息'''
        self.gotoCriditDetail(getWay='xpath')
        self.selectCreditCardAmt(index=6)
        self.inputCreditCount(value='3')
        self.selectPerCreditCardMaxAmt(index=3)
        self.selectCreditCardUsedAmt(index=4)
        self.selectBanks1()
        self.selectBanks2()
        self.selectBanks3()
        self.selectOtherBanks()
        self.inputOtherBank(value='花旗银行')
        self.selectPersonCredit(index=6)
        self.inputOverTime1(value='2')
        self.inputOverTime2(value='3')
        self.inputOverTime3(value='4')
        self.inputOverTime4(value='6')
        self.inputTwoOverTime(value='10')
        self.selectPairCredit(index=3)
        self.selectCmpCredit(index=5)
        self.inputCmpOverTimeCount(value='5')
        self.inputCmpMaxOverTimes(value='4')
        self.selectPersonDebt()
        self.selectCmpDebt()

        '''房产信息'''
        self.gotoHouseDetail(getWay='xpath')
        self.setIsHasHouse()
        self.setIsHasBackupHouse()
        self.selectHouseType(index=3)
        self.selectHouseProperty(index=2)
        self.selectHouseLocation(index=3)
        self.selectHouseSqure(index=4)
        self.inputHouseAddress(value='上海市黄兴花园15栋601室')
        self.setIsHasHouseLicense()
        self.inputHouseAmout(value='150')
        self.selectHouseEvalution(index=5)
        self.inputHouseAge(value='50')
        self.selectHouseImpawn(index=2)
        self.inputHouseLoanBlance(value='123.5')
        self.selectHouseRepayAmt(index=3)
        self.selectHouseReturnAmt(index=4)
        self.setIsHasHouseOtherOwner()
        self.setIsHasHouseChildOwner()
        self.setIsAllHouseOwnerSigned()

        '''车产信息'''
        self.gotoCarDetail(getWay='xpath')
        self.setIsHasCar()
        self.setIsSecondCar()
        self.selectCarProvince(index=3)
        self.selectCarCity(index=1)
        self.inputCarBuyAmt(value='200')
        self.selectCarAge(index=1)
        self.selectCarDistance(index=3)
        self.selectCarAssesment(index=4)
        self.selectCarLoanStatus(index=2)
        self.selectCarPerMouthPayAmt(index=2)
        self.selectCarPaiedMouth(index=3)
        self.inputCarRestLoanAmt(value='20')

        '''设备信息'''
        self.gotoEquipDetail(getWay='xpath')
        self.setIsHasEquipment()
        self.inputEquipAge(value='40')
        self.inputEquipNowAmt(value='220')
        self.inputEquipBuyAmt(value='1000')
        self.setIsHasInvoice()
        self.selectEquipMortgage(index=2)

        '''保单信息'''
        self.gotoInsuranceDetail(getWay='xpath')
        self.setIsHasInsurance()
        self.selectInsureTpye(index=1)
        self.setIsInsureStopPay()
        self.selectInsurePayTpye(index=1)
        self.inputInsureEffectTime(value='20')
        self.inputInsurePaiedMonths(value='10')
        self.inputInsurePerMounthAmt(value='2500')
        self.setIsInsurePayOff()
        self.selectInsurePerson(index=1)
        self.selectInsureCmp(index=5)

        '''其他资产'''
        self.gotoOtherAssetDetail(getWay='xpath')
        self.selectOtherAsset1()
        self.selectOtherAsset2()

        '''担保信息'''
        self.gotoGurantDetail(getWay='xpath')
        self.setIsHasGuarantee()
        self.selectGuarantorAdvantage1()
        self.selectGuarantorAdvantage2()
        self.setIsSpouseSign()

        '''补充信息'''
        self.gotoAdditionInfoDetail(getWay='xpath')
        # self.selectOtherInfo1()
        # self.selectOtherInfo2()
        # self.selectOtherInfo3()
        # self.selectOtherInfo4()

        '''提交'''
        self.submitFinceBookInfo()

    # ============================================================================================
    # 验证case的执行结果
    search_cltname_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[1]/td/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[3]/div') #列表页客户名称
    def verify_finceBookInfo_save_success(self):
        return  self.find_element(*self.search_cltname_loc).text


