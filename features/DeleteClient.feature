# Created by kun yang at 2018/7/19
Feature: 删除客户

  Scenario: 列表页右键删除客户
    Given 销售顾问登录融管系统
    When 创建共享客户1
    Given 销售顾问登录融管系统
    When 查询共享客户1
    When 选择客户，点击鼠标右键，选择【删除】按钮删除客户

  Scenario: 列表页右上角删除客户
    Given 销售顾问登录融管系统
    When 创建共享客户2
    Given 销售顾问登录融管系统
    When 查询共享客户2
    When 选择客户，点击列表页右上角的【删除】按钮删除客户