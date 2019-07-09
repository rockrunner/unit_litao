#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 9i
#====#====#====#====
from pykeyboard import PyKeyboard
from selenium import webdriver
import unittest
import os,time,random
from selenium.webdriver import ActionChains


class MarketSale(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.system('taskkill /f /im firefox.exe')
        cls.firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        cls.driver_path = r'F:\driver\geckodriver.exe'
        cls.driver = webdriver.Firefox(firefox_binary=cls.firefox_path, executable_path=cls.driver_path)
        cls.driver.get('http://192.168.1.130:8080/WoniuBoss2.5/')
        cls.driver.maximize_window()
        cls.keyboard = PyKeyboard()
        time.sleep(2)


    def test01(self):
        self.driver.find_element_by_name("userName").click()
        self.driver.find_element_by_name("userName").clear()
        self.driver.find_element_by_name("userName").send_keys("WNCD000")
        self.driver.find_element_by_name("userPass").click()
        self.driver.find_element_by_name("userPass").clear()
        self.driver.find_element_by_name("userPass").send_keys("woniu123")
        self.driver.find_element_by_name("checkcode").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/button").click()
        time.sleep(3)

    def test02(self):
        self.driver.find_element_by_link_text('市场营销').click()
        mar=self.driver.page_source
        self.assertIn(u"上传专属" , mar)
        print("市场营销页面打开成功")
    def test03(self):
        self.driver.find_element_by_xpath("//div[@id='queryDiv']/select").click()
        #随机选择地区
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择状态
        self.driver.find_element_by_name("cus.last_status").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #第一个时间框
        self.driver.find_element_by_xpath("//div[@id='queryDiv']/input").click()
        self.keyboard.press_key(self.keyboard.delete_key)
        self.driver.find_element_by_xpath("//div[2]/div[2]/input").send_keys("2018-03-01")
        #第二个时间框
        self.driver.find_element_by_xpath("//div[@id='queryDiv']/input[2]").click()
        self.keyboard.press_key(self.keyboard.delete_key)
        self.driver.find_element_by_xpath("//div[@id='queryDiv']/input[2]").send_keys("2018-11-01")
        #点击查询
        self.driver.find_element_by_xpath("//div[@id='queryDiv']/button").click()
    def test04(self):
        self.driver.find_element_by_xpath("//button[@onclick='showUpResModal();']").click()
        mar = self.driver.page_source
        self.assertIn(u"上传专属简历", mar)
        print("上传专属简历窗口打开成功")
        #关闭窗口
        self.driver.find_element_by_xpath("//div[@id='upRes-modal']/div/div/div/button").click()
    def test05(self):
        self.driver.find_element_by_xpath("//button[@onclick='showUpResModal();']").click()
        self.driver.find_element_by_xpath("//form[@id='form1']/div/div/select").click()
        #随机选择区域和部门
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)

        self.driver.find_element_by_xpath("//form[@id='form1']/div/div[2]/select").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        webdriver.ActionChains(self.driver).click(self.driver.find_element_by_xpath("//form[@id='form1']/div[2]/span/input")).perform()
        self.keyboard.type_string(r"C:\\Users\Administrator\Desktop\test-B.xls")
        time.sleep(3)
        self.keyboard.press_key(self.keyboard.enter_key)
        self.keyboard.release_key(self.keyboard.enter_key)

    def test06(self):
        #点击新增网络
        self.driver.find_element_by_xpath("button[@onclick='showAddResModal();']").click()
        #随机选择区域
        self.driver.find_element_by_name("cus.region").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择部门
        self.driver.find_element_by_name("cus.department_id").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择性别
        self.driver.find_element_by_name("cus.sex").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择最新状态
        self.driver.find_element_by_xpath("//form[@id='addResource-form']/div/div[3]/div/select").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择学历
        self.driver.find_element_by_xpath("//form[@id='addResource-form']/div/div[4]/div[2]/select").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择渠道来源
        self.driver.find_element_by_xpath("cus.source").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #随机选择工作年限
        self.driver.find_element_by_xpath("//form[@id='addResource-form']/div/div[5]/div[2]/select").click()
        random_count = random.randrange(1, 3)
        print(random_count)
        for i in range(random_count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(1)
        #点击保存
        self.driver.find_element_by_id("addCusBtn").click()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
        unittest.main()



