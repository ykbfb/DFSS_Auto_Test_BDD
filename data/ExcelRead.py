# _*_ coding:utf-8 _*_

__author__ = '苦叶子'

import xlrd

if __name__ == '__main__':

    # # excel文件全路径
    # xlPath = "F:\DFSS_New_Auto_Test\data\TestData.xlsx"
    #
    # # 用于读取excel
    # xlBook = xlrd.open_workbook(xlPath)
    #
    # # 获取excel工作簿数
    # count = len(xlBook.sheets())
    # print(u"工作簿数为:  ", count)
    #
    # # 获取 表 数据的行列数
    # table = xlBook.sheets()[0]
    # nrows = table.nrows
    # ncols = table.ncols
    # print(u"表数据行列为(%d, %d)" % (nrows, ncols))
    #
    # # 循环读取数据
    # for i in range(1, nrows):
    #     rowValues = table.row_values(i)  # 按行读取数据
    #     print(rowValues)
    #
    #     # # 输出读取的数据:
    #     for data in rowValues:
    #          print(data)
    #     print("")

    #==============================================================================
    def open_excel(file='F:\DFSS_New_Auto_Test\data\TestData.xlsx'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            print(str(e))
        # 根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引

    def excel_table_byindex(file='F:\DFSS_New_Auto_Test\data\TestData.xlsx', colnameindex=0, by_index=0):
        data = open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows  # 行数
        colnames = table.row_values(colnameindex)  # 某一行数据
        list1 = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                    list1.append(app)
        return list1
        print(list1)

excel_table_byindex('F:\DFSS_New_Auto_Test\data\TestData.xlsx', 0, 0)



