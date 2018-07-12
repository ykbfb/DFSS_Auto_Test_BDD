import csv, xlrd,xlwt

class TestData:
    with open('F:\DFSS_New_Auto_Test\data\TestData.csv','r') as testdata: #用with，文件不用时会自动关闭
        data = csv.reader(testdata)
        for aa in data:
            print(aa)


    f = open('F:\DFSS_New_Auto_Test\data\TestData.csv','r')  #此方法，文件不用时不会自动关闭
    data2 = csv.reader(f)
    for bb in data2:
        print(bb)
    f.close()



    with open("F:\DFSS_New_Auto_Test\data\TestData.csv", "r") as f:
        reader = csv.DictReader(f)
        username = [row['用户名'] for row in reader]
        password = [row['密码'] for row in reader]
        city = [row['城市'] for row in reader]