#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import os
import unittest
#======================
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(),"./DFSS_Auto_Test_BDD")))
#======================

#发邮件
def send_email(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject']= Header("融管系统自动化测试报告",'utf-8')
    
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qiye.163.com")
    smtp.login("yangkun@rongzi.com","Dfss!147")
    smtp.sendmail("yangkun@rongzi.com","yangkun@rongzi.com",msg.as_string())
    smtp.quit()
    print("邮件发送成功！")
    
#查找测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    current_path = os.path.dirname(__file__)#加此句代码，是为了在用命令执行项目的时候能正常运行
    filename = current_path + '/report/' +now+'result.thml'  #相对路径
    #filename = 'G:\\DFSS_Auto_Test_BDD\\report\\' +now+'result.thml'#绝对路径
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,
                            title='融管系统自动化测试报告',
                            description='环境：window 7 浏览器： Chrome')
    # runner = HTMLTestRunner()
    discover = unittest.defaultTestLoader.discover(current_path + '/test_case/testcases',pattern = '*_testcase.py')
    #discover = unittest.defaultTestLoader.discover('G:\\DFSS_Auto_Test_BDD\\test_case\\testcases',pattern = '*_testcase.py')
    #================================================================================================================
    #定时跑case
    # k = 1
    # while k < 2:
    #     timing = time.strftime('%H:%M', time.localtime(time.time()))
    #     if timing == '10:35':  # 17_35指17:35,这个可以根据需要设定时间
    #         print('start to run scripts')
    #         runner.run(discover)  # 运行所有的case
    #         print('Finish runing scripts')
    #         break
    #     else:
    #         time.sleep(3)
    #         print(timing)
    #==================================================================================================================
    runner.run(discover)
    fp.close()
    file_path = new_report('./report/')
    send_email(file_path)

# input(">>Press any key to exit...")
    
    
    
    
    
    
    
    