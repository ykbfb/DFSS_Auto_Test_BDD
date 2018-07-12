# Created by kun fyang at 2018/7/9

@approve_intview
Feature: 邀约审批

  Scenario: 邀约审批
    Given 销售经理登录融管系统
    When 审批邀约
    Then 邀约审批成功

