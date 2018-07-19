# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: Administrator
'''
import random

class Data:

#===============测试角色=========================================
    sales = 'yanfang'  #融资顾问
    sales_manager= 'wangweiwei' #销售经理
    service_manager = 'xuweilan'#融服经理
    ser_director_manager = 'yanghongyuan'#融资总监
    city = 'suzhou'

#===============客户详情=========================================
    lnk_moblie = '15928369517'
    sub_s = lnk_moblie[7:]
    lnk_name = '自动化联系人' + sub_s
    cmp_name = '需求书修改有限公司'+ lnk_moblie
    #cmp_name = '需求书修改有限公司18577788899'

#===============合同归档=========================================
    #合同打回、作废原因
    finance_name = 'sunquan'
    ctr_reject_memo = '自动化测试打回合同'
    ctr_discar_memo = '自动化测试作废合同'
    ContractCode = 'HY05122018000017'
    #ContractCode ='WB05122018000207'

#===============融资订单=========================================
    #意向单
    org_name = '浦发银行'
    prd_name = '线上万用金'
    credit_manager = '令磊'

    #融资喜报审批
    chanl_clt_name = '需求书修改有限公司'+ lnk_moblie
    #chanl_clt_name = '需求书修改有限公司108'
    fin_clt_name = '需求书修改有限公司'+lnk_moblie
    #fin_clt_name = '需求书修改有限公司108'

#===============操作客户========================================
    #客户释放公海
    share_phone1 = random.randint(10000000000, 19999999999)
    share_phone2 = random.randint(10000000000, 19999999999)
    share_phone3 = random.randint(10000000000, 19999999999)

    #删除客户
    delete_phone1 = random.randint(10000000000, 19999999999)
    delete_phone2 = random.randint(10000000000, 19999999999)

    #划转至大项目部
    move_client_phone = random.randint(10000000000, 19999999999)

#===============退费流程=========================================
    #强制退费
    force_clt_name = '需求书修改有限公司106'

    #销售喜报
    sal_clt_name = '需求书修改有限公司124'

    #紧急退费
    ur_clt_name = '需求书修改有限公司106'

#==========================================================================================================
#    执行feature 文件的标签（tags）顺序
#===========================================================================================================
# behave --tags=user_login,createNewClient,myclient,finance_book,create_come_intview,approve_intview,create_vip_contract,arc_vip_contract_cmp,create_salesOrder_cmp,salesOrder_oprate,my_order












