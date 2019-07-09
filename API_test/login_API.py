#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#

import requests
import unittest
from selenium import webdriver

class personalManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session=requests.session()


    @classmethod
    def tearDownClass(cls):
        pass

    def test_login(self):
        # session=requests.session()
        data={"userName":"WNCD000","userPass":"woniu123","checkcode":"0000"}
        resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/log/userLogin",data=data)
        print(resp.text)
        if resp.text == 'success':
            print('首页登陆测试成功')
        else:
            print('首页登陆测试失败')


if __name__=='__main__':
      unittest.main()

