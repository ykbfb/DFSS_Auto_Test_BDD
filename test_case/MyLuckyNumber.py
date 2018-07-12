import random
import io
import time
import os

#================================================================
#  双色球
#================================================================
def getRedBlueBall():
    r_num = []
    b_num = []

    for i in range(0,6):
        '''随机获取6个红球'''
        num = random.randint(1,33)
        r_num.append(num)

        if num in r_num:
            r_num.append(num)
            r_num.pop()
        else:
            r_num.append(num)


    for j in range(0,1):
        '''随机获取1个蓝球'''
        num = random.randint(1,16)
        b_num.append(num)

        if num in b_num:
            b_num.append(num)
            b_num.pop()
        else:
            r_num.append(num)

    with open("f:\LuckyNumber.txt", "a") as f:   #读写模式为"a"，则表示在文件的末尾追加后续的写入内容，不会覆盖前面的内容
        f.write(str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+" 双色球中奖号码是： "+str(r_num)+"-"+str(b_num)+"\n")

    f = open("f:\LuckyNumber.txt", "r")
    a = f.readlines()[-1] #读取文件中的最后一行数据
    print(a)
    f.close()

#======================================================================================
#  超级大乐透
#======================================================================================
def getSuperLotto():
    r_num = []
    b_num = []

    for i in range(0,5):
        '''随机获取5个红球'''
        num = random.randint(1,35)
        r_num.append(num)

        if num in r_num:
            r_num.append(num)
            r_num.pop()
        else:
            r_num.append(num)


    for j in range(0,2):
        '''随机获取2个蓝球'''
        num = random.randint(1,12)
        b_num.append(num)

        if num in b_num:
            b_num.append(num)
            b_num.pop()
        else:
            r_num.append(num)

    with open("f:\LuckyNumber.txt", "a") as f:   #读写模式为"a"，则表示在文件的末尾追加后续的写入内容，不会覆盖前面的内容
        f.write(str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+" 超级大乐透中奖号码是： "+str(r_num)+"-"+str(b_num)+"\n")

    f = open("f:\LuckyNumber.txt", "r")
    a = f.readlines()[-1]
    print(a)
    f.close()

#=======================================================================
# 根据当前日期决定投注双色球、超级大乐透
#=======================================================================
def getLuckyNumber():
    currtime = time.localtime()
    curr_week_day =int(time.strftime('%w',currtime)) #获取当前日期为星期几

    if (curr_week_day != 6) and (curr_week_day % 2) == 0:
        getRedBlueBall()

    elif curr_week_day == 7:
        getRedBlueBall()

    elif (curr_week_day != 7) and (curr_week_day % 2) != 0:
        getSuperLotto()

    else:
        print("今天请注意休息，改日再战！")

if __name__ == '__main__':
    getLuckyNumber()
