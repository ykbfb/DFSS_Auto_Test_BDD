# Created by kun yang at 2018/7/13
@cus_call
Feature: 拨打电话

  @double_call
  Scenario:列表页双击拨打电话
    Given 销售顾问登录融管系统
    When 查询客户
    When 进入【我的客户】列表页，选择客户双击，并在呼叫详情页输入呼叫详情，点击【保存】

  @rightclick_call
  Scenario:列表页右键拨打电话
    Given 销售顾问登录融管系统
    When 查询客户
    When 进入【我的客户】列表页，选择客户鼠标右键，点击【呼叫】按钮，并在呼叫详情页输入呼叫详情，点击【保存】

  @list_call
  Scenario:列表页直接拨打电话
    Given 销售顾问登录融管系统
    When 查询客户
    When 进入【我的客户】列表页，选择客户点击【呼叫】按钮，并在呼叫详情页输入呼叫详情，点击【保存】

  Scenario:列表页批量拨打电话
    Given 销售顾问登录融管系统
    When 查询客户
    When 进入【我的客户】列表页，选择客户点击【批量呼叫】按钮，并在呼叫详情页输入呼叫详情，点击【保存】

