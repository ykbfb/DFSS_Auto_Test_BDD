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
            username = user[0][1]
            password = user[0][2]
            city = user[0][3]
            return username,password,city
        except:
            print('输入的角色错误')

#===================================================================================================================================================
# 初始化客户信息
#===================================================================================================================================================
    def getClient(self,clt_isexist):
        self.clt_isexist = clt_isexist
        try:
            client = get_excel_specfied_row("BaseData.xls", "clientInfo",clt_isexist)
            lnk_mobile = client[0][1]
            lnk_name = client[0][4]
            cmp_name = client[0][5]
            ContractCode = client[0][6]
            return lnk_mobile,lnk_name,cmp_name,ContractCode
        except:
            print('输入错误，请确认输入内容为：老客户 or 新客户')


#=================================================================================================================================================
# 初始化测试结果
#=================================================================================================================================================
    def getExpectedResult(self,scenario):
        self.scenario = scenario
        try:
            result = get_excel_specfied_row("BaseData.xls","expectResult",scenario)
            expected = result[0][1]
            return expected
        except:
            print('输入的测试场景不存在')



if __name__ == '__main__':
    u = Data()
    u1 = u.getExpectedResult('客户已存在')
    print(u1)
    # print(Data.sales_manager)

