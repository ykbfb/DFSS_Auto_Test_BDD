#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8


'''
Created on 2017-4-25

@author: Administrator
'''

from selenium import webdriver
import os
import time



#在指定目录下创建文件夹
def createDir(path): 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\") 
    # 判断路径是否存在: 存在 则返回   True；不存在   返回 False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')

 
#--===================================================================
def insert_img(driver,file_name):
#--========================================================
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)
#--========================================================   
#     base_path = "F:\\Testlog-" + time.strftime('%Y%m%d',time.localtime(time.time())) +"\\"
#     #创建文件夹
#     folder_path = createDir(base_path) 
#     file_path = base_path + file_name
#     #保存文件截图
#     driver.get_screenshot_as_file(file_path)
#--=========================================================

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
#     insert_img(driver,'-baidu.jpg')
    insert_img(driver,str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+'-baidu.jpg')
    print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    driver.quit()
    
    
    