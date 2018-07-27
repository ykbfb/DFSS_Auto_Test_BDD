import sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ArchiveContractPage import ArchiveContractPage
from data.TestData import Data
import time
from behave import *
from hamcrest import assert_that, equal_to

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


@When('以：{archive_type}名义归档{contract_type}合同，进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【归档】按钮')
def step_archiveVIPContract(context,archive_type,contract_type):
    context.archive_type = archive_type
    context.contract_type = contract_type
    global ac
    ac = ArchiveContractPage(context.driver)
    ac.gotoNeedAchiveList(Data.cmp_name)
    if archive_type == '公司' and contract_type == '会员':
        ac.archiveContractForCMP_VIP()  # 会员合同归档
        functions.insert_img(context.driver, "archiveVIPContractForCMP_" + current_time + ".png")
    elif archive_type == '公司' and contract_type == '外包':
        ac.archiveContractForCMP_BPO() #外包合同归档
        functions.insert_img(context.driver, "archiveBPOContractForCMP_" + current_time + ".png")
    elif archive_type == '个人' and contract_type == '会员':
        ac.archiveContractForPerson_VIP()  # 会员合同归档
        functions.insert_img(context.driver, "archiveContractForPerson_" + current_time + ".png")
    elif archive_type == '个人' and contract_type == '外包':
        ac.archiveContractForPerson_BPO() #外包合同归档
        functions.insert_img(context.driver, "archiveContractForPerson_" + current_time + ".png")
    else:
        print('归档类型、合同类型错误， 请确认归档类型为：公司or个人；合同类型为：会员or外包')

    
@Then('合同归档成功')
def step_verifyContractArchiveSucess(context):
    ac.gotoArchivedContractList(Data.cmp_name)
    assert Data.lnk_moblie in ac.verifyContractArchivedSucess()
    functions.insert_img(context.driver,"CheckArchivedContractSucess_"+current_time+".png")
    ac.setWaitTime(2)

@When('进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【打回】按钮')
def step_rejectContract(context):
    ac.gotoNeedAchiveList(Data.cmp_name)
    ac.rejectContract(Data.ctr_reject_memo)
    functions.insert_img(context.driver, current_time + "__rejectContract.png")
    ac.setWaitTime(2)

@Then('合同打回成功')
def step_verifyContractRejectSucess(context):
    ac.gotoOtherTab(Data.cmp_name)
    assert Data.lnk_moblie in ac.verifyContractRejecteddSucess()
    functions.insert_img(context.driver,"CheckRejectedContractSucess_"+current_time+".png")
    ac.setWaitTime(2)

@When('进入【财务】-【合同审批发放】-【未归档】页面选择合同并点击【作废】按钮')
def step_discardContract(context):
    ac = ArchiveContractPage(context.driver)
    ac.gotoNeedAchiveList(Data.cmp_name)
    ac.discarContract(Data.ctr_discar_memo)
    functions.insert_img(context.driver, current_time + "__discarContract.png")
    ac.setWaitTime(2)

@Then('合同作废成功')
def step_verifyContractDiscardSucess(context):
    ac.gotoDiscaredContractList(Data.cmp_name)
    assert Data.lnk_moblie in ac.verifyContractDiscardSucess()



