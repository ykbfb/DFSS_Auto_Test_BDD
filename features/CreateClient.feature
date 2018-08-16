# Created by kun yang at 2018/7/6

@createNewClient
Feature: 创建客户

  @exist
  Scenario: 已存在客户不能创建
    Given 销售顾问登录融管系统
    When 输入已存在的手机号
    Then 校验客户已经存在

  @not_exist
  Scenario Outline: 不存在客户能创建成功
    Given 销售顾问登录融管系统
    When 输入系统中不存在的手机号:<lnk_mobile>
    Then 校验客户不存在
    When 输入客户详情
    Then 客户创建成功:<lnk_mobile>

  Examples: 客户号码
    |lnk_mobile|
    |18325556360|
    |18325556361|
    |18325556362|
