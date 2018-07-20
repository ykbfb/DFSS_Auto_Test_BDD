# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

# --==================================================================
# By 函数的属性：
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
#---------------------------------------------------------------------
#定位动态id、name元素
# driver.find_element_by_xpath("//iframe[contains(@id, 'layui-layer-iframe')]")
# driver.find_element_by_xpath("//div[starts-with(@id, 'btn-attention')]")
# driver.find_element_by_xpath("//div[ends-with(@id, 'btn-attention')]")
# --==================================================================

from selenium.webdriver.common.by import By
from .base import Page
import time

class SalesResultApprovalPage(Page):
    # 销售喜报审批--分公司财务
    finance_menu_loc = (By.XPATH, '//*[@id="wnav"]/div[2]/div[1]/div[1]')  # 财务
    fin_salresult_menu_loc = (By.XPATH, '//*[@id="wnav"]/div[2]/div[2]/ul/li[2]/div/a/span[2]')  # 销售喜报审批
    fin_sales_resultlistframe_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    fin_clt_name_loc = (By.ID, 'querycode')  # 客户名称
    fin_search_btn_loc = (By.ID, 'Button4')  # 查询

    fin_order_result_loc = (By.XPATH, '//*[@id="htmlcontent"]/table/tbody/tr[2]/td[1]/input[1]')  # 查看
    fin_order_detal_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    fin_apprv_memo_loc = (By.ID, 'fadnoti')  # 审批意见
    fin_move_apprv_memo_loc = 'fadnoti'
    fin_apprv_pass_loc = (By.ID, 'compairendaction')  # 通过


    def approveSalesResult_Finance(self, value):
        self.value = value
        self.click_element(*self.finance_menu_loc)
        self.click_element(*self.fin_salresult_menu_loc)
        self.setWaitTime(10)
        self.switchToOneFrameByXpath(self.fin_sales_resultlistframe_loc)
        self.input_value(self.fin_clt_name_loc, value)
        self.click_element(*self.fin_search_btn_loc)

        time.sleep(1)
        self.click_element(*self.fin_order_result_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.fin_order_detal_frame_loc)
        self.scrollToElement('id', self.fin_move_apprv_memo_loc)
        self.input_value(self.fin_apprv_memo_loc, '自动化测试：销售喜报审批--分公司财务')
        self.click_element(*self.fin_apprv_pass_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(1)
        self.close_alert()

    # 销售喜报审批-数据专员
    dt_salesresult_menu_loc = (By.XPATH, '//*[@id="wnav"]/div[1]/div[2]/ul/li[8]/div/a/span[2]')  # 销售业绩审批
    dt_sales_resultlistframe_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    dt_sal_city_loc = 'citys_c'  # 城市
    dt_clt_name_loc = (By.ID, 'querycode')  # 客户名称
    dt_search_loc = (By.ID, 'Button4')  # 查询

    dt_order_detail_loc = (By.XPATH, '//*[@id="htmlcontent"]/table/tbody/tr[2]/td[2]/input[1]')  # 查看
    dt_order_detal_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_apprv_memo_loc = (By.ID, 'fadnoti')  # 审批意见
    dt_move_apprv_memo_loc = 'fadnoti'
    dt_apprv_pass_loc = (By.ID, 'Button1')  # 通过

    dt_sales_resultdetail_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_save_close_loc = (By.ID, 'btnSaveClose')  # 保存关闭并发送
    dt_move_save_close_loc = 'btnSaveClose'

    dt_confirm_loc = (By.CLASS_NAME, 'layui-layer-btn0')  # 确定

    dt_message_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    dt_msg_send_loc = (By.XPATH, '//*[@id="main"]/div[1]/table/tbody/tr[4]/td[2]/input[1]')  # 发送
    dt_send_success_loc = (By.CLASS_NAME, 'layui-layer-btn0')  # 发送成功

    def approveSalesResult_DataManager(self, value):
        self.value = value
        self.click_element(*self.dt_salesresult_menu_loc)
        self.setWaitTime(20)
        self.switchToOneFrameByXpath(self.dt_sales_resultlistframe_loc)
        self.getDropdownMenuById(self.dt_sal_city_loc, 0)
        self.input_value(self.dt_clt_name_loc, value)
        self.click_element(*self.dt_search_loc)

        time.sleep(1)
        self.click_element(*self.dt_order_detail_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_order_detal_frame_loc)
        self.scrollToElement('id', self.dt_move_apprv_memo_loc)
        self.input_value(self.dt_apprv_memo_loc, '自动化测试：销售喜报审批--数据部')
        self.click_element(*self.dt_apprv_pass_loc)
        time.sleep(1)
        self.close_alert()
        time.sleep(3)

        # 喜报详情页
        self.switchToParentFrame()
        self.switchWindow()
        time.sleep(2)
        self.switchToOneFrameByXpath(self.dt_sales_resultdetail_frame_loc)
        self.scrollToElement('id', self.dt_move_save_close_loc)
        self.click_element(*self.dt_save_close_loc)
        time.sleep(1)

        # 确认窗口
        self.switchWindow()
        self.click_element(*self.dt_confirm_loc)
        time.sleep(1)

        # QQ广播页面
        self.switchToDefaultContent()
        self.switchToOneFrameByXpath(self.dt_sales_resultlistframe_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.dt_message_frame_loc)
        time.sleep(1)
        self.click_element(*self.dt_msg_send_loc)
        time.sleep(1)

        # 发送成功确认
        self.switchWindow()
        self.click_element(*self.dt_send_success_loc)












