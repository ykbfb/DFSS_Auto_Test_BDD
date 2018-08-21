# env config
from past.builtins import execfile
import os

#指定测试环境
ENV = 'test'
#===========================================================================================================================================
#融管系统测试环境地质
DFSS_WEB_TEST_BASE_URL = 'http://10.40.3.230:10023/Account/Logon'

#===========================================================================================================================================
#等待时间
WAIT_TIME = 20
#===========================================================================================================================================
#浏览器driver配置
Chrome_driver_path = r'D:\Users\Administrator.SKYUSER-Q\AppData\Local\Google\Chrome\Application\chromedriver.exe'
IE_driver_path = ''
Firefox_driver_path = ''
#===========================================================================================================================================
#数据库配置
DB_HOST = '10.40.3.230'
DB_PORT = ''
DB_USER = 'Info'
DB_PASSWORD = 'dfss@qqq.111'
DB_NAME = 'DFSS_SUZHOU'
#===========================================================================================================================================
#测试文件存放地址：
cur_path = os.getcwd() #当前脚本文件的路径（即settings文件的路径）
father_path=os.path.abspath(os.path.dirname(cur_path)+os.path.sep+".") #当前文件的父级路径
#father_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
grader_father=os.path.abspath(os.path.dirname(cur_path)+os.path.sep+"..") #当前文件的前两级目录

Contract_file = father_path+ r"\TestDataFiles\upload_files\girl.jpg"
Other_file = father_path + r"\TestDataFiles\upload_files\图图.jpg"

#======================================================================================================================================
# local debugging config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT_DIRECTORY = os.path.join(BASE_DIR, 'logs')

SETTING_LOCAL_DIR = os.path.join(BASE_DIR, "settings_local.py")
if os.path.exists(SETTING_LOCAL_DIR):
    execfile(SETTING_LOCAL_DIR)