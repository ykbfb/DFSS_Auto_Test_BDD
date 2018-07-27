# !/usr/bin/python3

import os
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from test_case.models import getDir
import xlrd
import xlwt

'''excel读写'''
proDir = getDir.proDir

class PyExcel:
    """Use the given excel_name and sheet_name, sheet_value, write excel and read excel.
        1. write_excel
        2. read_excel
    """
    TestFile = os.path.join(proDir, "TestDataFiles")
    suffix = ".xls"

    def __init__(self, excel_name, sheet_name=None, sheet_value=None):
        """
        initialization parameter
        :param excel_name: The file suffix must be "xls"
        :param sheet_name: set the workbook's sheetName
        :param sheet_value: The type of object must be "list" or "tuple"
        """
        self.excel_name = excel_name
        self.sheet_name = sheet_name
        self.sheet_value = sheet_value

        if not str(self.excel_name).endswith(self.suffix):
            raise Exception('%s suffix is not "%s"' %
                            (self.excel_name, self.suffix))
        self.EXCEL_PATH = os.path.join(self.TestFile, self.excel_name)

        if self.sheet_value is not None:
            try:
                if isinstance(self.sheet_value, list) or isinstance(self.sheet_value, tuple):
                    for i in range(len(self.sheet_value)):
                        assert isinstance(self.sheet_value[i], list)
            except TypeError as e:
                print(e)

    def write_excel(self):
        if self.sheet_name is not None:
            wb = xlwt.Workbook()
            sheet = wb.add_sheet(self.sheet_name)

            for i in range(len(self.sheet_value)):
                for j in range(len(self.sheet_value[i])):
                    sheet.write(i, j, self.sheet_value[i][j])

            wb.save(self.EXCEL_PATH)
            print("write date success!")
        else:
            return False

    def read_excel(self):
        workbook = xlrd.open_workbook(self.EXCEL_PATH)
        if self.sheet_name:
            work_sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            work_sheet = workbook.sheet_by_index(0)

        for i in range(work_sheet.nrows):
            for j in range(work_sheet.ncols):
                print(work_sheet.cell_value(i, j), "\t", end="")
            print()


def get_excel_value(excel_name, sheet_name):
    """
    根据excel名，sheet名获取整个sheet中的数据
    get excel value by given excel_name and sheet_name
    :param excel_name:
    :param sheet_name:
    :return: cls
    """
    cls = []
    excel_path = os.path.join(proDir, "TestDataFiles", excel_name)
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows

    # for i in range(nrows):
    #     if sheet.row_values(i)[0] != "case_name":
    #         cls.append(sheet.row_values(i))
    # return cls

    for i in range(1,nrows):
        cls.append(sheet.row_values(i))
    return cls


def get_excel_specfied_row(excel_name, sheet_name,key_value):
    '''获取excel中指定行的数据
    excel_name 文件名称， sheet_name 工作表名， key_value 工作表中指定行第一列的数据

    '''
    line=[]
    excel_path = os.path.join(proDir, "TestDataFiles", excel_name)
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)
    nrows = sheet.nrows

    for i in range(nrows):
        if sheet.row_values(i)[0] == key_value:
            line.append(sheet.row_values(i))
    return line

def get_excel_specfied_col(excel_name, sheet_name,col_num):
    '''获取excel中指定列的数据
    excel_name 文件名称， sheet_name 工作表名， col_num 工作表中指定第几列

    '''
    col=[]
    excel_path = os.path.join(proDir, "TestDataFiles", excel_name)
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name(sheet_name)

    col.append(sheet.col_values(col_num))
    return col


if __name__ == "__main__":
    value = (
        ["case_name", "username", "password","city", "excepted"],
        ["用户名错误，密码和城市正确", "hello", "123456","suzhou", "您的登录信息有误，请检查用户名和相关城市！"],
        ["用户名正确，密码错误，城市正确", "qiushun", "abc123","suzhou", "提供的用户名或密码不正确。"],
        ["用户名和密码正确，城市错误", "qiushun", "123456","shanghai", "您的登录信息有误，请检查用户名和相关城市！"],
        ["用户名，密码，城市都正确","qiushun","123456","suzhou","Hello,邱顺 [AA1128]"]
    )
    excel = PyExcel(excel_name="loginCase.xls", sheet_name="login_test", sheet_value=value)
    excel.write_excel()
    excel.read_excel()