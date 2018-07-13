# Created by kun yang at 2018/7/10

@archive_contract
Feature: 合同归档测试

  @arc_vip_contract_cmp
  Scenario: 以公司名义归档会员合同
    Given 分公司财务登录融管系统
    When 以：公司名义归档会员合同，进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【归档】按钮
    Then 合同归档成功
  @arc_bpo_contract_cmp
  Scenario: 以个人名义归档外包合同
    Given 分公司财务登录融管系统
    When 以：公司名义归档外包合同，进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【归档】按钮
    Then 合同归档成功

  @arc_vip_contract_person
  Scenario: 以个人名义归档会员合同
    Given 分公司财务登录融管系统
    When 以：个人名义归档会员合同，进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【归档】按钮
    Then 合同归档成功

  @arc_bpo_contract_person
  Scenario: 以个人名义归档外包合同
    Given 分公司财务登录融管系统
    When 以：个人名义归档外包合同，进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【归档】按钮
    Then 合同归档成功

  @reject_contract
  Scenario: 合同打回
    Given 分公司财务登录融管系统
    When 进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【打回】按钮
    Then 合同打回成功

  @discard_contract
  Scenario: 合同作废
    Given 分公司财务登录融管系统
    When 进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【作废】按钮
    Then 合同打回成功