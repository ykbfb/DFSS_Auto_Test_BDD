#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

#如果定位不到元素，则强制在页面暂停，用time.sleep（）
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


'''
Created on 2017年4月25日

@author: Administrator
'''
class Page(object):
    
    dfss_url = 'http://10.40.3.230:10023/Account/Logon'
    
    def __init__(self,selenium_driver,base_url=dfss_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 10
        self.parent = parent
    
    def _open(self,url):
        url = self.base_url +url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' %url
        
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    #输入框输入东西
    def input_value(self,loc,value):
        self.value = value
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(value)

    #点击元素
    def click_element(self,*loc):
        self.find_element(*loc).click()

    def open(self):
        self._open(self.url)
        
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)
    
    def script(self,src):
        return self.driver.execute_script(src)

    def setWaitTime(self,wait_time): #隐式等待
        self.wait_time = wait_time
        self.driver.implicitly_wait(wait_time)

    def waitElmentUntill(self,wait_time,ele_path): #现实等待：wait_time等待时间， ele_path元素路径
        self.wait_time = wait_time
        self.ele_path = ele_path
        try:
            WebDriverWait(self.driver,wait_time).until(EC.presence_of_element_located(ele_path))
            #WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_element_located(self.find_element(*self.ele_path)))
            '''判断元素是否可见，如果可见就返回这个元素'''
        except TimeoutError as e:
            print("等待超时，元素找不到： " + e)

    def close(self):
        # self.delete_cookies()
        self.KeyboardActions()
        self.driver.quit()

    def delete_cookies(self):
        cookies = self.driver.get_cookies()
        print(f"main: cookies = {cookies}")
        self.driver.delete_all_cookies()

#==================================================================================================================
    #切换页面框架
    def switchFrame(self,frame1,frame2):
        self.frame1 = frame1
        self.frame2 = frame2
        
        try:
            frame = self.driver.find_element_by_xpath(frame1)
            print("get the element success--frame1")
        except NoSuchElementException:
            assert 0, "can't find the Element--xpath"
        self.driver.switch_to.frame(frame)          
        self.driver.implicitly_wait(20)
        self.driver.switch_to.default_content() #返回默认框架
                 
        try:
            frame = self.driver.find_element_by_xpath(frame2)
            print("get the element success--frame2")
        except NoSuchElementException:
            assert 0, "can't find the Element--xpath2"
        self.driver.switch_to.frame(frame)
        print("frame Is switch successfully")

    def switchToOneFrame(self, frame):  # frame参数为指定iframe 的id、name； 如果没有id、name则可以用frame的下标来表示
        self.frame = frame

        try:
            self.driver.switch_to.frame(frame)
            print('switch to one frame by ID...')
        except NoSuchElementException as e:
            print("找不到指定的iframe",e)


    def switchToDefaultContent(self):  # 切换回主文档
        try:
            self.driver.switch_to.default_content()
            print('switch to default frame...')
        except NoSuchElementException as e:
            print('切换iframe到最顶层失败',e)

    def switchToOneFrameByXpath(self, frame):  # frame没有id,name, 根据xpath定位
        self.frame = frame
        try:
            trg_frame = self.driver.find_element_by_xpath(frame)
            self.driver.switch_to.frame(trg_frame)
            print('has switch to the frame by xpath: ', frame)
        except NoSuchElementException as e:
            print('未找到指定的iframe',e)

    def switchToParentFrame(self):  # 回退到上一层frame
        try:
           self.driver.switch_to.parent_frame()
           print('swithch to parent frame success')
        except NoSuchElementException as e:
            print('未找到上层iframe',e)

#=================================================================================================================================
    #窗口最大化
    def maxWindow(self):
        self.driver.maximize_window()

    #用JavaScript实现弹窗最大化
    def maxWindowByJs(self):
        src = 'function openwin_full(url) {var scrWidth=screen.availWidth;' \
              'var scrHeight=screen.availHeight;' \
              ' var self=window.open(url,"PowerBOS","resizable=1");' \
              'self.moveTo(0,0);self.resizeTo(scrWidth,scrHeight);}'
        self.script(src)

    #切换窗口
    def switchWindow(self):
        current_window = self.driver.current_window_handle #获取当前窗口句柄
        all_handles = self.driver.window_handles #获取所有窗口句柄
            
        for handle in all_handles: #切换到新打开的窗口
            if handle != current_window:
                self.driver.switch_to.window(handle)
                print('get current window')

    # 切换窗口
    def switchWindow2(self):
        # all_handles = self.driver.window_handles  # 获取所有窗口句柄
        for handle in self.driver.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
            self.driver.switch_to.window(handle)

    # 返回当前窗口
    def switchToCurrentWindow(self):
        current_window = self.driver.current_window_handle
        try:
            self.driver.switch_to.window(current_window)
            print("Now has switch to current window!")
            print(self.driver.current_window_handle.title())
        except WindowsError as e:
            print('窗口切换失败： ', e)

    # 返回当前窗口的上一个窗口
    def switchToLastWindow(self):
        all_win = self.driver.window_handles  # 返回所有窗口
        try:
            self.driver.switch_to.window(all_win[0])
            print('has return to last window')
        except WindowsError as e:
            print('窗口切换失败： ',e)


    # 返回当前窗口的第二个窗口
    def switchToSecondWindow(self):
        all_win = self.driver.window_handles  # 返回所有窗口
        try:
            self.driver.switch_to.window(all_win[2])
            print('has return to last window')
        except WindowsError as e:
            print('窗口切换失败： ',e)

    # 返回当前窗口的最后一个个窗口
    def switchToLastWindow2(self):
        all_win = self.driver.window_handles  # 返回所有窗口
        try:
            self.driver.switch_to.window(all_win[-1])
            print('has return to last window')
        except WindowsError as e:
            print('窗口切换失败： ',e)


#==========================================================================================================================
    # 将鼠标移动到指定位置
    def moveToX(self, x, y):
        self.x = x
        self.y = y

        ActionChains(self.driver).move_by_offset(x, y).click()
        print("move suceesfully")

    # 这个方法可以将滚动条拖动到需要显示的元素位置
    def scrollToElement(self, getWay, target):  # getWay元素定位的方式； target元素属性名称（id,name,xpath...）
        self.getWay = getWay
        self.target = target

        if getWay == 'id':
            target_element = self.driver.find_element_by_id(target)
            self.driver.execute_script("arguments[0].scrollIntoView();", target_element)  # 拖动到可见的元素去
            print("move to element success: ", target)
        elif getWay == 'name':
            target_element = self.driver.find_element_by_name(target)
            self.driver.execute_script("arguments[0].scrollIntoView();", target_element)  # 拖动到可见的元素去
            print("move to element success: ", target)
        elif getWay == 'xpath':
            target_element = self.driver.find_element_by_xpath(target)
            self.driver.execute_script("arguments[0].scrollIntoView();", target_element)  # 拖动到可见的元素去
            print("move to element success: ", target)
        elif getWay == 'class_name':
            target_element = self.driver.find_element_by_class_name(target)
            self.driver.execute_script("arguments[0].scrollIntoView();", target_element)  # 拖动到可见的元素去
            print("move to element success: ", target)
        elif getWay == 'CSS':
            target_element = self.driver.find_element_by_css_selector(target)
            self.driver.execute_script("arguments[0].scrollIntoView();", target_element)  # 拖动到可见的元素去
            print("move to element success: ", target)
        else:
            print("can't find the element, please select the correct way: id, name, xpath, CSS, class_name")

#=======================================================================================================================================
    #删除浏览器缓存
    def deleteAllCookies(self):
        self.driver.delete_all_cookies()  # 删除所有cookie

    #清除浏览器缓存
    def KeyboardActions(self):
        #清除浏览器缓存 Ctrl + F5
        ActionChains(self.driver).key_down(Keys.CONTROL).key_down(Keys.F5).send_keys(Keys.UP).perform()
# --====================================================================================================================================
# --定位下拉框： get dropdown menu
# --=====================================================================================================================================

    def getDropdownMenu(self, dropMenu_path, drop_elem):  # dropMenu_path 下拉框、 drop_elem 下拉框中的选项
        self.dropMenu_path = dropMenu_path
        self.drop_elem = drop_elem
        self.driver.find_element_by_id(dropMenu_path)
        self.driver.find_element_by_xpath(drop_elem).click()

    # 通过select定位下拉框元素
    def getDropdownMenuByXpath(self, dropMenu_path, value):  # find_type定位元素的方式、dropMenu_path下拉框元素的路径、Value下列选项所在的位置索引
            Select(self.driver.find_element_by_xpath(dropMenu_path)).select_by_index(value)

    def getDropdownMenuById(self, dropMenu_path, value):  # find_type定位元素的方式、dropMenu_path下拉框元素的路径、Value下列选项所在的位置索引
            Select(self.driver.find_element_by_id(dropMenu_path)).select_by_index(value)

#============================================================================================================================================
    #鼠标右键
    def rightClick(self, elm_path):
        self.elm_path = elm_path
        elm = self.driver.find_element_by_xpath(elm_path)
        ActionChains(self.driver).context_click(elm).perform()

    # ----鼠标双击操作-------
    def doubleClick(self, getway, elm_path):
        self.elm_path = elm_path
        elm = self.driver.find_element_by_xpath(elm_path)
        ActionChains(self.driver).double_click(elm).perform()

#============================================================================================================================================
    # --时间选择器定位
    def getDateTimePicker(self, timePicker_id, time_value):  # timePicker_id时间控件的id；  time_value手动输入日期的值
        # 将时间控件字段置为空
        jStr1 = "$('input[id="
        jStr2 = "]').attr('readonly',false)"
        js = jStr1 + timePicker_id + jStr2
        self.driver.execute_script(js)

        # 找到时间控件元素，并手动输入日期
        self.driver.find_element_by_id(timePicker_id).clear()
        self.driver.find_element_by_id(timePicker_id).send_keys(time_value)
        self.driver.implicitly_wait(10)
        print("The date time is: ", self.driver.find_element_by_id(timePicker_id).get_attribute('value'))

    # ============================================================================================================================================
    # --只读输入框文字输入
    def inputForReadonlyEle(self, ele_id, value):  # timePicker_id时间控件的id；  time_value手动输入日期的值
        # 将时间控件字段置为空
        jStr1 = "$('input[id="
        jStr2 = "]').attr('readonly',false)"
        js = jStr1 + ele_id + jStr2
        self.driver.execute_script(js)

        # 找到时间控件元素，并手动输入日期
        self.driver.find_element_by_id(ele_id).clear()
        self.driver.find_element_by_id(ele_id).send_keys(value)
        self.driver.implicitly_wait(10)
        print("The date time is: ", self.driver.find_element_by_id(ele_id).get_attribute('value'))
  #=========================================================================================================================================
    #获取复选框
    def getCheckbox(self, checkbox_path):  # checkbox_path复选框的路径
        self.checkbox_path = checkbox_path

        try:
            checkbox = self.driver.find_element_by_id(checkbox_path)
            if checkbox.is_selected():
                print("The check box  is selected")
                # checkbox.click()
            else:
                print("check box is not selected...now please selected")
                checkbox.click()
                print("The check box is selected now...")
        except Exception as e:
            print("Exception occured", format(e));
        finally:
            # driver.quit()
            print("It's OK")

#==================================================================================================================================================
    #获取单选按钮
    def getRadioButton(self, radio):  # radio 单选按钮元素的名称（元素的id)
        self.radio = radio

        try:
            radiobutton = self.driver.find_element_by_id(radio)
            if radiobutton.is_selected():
                print("The radiobutton is selected")
                radiobutton.click()
            else:
                print("radio is not selected...now please selected")
                radiobutton.click()
                print("the radio button is selected now...")
        except Exception as e:
            print("Exception occured", format(e));
        finally:
            # driver.quit()
            print("It's OK")

# ===========================================================================================
#   文件上传处理
# ===========================================================================================
# input框上传

    def uploadFile(self, getWay, elem, file_path):  # getWay获取元素的方法；elem元素的属性id,xpath...;file_path文件路径
        self.getWay = getWay
        self.elem = elem
        self.file_path = file_path

        if getWay=='id':
            upload = self.driver.find_element_by_id(elem)
            upload.send_keys(file_path)  # 发送文件所在路径
            print(upload.get_attribute('value'))
        elif getWay=='name':
            upload = self.driver.find_element_by_name(elem)
            upload.send_keys(file_path)  # 发送文件所在路径
            print(upload.get_attribute('value'))
        elif getWay=='class_name':
            upload = self.driver.find_element_by_class_name(elem)
            upload.send_keys(file_path)  # 发送文件所在路径
            print(upload.get_attribute('value'))
        elif getWay=='CSS':
            upload = self.driver.find_element_by_css_selector(elem)
            upload.send_keys(file_path)  # 发送文件所在路径
            print(upload.get_attribute('value'))
        elif getWay=='xpath':
            upload = self.driver.find_element_by_xpath(elem)
            upload.send_keys(file_path)  # 发送文件所在路径
            #print(upload.get_attribute('value'))
        else:
            print("can find the element, please use correct way: id,name,class_name,CSS,xpath")

    def uploadFile2(self,elem,file_path):
        self.elem = elem
        self.file_path = file_path
        self.find_element(*self.elem).send_keys(file_path)

    #关闭alert窗口
    def close_alert(self):
        self.driver.switch_to_alert().accept()  # 点击弹出里面的确定按钮
        # alert = self.driver.switch_to_alert()
        # 接收
        # alert.accept()
        # self.driver.execute("acceptAlert")

    #生成随机数
    def getRandomNumber(self,count):
        self.count = count
        num = random.random()

    #判断元素是否存在
    def _isElementExist(self,element):
        flag = True
        try:
            self.find_element(*element)
            return flag
        except:
            flag = False
            return flag




        
        
        
        
        