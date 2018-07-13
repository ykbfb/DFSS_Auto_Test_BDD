# Created by kun yang at 2018/7/5
#Feature: 测试登录融管系统
#  Scenario Outline: 验证登录成功
#    Given 打开登录页面: http://10.40.3.230:10023/Account/Logon
#    When 输入用户名:<username>，输入密码:<password>，输入城市:<city> 登录系统
#    Then 登录成功:<result>
#      #And 关闭浏览器
#
#  Examples: 用户表及验证结果
#    |username|password|city|result|
#    |qiushun |123456   |suzhou   |Hello,邱顺 [AA1128]|
#    |yanfang |123456   |suzhou   |Hello,颜芳 [AA5771]|
#    |liuchao |123456   |suzhou   |Hello,刘超 [AA1611]|

@user_login
Feature: 测试登录融管系统

  Scenario: 验证登录成功
    Given 打开登录页面: http://10.40.3.230:10023/Account/Logon
    When 输入用户信息
    Then 登录成功
#      And 关闭浏览器



