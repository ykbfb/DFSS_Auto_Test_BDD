# Created by kun yang at 2018/7/24
Feature: 意向金转业绩

  Scenario: 创建意向金转业绩
    Given 销售顾问登录融管系统
    When 查询客户
    When 打开【我的客户】，列表中选择客户，在【合同管理】中点击【转业绩】按钮，并填写转业绩详情,提交

  Scenario: 经理审批意向金转业绩
    Given 销售经理登录融管系统
    When 打开【综合管理】→【意向金转业绩审批】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮

  Scenario: 销售总监审批意向金转业绩
    Given 销售总监登录融管系统
    When 打开【销售管理】→【意向金转业绩审批-总监】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮

  Scenario: 分公司总经理意向金转业绩
    Given 分公司总经理登录融管
    When 打开【销售管理】→【意向金转业绩审批-分总】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮

  Scenario: 数据部审批意向金转业绩
    Given 销售顾问登录融管系统
    When 打开【资源管理】→【意向金转业绩审批】，选择指定的意向金转业绩申请，点击【审批】按钮，填写审批意见，点击【通过】按钮，喜报详情页面点击【保存关闭并发送】按钮