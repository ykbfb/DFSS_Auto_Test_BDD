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
#---------------------------------------------------------------------
#定位动态id、name元素
# driver.find_element_by_xpath("//iframe[contains(@id, 'layui-layer-iframe')]")
# driver.find_element_by_xpath("//div[starts-with(@id, 'btn-attention')]")
# driver.find_element_by_xpath("//div[ends-with(@id, 'btn-attention')]")
# --==================================================================

from selenium.webdriver.common.by import By
from .base import Page
from test_case.models import settings
import time

class ServiceManageOrderPage(Page):
    #融资订单管理
    order_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]') #融资订单管理
    my_order_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[1]/div/a/span[2]')#我的订单
    order_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    cmp_name_loc = (By.XPATH,'//*[@id="div_cpname"]/input') #客户名称、姓名
    search_loc = (By.XPATH,'//*[@id="main"]/form/div/div/div[2]/div[1]') #查询
    recive_order_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[12]/input[1]') #接单按钮
    pop_frame_loc = '//*[@id="layui-layer3"]/div[2]/iframe'#弹窗frame
    submit_loc = (By.XPATH,'//*[@id="main"]/form/table/tbody/tr[6]/td/input')

    market_amt_loc = '//*[@id="ContractInfo"]/table/tbody/tr[9]/td'
    scroll_submit_loc = '//*[@id="main"]/form/table/tbody/tr[6]/td/input'
    pop_close_btn_loc = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]') #弹出框： 【确定】 按钮
    accpt_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确认


    # ===================================================================================================
    #打开我的订单
    #====================================================================================================
    def gotoMyOrder(self):
        time.sleep(1)
        self.find_element(*self.order_nav_loc).click()
        self.setWaitTime(10)
        self.find_element(*self.my_order_loc).click()
        time.sleep(1)
        self.switchToDefaultContent()
        self.switchToOneFrameByXpath(self.order_list_frame_loc)

    #===================================================================================================
    #接单
    #===================================================================================================
    def acceptOrder(self,cmp_name):
        '''待处理-查询订单'''
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        self.find_element(*self.cmp_name_loc).clear()
        self.find_element(*self.cmp_name_loc).send_keys(cmp_name)
        self.find_element(*self.search_loc).click()
        time.sleep(2)

        '''接单页面确认'''
        self.find_element(*self.recive_order_loc).click()
        # time.sleep(1)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.pop_frame_loc)
        self.scrollToElement('xpath',self.scroll_submit_loc)
        self.find_element(*self.submit_loc).click()

        '''确认提交订单'''
        self.switchWindow()
        time.sleep(1)
        self.find_element(*self.pop_close_btn_loc).click()
        time.sleep(1)
        self.switchWindow()
        self.click_element(*self.accpt_confirm_loc)
        time.sleep(1)

    #=======================================================================================================
    #【贷前调查】 转入 【专家测评】
    #=======================================================================================================
    pre_loan_inv_loc = (By.XPATH,'//*[@id="ulType"]/li[2]') #贷前调查
    clt_name_loc = (By.XPATH,'//*[@id="div_cpname"]/input') #客户名称
    pre_search_loc = (By.XPATH,'//*[@id="main"]/form/div/div/div[2]/div[1]')#查询
    movetoExpert_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[17]/input') #转入专家测评
    confirm_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    memo_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[1]/td[2]/textarea')
    confirm_btn_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[2]/td/button')

    def moveToExpert(self,cmp_name):
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        self.find_element(*self.pre_loan_inv_loc).click()
        time.sleep(1)
        self.find_element(*self.clt_name_loc).clear()
        self.find_element(*self.clt_name_loc).send_keys(cmp_name)
        time.sleep(2)
        self.find_element(*self.pre_search_loc).click()
        time.sleep(2)
        self.find_element(*self.movetoExpert_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.confirm_frame_loc)
        self.find_element(*self.memo_loc).clear()
        self.find_element(*self.memo_loc).send_keys('自动化测试--转入专家测评')
        self.find_element(*self.confirm_btn_loc).click()
        time.sleep(1)
        self.close_alert()
        time.sleep(1)

#========================================================================================================
#【专家测评】转入【机构寻访】
#========================================================================================================
    exprt_tab_loc = (By.XPATH,'//*[@id="ulType"]/li[3]') #专家测评
    expert_clt_name_loc = (By.XPATH,'//*[@id="div_cpname"]/input') #客户名称
    exprt_search_loc = (By.XPATH,'//*[@id="main"]/form/div/div/div[2]/div[1]')#查询
    moveToAgency_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[16]/input')#转入机构寻访
    exp_pop_iframe_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    exp_memo_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[1]/td[2]/textarea')#备注
    exp_submit_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[2]/td/button')#提交

    def moveToAgencySearch(self,cmp_name):
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        time.sleep(1)
        self.find_element(*self.exprt_tab_loc).click()
        time.sleep(1)
        self.find_element(*self.expert_clt_name_loc).clear()
        self.find_element(*self.expert_clt_name_loc).send_keys(cmp_name)
        time.sleep(2)
        self.find_element(*self.exprt_search_loc).click()
        time.sleep(2)
        self.find_element(*self.moveToAgency_loc).click()
        self.setWaitTime(10)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.exp_pop_iframe_loc)
        self.find_element(*self.exp_memo_loc).clear()
        self.find_element(*self.exp_memo_loc).send_keys('自动化测试--转入机构寻访')
        self.find_element(*self.exp_submit_loc).click()
        time.sleep(1)
        self.close_alert()
        time.sleep(1)

#==========================================================================================================
#机构寻访中创建意向单
#=========================================================================================================
    agency_tab_loc = (By.XPATH,'//*[@id="ulType"]/li[4]')#专家测评
    agen_clt_name_loc = (By.XPATH,'//*[@id="div_cpname"]/input')#客户名称
    agen_search_loc = (By.XPATH,'//*[@id="main"]/form/div/div/div[2]/div[1]')#查询
    agen_evalu_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[11]/span/input')#预测评
    agen_pop_iframe_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"#弹窗的iframe
    np_comfirm_loc = (By.XPATH,'//*[@id="layui-layer2"]/div[3]/a') #没有合适的产品
    add_more_prd_loc = (By.ID,'Add_More')#添加更多产品
    org_name_loc = (By.XPATH,'//*[@id="td_OrgName"]/span/input[1]')#机构名称
    sel_org_loc = (By.ID,'_easyui_combobox_86')#下拉框选择机构
    # sel_org_loc = (By.XPATH,'//id[contains(@id, "_easyui_combobox"')#下拉框选择机构
    prd_name_loc = (By.XPATH,'//*[@id="td_PrdName"]/span/input[1]')#产品名称
    sel_prd_loc = (By.ID,'_easyui_combobox_277')#选择产品
    add_prd_reason_loc = (By.ID,'addReason')#添加理由
    add_btn_loc = (By.ID,'btn_addMore')#添加按钮
    show_search_btn_loc = (By.ID,'btnSearchCondition')#显示查询条件
    fruzzy_search_loc = (By.ID,'searchText')#模糊匹配
    #sel_credit_manager_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[1]/div/img')#展开信贷经理
    #sel_credit_manager_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[3]/td[1]/div[1]')
    sel_credit_manager_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[4]/td[1]/div')#展开信贷经理
    sel_all_loc = (By.CLASS_NAME,'_selectall')#全选
    send_aim_order_loc = (By.ID,'btn_SendYXD')#发送意向单
    continue_send_loc = (By.ID,'continueSend')#继续发送
    confirm_aim_loc = (By.CLASS_NAME,'layui-layer-btn0')#确认
    sec_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确定
    close_win_loc = (By.XPATH,'/html/body/div[4]/span[1]/a[3]')#关闭意向单管理页面


    def createAimOrder(self,cmp_name,org_name,prd_name):
        self.cmp_name = cmp_name
        self.org_name = org_name
        self.prd_name = prd_name
        self.gotoMyOrder()
        time.sleep(1)
        self.find_element(*self.agency_tab_loc).click()
        time.sleep(2)
        self.find_element(*self.agen_clt_name_loc).clear()
        self.find_element(*self.agen_clt_name_loc).send_keys(cmp_name)
        self.find_element(*self.agen_search_loc).click()
        time.sleep(2)

        '''打开预测评'''
        self.find_element(*self.agen_evalu_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.agen_pop_iframe_loc)
        self.setWaitTime(20)
        time.sleep(2)
        # self.find_element(*self.np_comfirm_loc).click()
        # time.sleep(2)
        # self.switchWindow()

       #===============================================================================================
        # '''添加更多产品'''
        # self.find_element(*self.add_more_prd_loc).click()
        # self.switchWindow()
        # self.find_element(*self.org_name_loc).clear()
        # self.find_element(*self.org_name_loc).send_keys(org_name)
        # time.sleep(1)
        # self.find_element(*self.sel_org_loc).click() #选择机构
        # time.sleep(1)
        # self.find_element(*self.prd_name_loc).clear()
        # self.find_element(*self.prd_name_loc).send_keys(prd_name)
        # time.sleep(2)
        # self.find_element(*self.sel_prd_loc).click() #选择产品
        # self.find_element(*self.add_prd_reason_loc).clear()
        # self.find_element(*self.add_prd_reason_loc).send_keys('自动化测试--产品添加理由： are you ok')
        # self.find_element(*self.add_btn_loc).click()
        # time.sleep(1)
       #===============================================================================================================

        '''发送意向单'''
        # self.click_element(*self.show_search_btn_loc)
        # time.sleep(1)
        # self.scrollToElement_new(*self.fruzzy_search_loc)
        # self.input_value(self.fruzzy_search_loc,prd_name)
        # time.sleep(5)
        # self.scrollToElement_new(*self.sel_credit_manager_loc)
        self.find_element(*self.sel_credit_manager_loc).click()
        time.sleep(1)
        self.find_element(*self.sel_all_loc).click()
        self.find_element(*self.send_aim_order_loc).click()
        self.switchWindow()
        time.sleep(1)
        self.find_element(*self.continue_send_loc).click()
        time.sleep(1)
        self.switchWindow()
        self.find_element(*self.confirm_aim_loc).click()
        time.sleep(1)
        # self.switchToParentFrame()
        # self.switchWindow()
        # self.click_element(*self.sec_confirm_loc)
        # time.sleep(1)
        self.switchWindow()
        self.switchToParentFrame()
        self.click_element(*self.close_win_loc)


#====================================================================================================
#创建子订单
#====================================================================================================
    aim_order_mng_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[11]/input')#意向单管理
    sub_pop_iframe_loc =  "//iframe[contains(@id, 'layui-layer-iframe')]"
    credit_manage_loc = (By.ID,'txt_BCName')#信贷经理
    sub_org_name_loc = (By.ID,'txt_OrgName')#机构名称
    sub_search_loc = (By.ID,'btncheck')#查询
    createSubOrder_btn_loc = (By.XPATH,'//*[@id="datagrid-row-r2-2-0"]/td[1]/div/input[1]')#创建子订单
    suborder_det_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    evaluation_amt_loc = (By.ID,'evaluation')#预估额度
    eavlu_date_loc = 'EstimateAmountTime'#预计放款时间
    sub_submit_loc = (By.XPATH,'//*[@id="main"]/form/table/tbody/tr[7]/td/input')#提交
    move_sub_submit_loc = '//*[@id="main"]/form/table/tbody/tr[7]/td/input'
    sub_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确定
    fin_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确定

    def createSubOrder(self,cmp_name,credit_manager,org_name):
        self.cmp_name = cmp_name
        self.credit_manager = credit_manager
        self.org_name = org_name
        self.gotoMyOrder()
        time.sleep(1)
        self.find_element(*self.agency_tab_loc).click()
        self.setWaitTime(20)
        time.sleep(1)
        self.find_element(*self.agen_clt_name_loc).clear()
        self.find_element(*self.agen_clt_name_loc).send_keys(cmp_name)
        self.find_element(*self.agen_search_loc).click()
        time.sleep(1)

        '''打开意向单管理'''
        self.find_element(*self.aim_order_mng_loc).click()
        self.switchWindow()
        time.sleep(2)
        self.switchToOneFrameByXpath(self.sub_pop_iframe_loc)
        self.find_element(*self.credit_manage_loc).clear()
        self.find_element(*self.credit_manage_loc).send_keys(credit_manager)
        self.find_element(*self.sub_org_name_loc).clear()
        self.find_element(*self.sub_org_name_loc).send_keys(org_name)
        self.setWaitTime(1)
        self.find_element(*self.sub_search_loc).click()
        time.sleep(1)
        '''创建子订单'''
        self.find_element(*self.createSubOrder_btn_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.suborder_det_loc)
        self.scrollToElement('xpath',self.move_sub_submit_loc)
        self.find_element(*self.evaluation_amt_loc).clear()
        self.find_element(*self.evaluation_amt_loc).send_keys(50)
        self.getDateTimePicker(self.eavlu_date_loc,time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.find_element(*self.sub_submit_loc).click()
        time.sleep(1)
        self.switchWindow()
        self.find_element(*self.sub_confirm_loc).click()
        time.sleep(2)
        self.switchWindow()
        self.click_element(*self.fin_confirm_loc)

#=============================================================================================================
#子订单：【贷前辅导】转入【机构审批】
#=============================================================================================================
    pre_loan_coach_loc = (By.XPATH,'//*[@id="ulType"]/li[5]')#贷前辅导
    coach_clt_name_loc = (By.XPATH,'//*[@id="div_cpname"]/input')#客户名称
    coach_search_loc = (By.XPATH,'//*[@id="main"]/form/div/div/div[2]/div[1]')#查询
    movetoOrgAppr_loc = (By.CLASS_NAME,'btn_zjcp')#转入机构审批
    coach_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    coach_memo_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[1]/td[2]/textarea')#备注
    coach_submit_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[2]/td/button')#提交

    def moveToOrgApproval(self,cmp_name):
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        time.sleep(1)
        self.find_element(*self.pre_loan_coach_loc).click()
        self.setWaitTime(10)
        time.sleep(1)
        self.find_element(*self.coach_clt_name_loc).clear()
        self.find_element(*self.coach_clt_name_loc).send_keys(cmp_name)
        self.find_element(*self.coach_search_loc).click()
        time.sleep(1)

        self.find_element(*self.movetoOrgAppr_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.coach_frame_loc)
        self.find_element(*self.coach_memo_loc).clear()
        self.find_element(*self.coach_memo_loc).send_keys('自动化测试--【贷前辅导】转入【机构审批】')
        self.find_element(*self.coach_submit_loc).click()
        time.sleep(1)
        self.close_alert()
        time.sleep(1)

#======================================================================================================================
#【机构审批】
#======================================================================================================================
    orgApproval_tab_loc = (By.XPATH,'//*[@id="ulType"]/li[6]')#机构审批
    org_clt_name_loc = (By.XPATH,'//*[@id="div_cpname"]/input')#客户名称
    org_search_loc = (By.XPATH,'//*[@id="main"]/form/div/div/div[2]/div[1]')#查询
    credit_estimat_loc = (By.CLASS_NAME,'btn_pj')#评价
    estimate_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    estimate_totalScrore_loc = (By.XPATH,'//*[@id="comment_wrap"]/table/tbody/tr[1]/td[2]/ul/li[5]/img')#总体评分
    estimate_attituteScore_loc = (By.XPATH,'//*[@id="comment_wrap"]/table/tbody/tr[2]/td[2]/ul/li[5]/img')#服务态度
    estimate_speedScore_loc = (By.XPATH,'//*[@id="comment_wrap"]/table/tbody/tr[3]/td[2]/ul/li[5]/img')#办理速度
    estimate_skillScore_loc = (By.XPATH,'//*[@id="comment_wrap"]/table/tbody/tr[4]/td[2]/ul/li[5]/img')#专业技能
    estimate_memo_loc = (By.ID,'remarkInfo')#评价内容
    estimate_submit_loc = (By.ID,'SubBtn')#提交


    def estimateCreditManager(self,cmp_name):
        '''信贷经理评价'''
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        time.sleep(2)
        self.find_element(*self.orgApproval_tab_loc).click()
        self.setWaitTime(10)
        time.sleep(1)
        self.find_element(*self.org_clt_name_loc).clear()
        self.find_element(*self.org_clt_name_loc).send_keys(cmp_name)
        self.find_element(*self.org_search_loc).click()
        time.sleep(1)

        self.find_element(*self.credit_estimat_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.estimate_frame_loc)
        self.find_element(*self.estimate_totalScrore_loc).click()
        self.find_element(*self.estimate_attituteScore_loc).click()
        self.find_element(*self.estimate_speedScore_loc).click()
        self.find_element(*self.estimate_skillScore_loc).click()
        self.find_element(*self.estimate_memo_loc).clear()
        self.find_element(*self.estimate_memo_loc).send_keys('自动化测试--信贷经理评价')
        self.find_element(*self.estimate_submit_loc).click()
        time.sleep(2)
        self.close_alert()

#-----------------------------------------------------------------------------------------------
    org_approve_loc = (By.CLASS_NAME,'btn_oa')#机构审批
    org_appr_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    org_appr_pass_loc = (By.XPATH,'//*[@id="divMng"]/table/tbody/tr[1]/td/input[1]')#通过
    org_appr_reject_loc = (By.XPATH,'//*[@id="divMng"]/table/tbody/tr[1]/td/input[2]')#不通过
    org_appr_amt_loc = (By.ID,'txtAmount')#审批金额
    org_appr_memo_loc = (By.ID,'txtMemo')#备注
    org_appr_submit_loc = (By.XPATH,'//*[@id="trSubmit"]/td/input')#提交
    org_appr_confirm_loc = (By.XPATH,'//*[@id="layui-layer1"]/div[3]/a')#确认

    def orgApprovePass(self,cmp_name):
        '''机构审批--通过'''
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        time.sleep(1)
        self.find_element(*self.orgApproval_tab_loc).click()
        self.setWaitTime(10)
        time.sleep(1)
        self.find_element(*self.org_clt_name_loc).clear()
        self.find_element(*self.org_clt_name_loc).send_keys(cmp_name)
        self.find_element(*self.org_search_loc).click()
        time.sleep(1)

        self.find_element(*self.org_approve_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.org_appr_frame_loc)
        time.sleep(2)
        self.find_element(*self.org_appr_pass_loc).click()
        self.find_element(*self.org_appr_amt_loc).clear()
        self.find_element(*self.org_appr_amt_loc).send_keys(55)
        self.find_element(*self.org_appr_memo_loc).clear()
        self.find_element(*self.org_appr_memo_loc).send_keys('自动化测试--机构审批： 通过')
        self.find_element(*self.org_appr_submit_loc).click()
        self.switchWindow()
        self.find_element(*self.org_appr_confirm_loc).click()

    def orgApproveReject(self,cmp_name):
        '''机构审批--不通过'''
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        time.sleep(1)
        self.find_element(*self.orgApproval_tab_loc).click()
        self.setWaitTime(10)
        time.sleep(1)
        self.find_element(*self.org_clt_name_loc).clear()
        self.find_element(*self.org_clt_name_loc).send_keys(cmp_name)
        self.find_element(*self.org_search_loc).click()
        time.sleep(1)

        self.find_element(*self.org_approve_loc).click()
        self.switchWindow()
        self.switchToOneFrameByXpath(self.org_appr_frame_loc)
        self.find_element(*self.org_appr_reject_loc).click()
        time.sleep(2)
        self.find_element(*self.org_appr_memo_loc).clear()
        self.find_element(*self.org_appr_memo_loc).send_keys('自动化测试--机构审批： 不通过')
        self.find_element(*self.org_appr_submit_loc).click()
        self.switchWindow()
        self.find_element(*self.org_appr_confirm_loc).click()

#-------------------------------------------------------------------------------------------------------------
#子订单放款，提交融资喜报
#-------------------------------------------------------------------------------------------------------------
    dealwith_loc = (By.CLASS_NAME,'btn_txcl')#填写处理
    org_deal_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    org_deal_desc_loc = (By.ID,'handwords')#处理进度描述
    moveto_deal_desc_loc = 'handwords'
    org_deal_success_loc = (By.ID,'chkChengjiao')#成交
    org_deal_submit_loc = (By.ID,'selectedyes')#确定

    def submitChanelResult(self,cmp_name):
        '''子订单成交--提交融资喜报'''
        self.cmp_name = cmp_name
        self.gotoMyOrder()
        time.sleep(1)
        self.find_element(*self.orgApproval_tab_loc).click()
        self.setWaitTime(10)
        time.sleep(1)
        self.find_element(*self.org_clt_name_loc).clear()
        self.find_element(*self.org_clt_name_loc).send_keys(cmp_name)
        self.find_element(*self.org_search_loc).click()
        time.sleep(2)

        self.find_element(*self.dealwith_loc).click()#填写处理
        self.switchWindow()
        self.switchToOneFrameByXpath(self.org_deal_frame_loc)
        self.scrollToElement('id',self.moveto_deal_desc_loc)
        self.find_element(*self.org_deal_desc_loc).clear()
        self.find_element(*self.org_deal_desc_loc).send_keys('自动化测试--子订单成交')
        self.find_element(*self.org_deal_success_loc).click()
        self.find_element(*self.org_deal_submit_loc).click()
        time.sleep(1)
        self.close_alert()
        time.sleep(2)
        self.switchToParentFrame()   #注意： 如果弹出的窗口跳出了它原本所在的iframe，即悬浮在外层的iframe，则只需将iframe切换到他的上层iframe即可用switch_to.window切换到弹出窗口 进行定位
        self.switchWindow()
        self.inputChanalResultDetail()

#------------------------------------------------------------------------------------------------
    #放款喜报填写详情页
    chanel_result_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    loan_total_amt_loc = (By.ID,'LendingTotal')#放款额度
    loan_org_rate_loc = (By.ID,'txtOrgRate')#机构放款费率
    loan_rate_type_loc = 'sltOrgRateType'#利率类型
    loan_org_other_rate_loc = (By.ID,'txtOrgOtherRate')#机构放款其他费率
    loan_other_rate_type_loc = 'sltOrgOtherRateType'#其他利率类型
    loan_repay_type_loc = 'sel_RePayType'#还款方式
    loan_oprate_type_loc = 'sel_DealWith'#办理方式
    loan_certicate_loc = 'UploadInput'#放款凭证
    upload_sucess_loc =(By.CLASS_NAME,'layui-layer-btn0')
    loan_startdate_loc = 'txtLendingDate'#放款期限： 起始日期
    loan_enddate_loc = 'txtLendingDateEnd'#放款期限： 结束日期
    loan_lend_date_loc = 'txtLendDateTime'#放款时间
    bank_CardNo_loc = (By.ID,'txt_BankCardNum')#银行卡号
    bank_card_phone_loc = (By.ID,'txt_BankCardCellphone')#银行卡对应手机号
    bank_name_loc = (By.ID,'txt_OpenBank')#开户银行
    bank_card_photo_loc = '//*[@id="pickerBankCardPhotographFile"]/div[2]/input'#银行卡拍照附件
    bank_card_upload_btn_loc = (By.ID,'btnUpload_pickerBankCardPhotographFile')#上传
    confirm_info_attch_loc = (By.XPATH,'//*[@id="pickerInfoServiceFile"]/div[2]/input')#信息服务确认书
    confirm_info_upload_loc = (By.ID,'btnUpload_pickerInfoServiceFile')#上传
    loan_memo_loc = (By.ID,'Memo')#备注
    loan_submit_loc = (By.XPATH,'//*[@id="main"]/div[1]/div/table/tbody/tr[2]/td[1]/input')#提交审核
    moveto_loan_submit_loc = '//*[@id="main"]/div[1]/div/table/tbody/tr[2]/td[1]/input'
    loan_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')#确认无误

    def inputChanalResultDetail(self):
        self.switchToOneFrameByXpath(self.chanel_result_pop_frame_loc)
        self.setWaitTime(10)
        self.find_element(*self.loan_total_amt_loc).clear()
        self.find_element(*self.loan_total_amt_loc).send_keys(500000)
        self.find_element(*self.loan_org_rate_loc).clear()
        self.find_element(*self.loan_org_rate_loc).send_keys(10)
        self.getDropdownMenuById(self.loan_rate_type_loc, 2)
        self.scrollToElement('xpath',self.moveto_loan_submit_loc)
        self.find_element(*self.loan_org_other_rate_loc).clear()
        self.find_element(*self.loan_org_other_rate_loc).send_keys(10)
        self.getDropdownMenuById(self.loan_other_rate_type_loc, 1)
        self.getDropdownMenuById(self.loan_repay_type_loc, 1)
        self.uploadFile('id',self.loan_certicate_loc,settings.Other_file)
        self.switchWindow()
        self.click_element(*self.upload_sucess_loc)
        self.getDropdownMenuById(self.loan_oprate_type_loc, 1)
        self.getDateTimePicker(self.loan_startdate_loc,time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.getDateTimePicker(self.loan_enddate_loc,time.strftime('%Y-%m-%d',time.localtime(time.time())))
        self.getDateTimePicker(self.loan_lend_date_loc,time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time())))
        self.input_value(self.bank_CardNo_loc,'1425368798651425470')
        self.input_value(self.bank_card_phone_loc,'16547586921')
        self.input_value(self.bank_name_loc,'苏州东坡银行')
        self.uploadFile('xpath',self.bank_card_photo_loc,settings.Other_file)
        self.click_element(*self.bank_card_upload_btn_loc)
        time.sleep(3)
        self.uploadFile2(self.confirm_info_attch_loc,settings.Other_file)
        time.sleep(1)
        self.click_element(*self.confirm_info_upload_loc)
        time.sleep(1)
        self.setWaitTime(20)
        self.find_element(*self.loan_memo_loc).clear()
        self.find_element(*self.loan_memo_loc).send_keys(10)
        self.find_element(*self.loan_submit_loc).click()
        time.sleep(2)
        self.switchWindow()
        self.find_element(*self.loan_confirm_loc).click()
        time.sleep(1)
        self.close_alert()

#=====================================================================================================================
#  校验case是否通过
#=====================================================================================================================
    acc_no_data_loc = (By.XPATH,'//*[@id="div_no"]/span')
    def verifyOrderAcceptSucess(self):
        '''校验接单成功'''
        self.switchToParentFrame()
        return self.find_element(*self.acc_no_data_loc).text


    preloan_no_data_loc = (By.XPATH,'//*[@id="div_no"]/span')
    def verifyOrderMovetoExprtSucess(self):
        '''校验转入专家测评成功'''
        self.switchToParentFrame()
        return self.find_element(*self.preloan_no_data_loc).text

    expert_no_data_loc = (By.XPATH,'//*[@id="div_no"]/span')
    def verifyOrderMovetoAgencyResearchSucess(self):
        '''校验转入机构寻访成功'''
        self.switchToParentFrame()
        return self.find_element(*self.expert_no_data_loc).text

    aim_order_cunt_loc = (By.ID,'AimSubOrderTotal_1')#意向单
    def verifyAimOrderCreateSucess(self):
        '''校验意向单是否创建成功'''
        self.switchToDefaultContent()
        self.switchToOneFrameByXpath(self.order_list_frame_loc)
        time.sleep(1)
        return self.find_element(*self.aim_order_cunt_loc).text

    order_detail_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[2]/td/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]/div/input[1]')
    #订单详情
    def verifySubOrderCreateSucess(self,credit_manager,org_name):
        '''校验子订单创建成功'''
        self.credit_manager = credit_manager
        self.org_name = org_name
        time.sleep(2)
        self.switchToParentFrame()
        self.input_value(self.credit_manage_loc,credit_manager)
        self.input_value(self.sub_org_name_loc,org_name)
        self.click_element(*self.sub_search_loc)
        time.sleep(1)
        print(self.find_element(*self.order_detail_loc).text)
        return  self.find_element(*self.order_detail_loc).text


