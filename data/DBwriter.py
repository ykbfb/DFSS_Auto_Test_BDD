

import pymssql

conn = pymssql.connect(host='10.40.3.230',
                       user='Info',
                       password='dfss@qqq.111',
                       database='DFSS_SUZHOU',
                       charset='utf8')

# 查看连接是否成功
cursor = conn.cursor()
sql = 'SELECT top 1 * FROM dbo.HRS_EMP_BASE'
cursor.execute(sql)
# 用一个rs变量获取数据
rs = cursor.fetchall()

print(rs)
