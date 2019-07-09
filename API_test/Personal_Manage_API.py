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
           data = {"userName": "WNCD000", "userPass": "woniu123", "checkcode": "0000"}
           resp = self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/log/userLogin", data=data)
           # print(resp.text)
           if resp.text == 'success':
               print('首页登陆测试成功')
           else:
               print('首页登陆测试失败')

       def personalManage(self):
           resp=self.session.get('http://192.168.1.108:8080/WoniuBoss2.5/employee')
           # print(resp.text)
           if '员工管理' in resp.text:
               print("人事管理页面打开测试成功")
           else:
               print("人事管理页面打开测试失败")


       def staff_manage_01(self):
           data={"pageSize":"10","pageIndex":"1","regionId":"3","deptId":"","empName":"","status":""}
           resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/employee/queryEmpByInfo",data=data)
           # print(resp.text)#pageSize=10&pageIndex=1&regionId=1&deptId=2&empName=&status=
           if '邓秋菊'in resp.text:
               print("下拉框地区：西安选择测试成功")
           else:
               print("下拉框地区：西安选择测试失败")
       def staff_manage_02(self):
           data={"pageSize":"10","pageIndex":"1","regionId":"1","deptId":"2","empName":"","status":""}
           resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/employee/queryEmpByInfo",data=data )
           # print(resp.text)#pageSize=10&pageIndex=1&regionId=1&deptId=2&empName=&status=%E7%A6%BB%E8%81%8C
           if '就业部' in resp.text:
               print("部门选择测试成功")
           else:
               print("部门选择测试失败")


       def staff_manage_03(self):
           data={"pageSize":"10","pageIndex":"1","regionId":"1","deptId":"2","empName":"","status":"%E7%A6%BB%E8%81%8C"}#http://192.168.1.108:8080/WoniuBoss2.5/employee/queryEmpByInfo
           resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/employee/queryEmpByInfo",data=data)
           # print(resp.text)
           if '"totalRow":0,"pageNumber":1,"firstPage":true,"lastPage":true,"totalPage":0,"pageSize":10,"list":[]'in resp.text:
               print("状态下拉框选择测试成功")
           else:
               print("状态下拉框选择测试失败")
       def newly_increased(self):
           data={}
           resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/option/showRegion",data=data)
           # print(resp.text)
           if '{"region_id":1,"region_name":"成都"},{"region_id":2,"region_name":"重庆"},{"region_id":3,"region_name":"西安"}' in resp.text:
                print("新增窗口打开测试成功")
           else:
               print("新增窗口打开测试失败")

       def New_details(self):
           data={"emp.region_id":"2","emp.department_id":"12","emp.employee_name":"%E9%98%BF%E5%8F%91","emp.work_id":"WNCD090","emp.position":"%E5%92%A8%E8%AF%A2%E5%B8%88","emp.sex":"%E5%A5%B3","emp.tel":"%E5%95%8A%E5%8F%91%E9%A1%BA%E4%B8%B0","emp.email":"ab%40qq.com","emp.qq":"987654321"}
           resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/employee/addEmp",data=data)
           # print(resp.text)
           if 'success'==resp.text:
               print("新增员工测试成功")
           else:
               print("新增员工测试失败")
       def modification(self):
           data={}
           resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/option/showRegion",data=data)
           # print(resp.text)
           if '"region_name":"西安"' in resp.text:
               print("修改页面打开测试成功")
           else:
               print("修改页面打开测试失败")
       def page_source(self):
           data={"pageSize":"10","pageIndex":"3","regionId":"","deptId":"","empName":"","status":""}#pageSize=10&pageIndex=3&regionId=&deptId=&empName=&status=
           resp=self.session.post("http://192.168.1.108:8080/WoniuBoss2.5/employee/queryEmpList",data=data)#pageSize=10&pageIndex=1&regionId=&deptId=&empName=&status=
           # print(resp.text)
           if 'pageNumber":3' in resp.text:
               print("页面数字连接接跳转成功")
           else:
               print("页面数字链接跳转失败")
if __name__=='__main__':
    wb=Woniuboss()
    wb.test_login()
    wb.personalManage()
    wb.staff_manage_01()
    wb.staff_manage_02()
    wb.staff_manage_03()
    wb.newly_increased()
    wb.New_details()
    wb.modification()
    wb.page_source()


