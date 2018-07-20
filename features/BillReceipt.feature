# Created by kun yang at 2018/7/10

@bill_recept
Feature: 收款单管理

  @create_aim_bill
  Scenario: 创建意向金收款单
    Given 分公司财务登录融管系统
    When 进入【出纳】-【收款单管理】点击【新增】按钮，交易类型选择：意向金，创建收款单
    Then 收款单创建成功

  @create_service_bill
  Scenario: 创建服务费收款单
    Given 分公司财务登录融管系统
    When 进入【出纳】-【收款单管理】点击【新增】按钮，交易类型选择：服务费，创建收款单
    Then 收款单创建成功

  @calculate_bill
  Scenario: 结算收款单
    Given 分公司财务登录融管系统
    When 进入【出纳】-【收款单管理】输入合同号查询收款单，点击【结算】按钮结算收款单
    Then 收款单结算成功