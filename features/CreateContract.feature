# Created by kun yang at 2018/7/9

@create_contract
Feature: 创建合同
  # Enter feature description here

  @create_vip_contract
  Scenario: 创建会员合同
    Given 销售顾问登录融管系统
    When 查询客户
      When 进入【合同管理】页签点击【创建合同】按钮，选择【债权会员合同】并输入会员合同信息详情
    Then 会员合同创建成功

  @create_bpo_contract
  Scenario: 创建外包合同
    Given 销售顾问登录融管系统
    When 查询客户
      When 进入【合同管理】页签点击【创建合同】按钮，选择【债权外包合同】并输入外包合同信息详情
    Then 外包合同创建成功

  @bpo_transto_vip
  Scenario: 外包转会员
    Given 销售顾问登录融管系统
    When 查询客户
      When 进入【合同管理】页签点击【转会员】按钮，选择【债权会员合同】并输入会员合同信息详情
    Then 外包转会员合同创建成功