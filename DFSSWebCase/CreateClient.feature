# Created by kun yang at 2018/7/6

@createNewClient
Feature: 创建客户

  Scenario: 已存在客户不能创建
    Given 登录融管系统
    When 输入手机号
    Then 校验客户已经存在

  Scenario: 不存在客户能创建成功
    Given 登录融管系统
    When 输入手机号
    Then 校验客户不存在
    When 输入客户详情
    Then 客户创建成功