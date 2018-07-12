# Created by kun yang at 2018/7/10
Feature: 收款单管理

  Scenario: 创建收款单
    Given 分公司财务登录融管系统
    When 进入【出纳】-【收款单管理】点击【新增】按钮创建收款单
    Then 收款单创建成功

  Scenario: 结算收款单
    Given 分公司财务登录融管系统
    When 进入【出纳】-【收款单管理】输入合同号查询收款单，点击【结算】按钮结算收款单
    Then 收款单结算成功