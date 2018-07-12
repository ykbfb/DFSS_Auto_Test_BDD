# Created by Administrator at 2018/7/9

@finance_book
Feature: 需求书测试
  '''测试需求书修改、保存、提交等操作'''

  @save_fin_bookInfo
  Scenario: 保存需求书
    Given 登录融管系统
    When 查询客户
    When 修改需求书并保存
    Given 登录融管系统
    When 查询客户
    Then 需求书保存成功

  @submit_fin_bookInfo
  Scenario: 提交需求书
    Given 登录融管系统
    When 查询客户
    When 修改需求书并提交
    Given 登录融管系统
    When 查询客户
    Then 需求书提交成功