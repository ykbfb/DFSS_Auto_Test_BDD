# Created by Administrator at 2018/7/10

@my_order
Feature: 我的订单

  @service_accpt_order
  Scenario: 融服接单
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【待处理】页签，选择相应的主订单并点击【接单】按钮进行接单
    Then 融服接单成功

   @order_moveto_expert
   Scenario: 转入专家测评
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【贷前调查】页签，选择相应的主订单并点击【转入专家测评】按钮
    Then 订单进入专家测评

  @order_moveto_agency
  Scenario: 转入机构寻访
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【专家测评】页签，选择相应的主订单并点击【转入机构寻访】按钮
    Then 订单进入机构寻访

  @create_aim_order
  Scenario: 创建意向单
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【机构寻访】页签，选择主订单并点击【智能融顾】按钮，选择相应的产品点击【发送意向单】
    Then 意向单创建成功

  @create_sub_order
  Scenario: 创建子订单
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【机构寻访】页签，选择主订单并点击【意向单管理】按钮，选择相应的意向单，点击【创建子订单】按钮进行子订单创建
    Then 子订单创建成功

  @suborder_moveto_org_appv
  Scenario: 子订单转入机构审批
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【贷前辅导】页签，选择子订单并点击【转入机构审批】按钮

  @estimate_credit_manager
  Scenario: 融服评价信贷经理
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【机构审批】页签，选择子订单并点击【评价】按钮对信贷经理进行评价

  @org_appv_notpass
  Scenario: 机构审批不通过
    Given 融服登录融管系统
    When 机构审批不通过：打开【融资订单管理】→【我的订单】→【机构审批】页签，选择子订单并点击【机构审批结果】按钮记录审批详情

  @org_appv_pass
  Scenario: 机构审批通过
    Given 融服登录融管系统
    When 机构审批通过：打开【融资订单管理】→【我的订单】→【机构审批】页签，选择子订单并点击【机构审批结果】按钮记录审批详情

  @submit_chanal_result
  Scenario: 融服提交喜报
    Given 融服登录融管系统
    When 打开【融资订单管理】→【我的订单】→【机构审批】页签，选择子订单并点击【填写处理】按钮,选择成交并填写喜报详情


