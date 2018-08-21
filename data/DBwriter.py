import pymssql
from test_case.models import settings
'''从文件中读取sql语句并执行'''

def executeSQLFromFile(filename):
    conn = pymssql.connect(host=settings.DB_HOST,
                           user=settings.DB_USER,
                           password=settings.DB_PASSWORD,
                           database=settings.DB_NAME,
                           charset='utf8')

    cursor = conn.cursor()
    with open(filename, 'r') as f:
        sqlFile = f.read()
        sqls = sqlFile.split('GO')

    for sql in sqls:
        try:
            cursor.execute(sql)
            print(sql)
        except Exception as e:
            print("SQL执行出错"+ str(e))
    conn.commit()
    print('测试数据初始化完成...')

    # rs = cursor.fetchall()     #获取游标查询的结果
executeSQLFromFile("../test_case/TestDataFiles/自动化测试数据初始化脚本.sql")
