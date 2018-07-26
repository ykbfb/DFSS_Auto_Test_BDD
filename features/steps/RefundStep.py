import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.RefundPage import RefundPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

#=================================================================================================================================================
#   新退费
#=================================================================================================================================================
@When('打开【我的客户】→【合同管理】→【新合同】，点击【退款】按钮并填写退款详情，提交审核')
def step_createMenberRefund(context):
    '''顾问创建新退费'''
    refund = RefundPage(context.driver)
    refund.createRefund()
    functions.insert_img(context.driver, "CreateMemberRefund_"+current_time+".png")

@When('打开【销售管理】→【新退费审批--总监】→【待审批】，选择待审批的新退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def setp_impl(context):
    '''销售总监审批新退费'''
    refund = RefundPage(context.driver)
    refund.approveRefund_Director(Data.cmp_name)
    functions.insert_img(context.driver, "Director_ApproveMemberRefund_"+current_time+".png")

@When('打开【销售管理】→【新退费审批】→【待审批】，选择待审批的新退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def setp_impl(context):
    '''分总审批新退费'''
    refund = RefundPage(context.driver)
    refund.approveRefund_DivManager(Data.cmp_name)
    functions.insert_img(context.driver, "DivManager_ApproveMemberRefund_"+current_time+".png")

@When('打开【出纳】→【新退费审批】→【待审批】，选择待审批的新退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def setp_impl(context):
    '''分公司财务审批新退费'''
    refund = RefundPage(context.driver)
    refund.approveRefund_Finance(Data.cmp_name)
    functions.insert_img(context.driver, "Finance_ApproveMemberRefund_"+current_time+".png")

@When('打开【付款专员】→【新退费审批】→【待审批】，选择【城市】，选择待审批的新退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def setp_impl(context):
    '''总部应收会计审批新退费'''
    refund = RefundPage(context.driver)
    refund.approveRefund_Accountant(Data.cmp_name)
    functions.insert_img(context.driver, "Accountant_ApproveMemberRefund_"+current_time+".png")
    
@When('打开【CFO】→【新退费审批】→【待审批】，选择【城市】，选择待审批的新退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def step_impl(context):
    '''CFO审批新退费'''
    refund = RefundPage(context.driver)
    refund.approveRefund_CFO(Data.cmp_name)
    functions.insert_img(context.driver, "CFO_ApproveMemberRefund_"+current_time+".png")

@When('打开【钱智总部出纳】→【新退费审批】→【待审批】，选择【城市】，选择待审批的新退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def step_impl(context):
    '''总部付款出纳审批新退费'''
    refund = RefundPage(context.driver)
    refund.approveRefund_Cashier(Data.cmp_name)
    functions.insert_img(context.driver, "Cashier_ApproveMemberRefund_"+current_time+".png")
    
#===================================================================================================================================================
#  意向金退费
#===================================================================================================================================================
@When('打开【我的客户】→【合同管理】→【新合同】，在“意向金”列点击【退款】按钮并填写退款详情，提交审核')
def step_impl(context):
    refund = RefundPage(context.driver)
    refund.createAimRefund_Sales()
    functions.insert_img(context.driver, "CreateAimRefund_"+current_time+".png")
    
    
@When('打开【销售管理】→【意向金退款审批】→【待审批】，选择待审批的意向金退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def step_impl(context):
    refund = RefundPage(context.driver)
    refund.approveAimRefund_Director()
    functions.insert_img(context.driver, "Director_ApproveAimRefund_"+current_time+".png")
        
@When('打开【销售管理】→【意向金退费审批--分总】→【待审批】，选择待审批的意向金退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def step_impl(context):
    refund = RefundPage(context.driver)
    refund.approveAimRefund_DivManager()
    functions.insert_img(context.driver, "DivManager_ApproveAimRefund_"+current_time+".png")
    
@When('打开【出纳】→【意向金退费审批】→【待审批】，选择待审批的意向金退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def step_impl(context):
    refund = RefundPage(context.driver)
    refund.approveAimRefund_Finance()
    functions.insert_img(context.driver, "Finance_ApproveAimRefund_"+current_time+".png")
    
@When('打开【付款专员】→【意向金退费审批】→【待审批】，选择【城市】，选择待审批的意向金退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def step_impl(context):
    refund = RefundPage(context.driver)
    refund.approveAimRefund_Accountant()
    functions.insert_img(context.driver, "Accountant_ApproveAimRefund_"+current_time+".png")
                    
@When('打开【钱智总部出纳】→【意向金退费审批】→【待审批】，选择【城市】，选择待审批的意向金退费申请，点击【审批】，填写【审批意见】并点击【通过】按钮')
def step_impl(context):
    refund = RefundPage(context.driver)
    refund.approveAimRefund_Cashier()
    functions.insert_img(context.driver, "Cashier_ApproveAimRefund_"+current_time+".png")
    
#=================================================================================================================================================
#  紧急退费
#=================================================================================================================================================
@When('打开【销售管理】→【紧急退费发起】，选择要退费的合同，点击【退费】按钮,填写退费详情并提交审核')
def step_createUrgencyRefund_DivManager(context):
    # 创建紧急退费--分总
    refund = RefundPage(context.driver)
    refund.createUrgencyRefund(Data.cmp_name)
    functions.insert_img(context.driver, "CreateUrgencyRefund_"+current_time+".png")

@When('打开【出纳】→【紧急退费初审】→【待审批】，选择需要审批的紧急退费申请，点击【审批】按钮，并填写“审批意见”，点击【通过】按钮')
def step_approveUrgencyRefund_Finance(context):
    # 紧急退费审批--分公司财务
    refund = RefundPage(context.driver)
    refund.approveUrgencyRefund_Finance(Data.cmp_name)
    functions.insert_img(context.driver, "Finance_ApproveUrgencyRefund_"+current_time+".png")

@When('打开【付款专员】→【紧急退费审批】→【待审批】，选择需要审批的紧急退费申请，点击【审批】按钮，并填写“审批意见”，点击【通过】按钮')
def step_approveUrgencyRefund_Account(context):
    #紧急退费审批--总部应收会计
    refund = RefundPage(context.driver)
    refund.approveUrgencyRefund_Accountant(Data.cmp_name)
    functions.insert_img(context.driver, "Accounttant_ApproveUrgencyRefund_"+current_time+".png")
    refund.close()

@When('打开【CFO】→【紧急退费审批】→【待审批】，选择需要审批的紧急退费申请，点击【审批】按钮，并填写“审批意见”，点击【通过】按钮')
def step_approveUrgencyRefund_CFO(context):
    # 紧急退费审批--CFO
    refund = RefundPage(context.driver)
    refund.approveUrgencyRefund_CFO(Data.cmp_name)
    functions.insert_img(context.driver, "CFO_ApproveUrgencyRefund_"+current_time+".png")

@When('打开【钱智总部出纳】→【紧急退费审批】→【待审批】，选择需要审批的紧急退费申请，点击【审批】按钮，并填写“审批意见”，点击【通过】按钮')
def step_approveUrgencyRefund_Cashier(context):
    #紧急退费审批--总部付款出纳
    refund = RefundPage(context.driver)
    refund.approveUrgencyRefund_Cashier(Data.cmp_name)
    functions.insert_img(context.driver, "Cashier_ApproveUrgencyRefund_"+current_time+".png")

@When('打开【综合管理】→【紧急退费审批】→【待审批】，选择需要审批的紧急退费申请，点击【审批】按钮，并填写“审批意见”，点击【通过】按钮')
def step_approveUrgencyRefund_SalesManager(context):
    #紧急退费审批--销售经理
    refund = RefundPage(context.driver)
    refund.approveUrgencyRefund_SalesManager(Data.cmp_name)
    functions.insert_img(context.driver, "SalesManager_ApproveUrgencyRefund_"+current_time+".png")

@When('打开【出纳】→【紧急退费终审】→【待审批】，选择需要审批的紧急退费申请，点击【审批】按钮，并填写“审批意见”，点击【通过】按钮')
def step_finalApproveUrgencyRefund_Finance(context):
    #紧急退费终审--分公司财务
    refund = RefundPage(context.driver)
    refund.final_ApproveUrgencyRefund_Finance(Data.cmp_name)
    functions.insert_img(context.driver, "Finance_FinalApproveUrgencyRefund_"+current_time+".png")


#=================================================================================================================================================
#     投诉强制退费
#=================================================================================================================================================
@When('打开【投诉强制退费】→【强制退费发起】，选择需要退费的合同，点击【退费】按钮并填写退费详情，提交审核')
def step_createForceRefund_CustomerService(context):
    # 强制退费创建--客服专员
    refund = RefundPage(context.driver)
    refund.createForceRefund(Data.cmp_name)
    functions.insert_img(context.driver, current_time + "CreateForceRefund_"+current_time+".png")

@When('打开【客服专员】→【投诉强制退费审批】→【待审批】，选择要审批的强制退费申请，点击【审批】按钮并填写退费详情，提交审核')
def step_approveForceRefund_CustomerService(context):
    #强制退费审批--客服专员
    refund = RefundPage(context.driver)
    refund.approveForceRefund_CustomerScevice(Data.cmp_name)
    functions.insert_img(context.driver, "CustomerScevice_ApproveForceRefund_"+current_time+".png")

@When('打开【销售管理】→【投诉强制退费审批】→【待审批】，选择要审批的强制退费申请，点击【审批】按钮并填写审批意见，点击【通过】按钮')
def step_approveForceRefund_ServiceDirector(context):
    #强制退费审批--客服总监
    refund = RefundPage(context.driver)
    refund.approveForceRefund_ServiceDirector(Data.cmp_name)
    functions.insert_img(context.driver, "ServiceDirector_ApproveForceRefund_"+current_time+".png")

@When('打开【出纳】→【投诉强制退费审批】→【待审批】，选择要审批的强制退费申请，点击【审批】按钮并填写审批意见，点击【通过】按钮')
def step_approveForceRefund_Finance(context):
    # 强制退费审批--分公司财务
    refund = RefundPage(context.driver)
    refund.approveForceRefund_Finance(Data.cmp_name)
    functions.insert_img(context.driver, "Finance_ApproveForceRefund_"+current_time+".png")

@When('打开【付款专员】→【投诉强制退费审批】→【待审批】，选择要审批的强制退费申请，点击【审批】按钮并填写审批意见，点击【通过】按钮')
def step_approveForceRefund_Accountant(context):
    # 强制退费审批--总部应收会计
    refund = RefundPage(context.driver)
    refund.approveForceRefund_Accountant(Data.cmp_name)
    functions.insert_img(context.driver, "Accountant_ApproveForceRefund_"+current_time+".png")

@When('打开【CFO】→【投诉强制退费审批】→【待审批】，选择要审批的强制退费申请，点击【审批】按钮并填写审批意见，点击【通过】按钮')
def step_approveForceRefund_CFO(context):
    # 强制退费审批--CFO
    refund = RefundPage(context.driver)
    refund.approveForceRefund_CFO(Data.cmp_name)
    functions.insert_img(context.driver, "CFO_ApproveForceRefund_"+current_time+".png")

@When('打开【钱智总部出纳】→【投诉强制退费审批】→【待审批】，选择要审批的强制退费申请，点击【审批】按钮并填写审批意见，点击【通过】按钮')
def step_approveForceRefund_Cashier(context):
    # 强制退费审批--总部付款出纳
    refund = RefundPage(context.driver)
    refund.approveForceRefund_Cashier(Data.cmp_name)
    functions.insert_img(context.driver, "Cashier_ApproveForceRefund_"+current_time+".png")

































































