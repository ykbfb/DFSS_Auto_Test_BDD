# Created by yang kun at 2018/7/9

@modify_lnk
Feature: 我的客户模糊查询及联系人修改

  Scenario: 修改联系人
    Given 销售顾问登录融管系统
    When 查询要修改联系人的客户
      When 输入联系人详情
    Then 联系人修改成功

  Scenario: 客户模糊查询
    Given 销售顾问登录融管系统
    When 模糊查询客户
    Then 客户查询成功