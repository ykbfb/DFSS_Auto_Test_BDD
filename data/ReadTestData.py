import sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import getDir
from test_case.models.common import get_excel_specfied_row,get_excel_specfied_col,get_excel_value
import time

proDir = getDir.proDir
current_time = time.strftime('%Y%m%d%S', time.localtime(time.time()))

class Data:
    '''初始化测试数据'''
#==================================================================================================================================================
# 初始化用户登录信息
#==================================================================================================================================================
    def getUser(self,role):
        self.role = role
        try:
            user = get_excel_specfied_row("BaseData.xls", "userInfo",role)
            u = {
            'username': user[0][1],
            'password': user[0][2],
            'city' : user[0][3]}
            return u
        except:
            print('输入的角色错误')

#===================================================================================================================================================
# 初始化客户信息
#===================================================================================================================================================
    def getClient(self, clt_isexist):
        self.clt_isexist = clt_isexist
        try:
            client = get_excel_specfied_row("BaseData.xls", "clientInfo",clt_isexist)
            a = {
            'lnk_mobile' : client[0][1],
            'lnk_name' : client[0][4],
            'cmp_name' : client[0][5],
            'ContractCode' : client[0][6]}
            return a

        except:
            print('输入错误，请确认输入内容为：老客户 or 新客户')

# ===================================================================================================================================================
# 初始化case的客户信息： 针对每个case 都单独设立一个客户，保证每个客户的独立性
# ===================================================================================================================================================
    def getCaseInitClient(self, key):
        self.key = key
        try:
            client = get_excel_specfied_row("BaseData.xls", "initData",key)
            a = {
            'lnk_mobile' : client[0][1],
            'lnk_name' : client[0][2],
            'cmp_name' : client[0][3]}
            return a
        except:
            print('输入错误，请确认输入内容在文件BaseData->initData->Key列中')

#=================================================================================================================================================
# 读取测试结果
#=================================================================================================================================================
    def getExpectedResult(self,scenario):
        self.scenario = scenario
        try:
            result = get_excel_specfied_row("BaseData.xls","expectResult",scenario)
            expected = result[0][1]
            return expected
        except:
            print('输入的测试场景不存在')
#===============================================================================================================================
#创建子订单的产品
#===============================================================================================================================
    #意向单
    org_name = '浦发银行' #机构
    prd_name = '线上万用金' #产品名称
    credit_manager = '令磊'  #信贷经理

if __name__ == '__main__':
    u = Data()
    u1 = u.getCaseInitClient('修改联系人')
    print(u1['lnk_mobile'])
    print(u1['lnk_name'])
    print(u1['cmp_name'])
    # print(Data.sales_manager)

