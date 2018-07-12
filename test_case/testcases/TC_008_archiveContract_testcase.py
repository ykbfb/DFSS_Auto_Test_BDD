# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: Administrator
'''
import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ArchiveContractPage import ArchiveContractPage
from data.TestData import Data
import time


class ArchiveContractTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统-管理端
    def user_login_verify(self, username=Data.finance_name, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)


    # 合同归档--以公司名义签订
    def test_1_archiveContractForCMP(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.archiveContractForCMP_VIP() #会员合同归档
        #arc_contract.archiveContractForCMP_BPO() #外包合同归档
        functions.insert_img(self.driver, current_time + "__archiveContractForCMP.png")

        #校验合同是否归档成功
        arc_contract.gotoArchivedContractList(Data.cmp_name)
        self.assertIn(Data.lnk_moblie,arc_contract.verifyContractArchivedSucess())
        functions.insert_img(self.driver, current_time + "__CheckArchivedContractSucessForCMP.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()

    # 合同归档--以个人名义签订
    def aa_test_2_archiveContractForPerson(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.archiveContractForPerson_VIP() #会员合同归档
        #arc_contract.archiveContractForPerson_BPO() #外包合同归档
        functions.insert_img(self.driver, current_time + "__archiveContractForPerson.png")

        #校验合同是否归档成功
        arc_contract.gotoArchivedContractList(Data.cmp_name)
        self.assertIn(Data.lnk_moblie,arc_contract.verifyContractArchivedSucess())
        functions.insert_img(self.driver, current_time + "__CheckArchivedContractSucessForPerson.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()

    #合同打回
    def aa_test_3_rejectContract(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.rejectContract(Data.ctr_reject_memo)
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__rejectContract.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()
    #合同作废
    def AA_test_4_discarContract(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.discarContract(Data.ctr_discar_memo)
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__discarContract.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()

if __name__ == '__main__':
    unittest.main()


