#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import requests

class Woniuboss:
        def __init__(self):
           self.session=requests.session()

        def test_login(self):
            # session=requests.session()
            data = {"userName": "WNCD000", "userPass": "woniu123", "checkcode": "0000"}#userName=WNCD000&userPass=woniu123&checkcode=0000
            resp = self.session.post("http://192.168.1.102:8080/WoniuBoss2.5/log/userLogin", data=data)
            # print(resp.text)
            if resp.text == 'success':
                print('首页登陆测试成功')
            else:
                print('首页登陆测试失败')
        #市场营销页面打开测试
        def market_sale(self):
            resp=self.session.get('http://192.168.1.102:8080/WoniuBoss2.5/market')
            # print(resp.text)
            if '市场营销'in resp.text:
                print("市场营销页面打开成功")
            else:
                print("市场营销页面打开失败")

            #新增资源模块，地区下拉框选择测试
        def Area_selection(self):
            data = {"pageSize":"10","pageIndex":"1","regionId":"%E6%88%90%E9%83%BD","empName":"","status":"","tartTime":"","endTime":""}#pageSize=10&pageIndex=1&region=%E6%88%90%E9%83%BD&status=&startTime=&endTime=
            resp = self.session.post("http://192.168.1.102:8080/WoniuBoss2.5/market/queryNetCus", data=data)
            # print(resp.text)
            if resp.text == '{"totalRow":0,"pageNumber":1,"firstPage":true,"lastPage":true,"totalPage":0,"pageSize":10,"list":[]}':
                print('地区选择测试成功')
            else:
                print('地区选择测试失败')

        def State_selection(self):#部门下拉框选择测试
            data = {"pageSize": "10", "pageIndex": "1", "regionId": "%E6%88%90%E9%83%BD", "status": "%E5%B7%B2%E9%A2%84%E7%BA%A6",
                    "tartTime": "","endTime": ""}
            resp = self.session.post("http://192.168.1.102:8080/WoniuBoss2.5/market/queryNetCus", data=data)
            # print(resp.text)
            if resp.text == '{"totalRow":0,"pageNumber":1,"firstPage":true,"lastPage":true,"totalPage":0,"pageSize":10,"list":[]}':
                print('部门选择测试成功')
            else:
                print('部门选择测试失败')

        # 查询按钮测试
        def Query_button(self):
            data={"pageSize":"10","pageIndex":"1","region":"%E9%87%8D%E5%BA%86","status":"%E5%B7%B2%E6%8A%A5%E5%90%8D","startTime":"2018-04-03","endTime":"2019-01-10"}
            resp=self.session.post('http://192.168.1.102:8080/WoniuBoss2.5/market/queryNetCus',data=data)
            print(resp.text)
            if resp.text == '{"totalRow":0,"pageNumber":1,"firstPage":true,"lastPage":true,"totalPage":0,"pageSize":10,"list":[]}':
                print('查询测试成功')
            else:
                print('查询测试失败')

        def Upload_exclusive(self):
             data={}
             resp=self.session.post('http://192.168.1.102:8080/WoniuBoss2.5/select/getRegion',data=data)
             print(resp.text)
             if '{"region_id":1,"region_name":"成都"},{"region_id":2,"region_name":"重庆"},{"region_id":3,"region_name":"西安"}'in resp.text:
                 print("上传专属窗口打开测试成功")
             else:
                 print('上传专属窗口测试打开失败')

        #上传专属窗口的地区选择测试和部门选择测试
        def Upload_exclusive_region_department(self):
            data={}
            resp=self.session.post('http://192.168.1.102:8080/WoniuBoss2.5/select/getDept?regionId=1',data=data)
            print(resp.text)
            if '{"department_id":1,"department_name":"管理部"},{"department_id":2,"department_name":"就业部"},{"department_id":3,"department_name":"咨询部"},{"department_id":4,"department_name":"电销部"},{"department_id":5,"department_name":"渠道部"},{"department_id":6,"department_name":"市场部"},{"department_id":7,"department_name":"教学部"},{"department_id":8,"department_name":"研发部"},{"department_id":9,"department_name":"财务部"}' in resp.text:
                print('上传专属窗口的地区选择测试和部门选择测试成功')
            else:
                print('上传专属窗口的地区选择测试和部门选择测试失败')
        #上传简历文件测试--------不会
        def Upload_Resume(self):
            data={}
            resp=self.session.post()
            print(resp.text)
            if resp.text =='':
                print('查询测试成功')
            else:
                print('查询测试失败')

        #新增网络窗口打开测试
        def New_Network(self):
            data = {}
            resp = self.session.post('http://192.168.1.102:8080/WoniuBoss2.5/select/getRegion',data=data)
            print(resp.text)
            if resp.text == '[{"region_id":1,"region_name":"成都"},{"region_id":2,"region_name":"重庆"},{"region_id":3,"region_name":"西安"}]':
                print('新增网络窗口打开测试成功')
            else:
                print('新增网络窗口打开测试失败')
        #新增网络窗口中的地区下拉框选择测试
        def New_Network_region(self):
            data={"region":"1"}
            resp=self.session.post('http://192.168.1.102:8080/WoniuBoss2.5/select/seeDept',data=data)
            print(resp.text)
            if resp.text=='[{"department_id":1,"department_name":"管理部"},{"department_id":2,"department_name":"就业部"},{"department_id":3,"department_name":"咨询部"},{"department_id":4,"department_name":"电销部"},{"department_id":5,"department_name":"渠道部"},{"department_id":6,"department_name":"市场部"},{"department_id":7,"department_name":"教学部"},{"department_id":8,"department_name":"研发部"},{"department_id":9,"department_name":"财务部"}]':
                print("新增网络窗口中的地区下拉框选择测试成功")
            else:
                print("新增网络窗口中的地区下拉框选择测试失败")
        #新增网络窗口中的电话号码和部门选择测试
        def New_Network_department_phonenum(self):
            data = {"tel":"13565678978","deptId":"4"}
            resp = self.session.post('http://192.168.1.102:8080/WoniuBoss2.5/market/showCusInfo', data=data)
            print(resp.text)
            if resp.text=='null':
                print("新增网络窗口中的电话号码和部门选择测试成功")
            else:
                print("新增网络窗口中的电话号码和部门选择测试失败")
        #













if __name__=="__main__":
    wb=Woniuboss()
    wb.test_login()
    wb.market_sale()
    wb.Area_selection()
    wb.State_selection()
    wb.Query_button()
    wb.Upload_exclusive()
    wb.New_Network()
    wb.New_Network_region()
    wb.New_Network_department_phonenum()