# Created by kun yang at 2018/7/18
@share_client
Feature: 共享客户

  @right_share
  Scenario: 列表页右键共享
    Given 销售顾问登录融管系统
    When 创建共享客户1
    Given 销售顾问登录融管系统
    When 查询共享客户1
    When 打开【客户管理】→【我的客户】，在客户列表页选择客户，单击鼠标【右键】，点击【共享】按钮，填写“共享原因”，将客户释放到公海

  @list_share
  Scenario: 列表页共享
    Given 销售顾问登录融管系统
    When 创建共享客户2
    Given 销售顾问登录融管系统
    When 查询共享客户2
    When 打开【客户管理】→【我的客户】，在客户列表页选择客户，点击列表右上角【共享】按钮，填写“共享原因”，将客户释放到公海

   @call_share
   Scenario: 呼叫页面共享
    Given 销售顾问登录融管系统
    When 创建共享客户3
    Given 销售顾问登录融管系统
    When 查询共享客户3
    When 打开【客户管理】→【我的客户】，在客户列表页选择客户，单击【呼叫】按钮，填写回访信息，点击【共享】填写“共享原因”，将客户释放到公海