# Created by kun yang at 2018/7/11

@apprv_channelresult
Feature: 融资喜报审批

  @sdir_appv_channelresult
  Scenario: 融服总监审批融资喜报
    Given 融服总监登录融管
    When 打开【融资管理】→【融资喜报审批】→【待审批】页签选择相应的喜报并点击【订单详情】、点击【通过】按钮进行喜报审批

  @fin_appv_channelresult
  Scenario: 分公司财务审批融资喜报
    Given 分公司财务登录融管系统
    When 打开【财务】→【融资喜报审批】→【待审批】页签选择相应的喜报并点击【订单详情】、点击【通过】按钮进行喜报审批
    
  @data_appv_channelresult
  Scenario: 数据部审批融资喜报
    Given 数据专员登录融管
    When 打开【资源管理】→【融资业绩审批】→【待审批】页签选择相应的喜报并点击【订单详情】、点击【通过】按钮进行喜报审批







