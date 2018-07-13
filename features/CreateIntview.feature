# Created by Administrator at 2018/7/9

@create_intview
Feature: 创建邀约

  @DC_intview
  Scenario: 创建DC邀约
    Given 登录融管系统
    When 查询客户
      When 输入DC邀约详情
    Then DC邀约创建成功

  @modify_intview
  Scenario: 修改邀约
    Given 登录融管系统
    When 查询客户
      When 修改输入邀约详情
    Then 邀约修改成功

  @create_come_intview
  Scenario: 创建已来访邀约
    Given 登录融管系统
    When 查询客户
    When 输入邀约详情
    Then 邀约创建成功