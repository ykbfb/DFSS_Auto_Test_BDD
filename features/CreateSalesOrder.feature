# Created by Administrator at 2018/7/10

@create_salesOrder
Feature: 创建销售订单
  # Enter feature description here

  @create_salesOrder_cmp
  Scenario: 创建企业主、个体户销售订单
    Given 销售顾问登录融管系统
    When 查询销售订单客户
    When 创建企业主销售订单：打开【销售订单管理】点击【创建销售订单】按钮，输入销售订单详情并提交
    Given 销售顾问登录融管系统
    When 查询销售订单客户
    Then 销售订单创建成功

  @create_salesOrder_person
  Scenario: 创建工薪族、其他销售订单
    Given 销售顾问登录融管系统
    When 查询销售订单客户
    When 创建工薪族销售订单：打开【销售订单管理】点击【创建销售订单】按钮，输入销售订单详情并提交
    Given 销售顾问登录融管系统
    When 查询销售订单客户
    Then 销售订单创建成功