# Created by Administrator at 2018/7/10

@salesOrder_oprate
Feature: 销售订单操作

  @accept_salesOrder
  Scenario: 销售订单接单
    Given 销售经理登录融管系统
    When 打开【销售管理】→【销售订单处理操作】→【待接单】点击【接单】按钮进行接单
    Then 销售订单接单成功

  @asign_salesOrder
  Scenario: 销售订单派单
    Given 销售经理登录融管系统
    When 打开【销售管理】→【销售订单处理操作】→【待派单】点击【派单】按钮并选择相应的产品线进行派单
    Then 销售订单派单成功