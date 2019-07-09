#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:李涛
#CreatDate:
#Version: 
#====#====#====#====
import time, os, random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard



from selenium import webdriver

class PersonalManagement():
    def __init__(self):
        firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver_path = r"F:\driver\geckodriver.exe"
        self.driver = webdriver.Firefox(firefox_binary=firefox_path, executable_path=driver_path)
        self.driver.get("http://192.168.1.130:8080/WoniuBoss2.5/")
        self.keyboard = PyKeyboard()

        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10)  # 页面加载的超时时间
        self.driver.set_script_timeout(10)  # 执行JavaScript脚本的超时时间
        self.driver.implicitly_wait(10)

    def login(self):
        driver = self.driver
        driver.get("http://192.168.1.130:8080/WoniuBoss2.5/")
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("WNCD000")
        driver.find_element_by_name("userPass").click()
        driver.find_element_by_name("userPass").clear()
        driver.find_element_by_name("userPass").send_keys("woniu123")
        driver.find_element_by_name("checkcode").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/button").click()
        time.sleep(3)

#点击人事管理进入员工管理模块，选择区域：成都 部门：就业部 点击查询按钮
    def staff_management(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'人事管理')]").click()
        # 随机选择区域
        self.driver.find_element_by_id("regionSel").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择部门
        self.driver.find_element_by_name("department_id").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择状态
        self.driver.find_element_by_name("emp.last_status").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #点击查询按钮
        self.driver.find_element_by_xpath("//div[@id='content']/div[2]/div[2]/button").click()

        # 新增员工
    def  new_staff(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'人事管理')]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='所属区域'])[1]/preceding::button[1]").click()
        #输入一个随机部门
        self.driver.find_element_by_name("emp.region_id").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #输入一个随机区域
        self.driver.find_element_by_name("emp.department_id").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #输入姓名
        self.driver.find_element_by_name("emp.employee_name").send_keys('王五')
        #输入工号
        self.driver.find_element_by_name("emp.work_id").send_keys('WNCD080')
        #输入职位
        self.driver.find_element_by_name("emp.position").send_keys('工程师')
        #输入电话
        self.driver.find_element_by_name("emp.tel").send_keys('15214345563')
        #输入qq
        self.driver.find_element_by_name("emp.qq").send_keys('1234567865')
        #输入邮箱
        self.driver.find_element_by_name("emp.email").send_keys('132445@qq.com')
        #随机选择性别
        self.driver.find_element_by_name("emp.sex").click()
        random_count = random.randrange(0, 2)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #点击保存
        self.driver.find_element_by_id("addEmpBtn").click()
    #修改功能
    def modification(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'人事管理')]").click()
        self.driver.find_element_by_xpath("//td[9]/button").click()
       #随机选择一个区域
        self.driver.find_element_by_xpath("//div[4]/div/div/form/div/div/div/select").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择一个部门
        self.driver.find_element_by_xpath("(//select[@name='emp.department_id'])[2]").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择一个状态
        self.driver.find_element_by_name("emp.emp_status").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择性别
        self.driver.find_element_by_xpath("(//select[@name='emp.sex'])[2]").click()
        random_count = random.randrange(0, 2)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #修改姓名
        self.driver.find_element_by_xpath("//form[@id='modifyEmp-form']/div/div[2]/div/input").send_keys("")
        #修改工号
        self.driver.find_element_by_xpath("//form[@id='modifyEmp-form']/div/div[2]/div[2]/input").send_keys("")
        #职位修改
        self.driver.find_element_by_xpath("//div[4]/div/div/form/div/div[3]/div/input").send_keys("")
        #修改电话
        self.driver.find_element_by_xpath("//form[@id='modifyEmp-form']/div/div[4]/div/input").send_keys("")
        #修改qq
        self.driver.find_element_by_xpath("//form[ @ id = 'modifyEmp-form'] / div / div[5] / div / input")
        #修改邮箱
        self.driver.find_element_by_xpath("//form[ @ id = 'modifyEmp-form'] / div / div[4] / div[2] / input").send_keys("")
        #点击保存
        self.driver.find_element_by_id("modifyEmpBtn").click()

    def page_number(self):
        #点击每页记录条数
        self.driver.find_element_by_xpath("//div[@id='content']/div[2]/div[3]/div[2]/div[4]/div/span[2]/span/button").click()
        #随机产生一个数
        random_count = random.randrange(0, 4)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)#选择每页展示数
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #点击页码数，跳转
        self.driver.find_element_by_xpath("(//a[contains(@href, '#')])[10]").click()

if __name__ == "__main__":
    PM=PersonalManagement()
    PM.login()
    # PM.staff_management()
    # PM.new_staff()
    PM.modification()
    PM.modification()