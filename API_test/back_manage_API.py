#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import requests


class Bcak_Manage:
    #初始化和登陆
    def __init__(self):
        self.session=requests.session()
    def test_login(self):
        data={"userName":"WNCD000","userPass":"woniu123","checkcode":"0000"}
        resp=self.session.post("http://192.168.1.122:8080/WoniuBoss2.5/log/userLogin",data=data)
        print(resp.text)
        if resp.text == 'success':
            print('首页登陆测试成功')
        else:
            print('首页登陆测试失败')

    #打开后台管理页面测试
    def open_backmanage(self):
        resp=self.session.get(' http://192.168.1.122:8080/WoniuBoss2.5/res')
        # print(resp.text)
        if '菜单管理'in resp.text:
            print('打开后台管理页面测试成功')
        else:
            print('打开后台管理页面测试失败')
    #资源树窗口打开测试
    def open_Resource_tree(self):
        data={{}}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/res/getResTreeNode',data=data)
        if '[{"des":"顶级目录","modifydate":"2018-06-19 00:00:00","name":"全部","pid":0,"id":1,"iconCls":"am-icon-desktop","type":1,"url":"#","seq":10,"open":true},{"des":null,"modifydate":null,"name":"转交责任人","pid":1,"id":2,"iconCls":"am-icon-coffee","type":1,"url":"/transmit/**","seq":1},{"des":null,"modifydate":null,"name":"分配资源","pid":2,"id":3,"iconCls":"am-icon-group","type":2,"url":"/allot/**","seq":10},{"des":null,"modifydate":null,"name":"公共资源池","pid":2,"id":4,"iconCls":"am-icon-user","type":2,"url":"/public/**","seq":11},{"des":null,"modifydate":null,"name":"新增固定资产","pid":2,"id":9,"iconCls":"am-icon-fire","type":2,"url":"/assets/showAddAssModal/","seq":1},{"des":null,"modifydate":null,"name":"修改固定资产","pid":1,"id":12,"iconCls":"am-icon-files-o","type":1,"url":"/assets/showModAssModal/","seq":1},{"des":null,"modifydate":null,"name":"晨考","pid":12,"id":18,"iconCls":"am-icon-bookmark-o","type":2,"url":"/system/res/delete","seq":11},{"des":null,"modifydate":null,"name":"考勤","pid":12,"id":19,"iconCls":"am-icon-bookmark","type":2,"url":"/system/res/save","seq":11},{"des":null,"modifydate":null,"name":"排课","pid":12,"id":28,"iconCls":"am-icon-bookmark-o","type":2,"url":"/system/role/delete","seq":11},{"des":null,"modifydate":null,"name":"就业管理","pid":1,"id":29,"iconCls":"am-icon-bookmark","type":1,"url":"/system/role/save","seq":11},{"des":null,"modifydate":null,"name":"人事面试","pid":29,"id":36,"iconCls":"am-icon-download","type":2,"url":"/common/file/upload","seq":20},{"des":null,"modifydate":null,"name":"技术面试","pid":29,"id":63,"iconCls":"am-icon-bookmark-o","type":2,"url":"/system/user/freeze","seq":11},{"des":null,"modifydate":null,"name":"财务管理","pid":1,"id":146,"iconCls":"am-icon-folder","type":1,"url":"/system/user/list","seq":8},{"des":null,"modifydate":null,"name":"查看","pid":146,"id":147,"iconCls":"am-icon-folder","type":2,"url":"/system/user/save","seq":10},{"des":null,"modifydate":null,"name":"录入","pid":146,"id":148,"iconCls":"am-icon-folder","type":2,"url":"/system/res/batchDelete","seq":10},{"des":null,"modifydate":null,"name":"错误日志","pid":1,"id":149,"iconCls":"am-icon-file-text-o","type":1,"url":"#/system/error","seq":13},{"des":null,"modifydate":null,"name":"操作记录","pid":1,"id":150,"iconCls":"am-icon-building-o","type":1,"url":"#/system/log","seq":11},{"des":null,"modifydate":null,"name":"录入","pid":18,"id":155,"iconCls":"am-icon-file","type":2,"url":null,"seq":1},{"des":null,"modifydate":null,"name":"查看","pid":18,"id":156,"iconCls":"am-icon-file","type":2,"url":null,"seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-07-06 00:00:00","name":"","pid":18,"id":166,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-07-13 00:00:00","name":"","pid":1,"id":168,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"","pid":36,"id":169,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"","pid":36,"id":170,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"发","pid":36,"id":171,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"","pid":2,"id":172,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"你好","pid":3,"id":173,"iconCls":"am-icon-file","type":2,"url":"","seq":1}]' in resp.text:
            print('资源树窗口打开测试成功')
        else:
            print('资源树窗口打开测试失败')
    #打开设置窗口
    def save_open_set_up(self):
        data={}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/res/getResTreeNode',data=data)
        if '[{"des":"顶级目录","modifydate":"2018-06-19 00:00:00","name":"全部","pid":0,"id":1,"iconCls":"am-icon-desktop","type":1,"url":"#","seq":10,"open":true},{"des":null,"modifydate":null,"name":"转交责任人","pid":1,"id":2,"iconCls":"am-icon-coffee","type":1,"url":"/transmit/**","seq":1},{"des":null,"modifydate":null,"name":"分配资源","pid":2,"id":3,"iconCls":"am-icon-group","type":2,"url":"/allot/**","seq":10},{"des":null,"modifydate":null,"name":"公共资源池","pid":2,"id":4,"iconCls":"am-icon-user","type":2,"url":"/public/**","seq":11},{"des":null,"modifydate":null,"name":"新增固定资产","pid":2,"id":9,"iconCls":"am-icon-fire","type":2,"url":"/assets/showAddAssModal/","seq":1},{"des":null,"modifydate":null,"name":"修改固定资产","pid":1,"id":12,"iconCls":"am-icon-files-o","type":1,"url":"/assets/showModAssModal/","seq":1},{"des":null,"modifydate":null,"name":"晨考","pid":12,"id":18,"iconCls":"am-icon-bookmark-o","type":2,"url":"/system/res/delete","seq":11},{"des":null,"modifydate":null,"name":"考勤","pid":12,"id":19,"iconCls":"am-icon-bookmark","type":2,"url":"/system/res/save","seq":11},{"des":null,"modifydate":null,"name":"排课","pid":12,"id":28,"iconCls":"am-icon-bookmark-o","type":2,"url":"/system/role/delete","seq":11},{"des":null,"modifydate":null,"name":"就业管理","pid":1,"id":29,"iconCls":"am-icon-bookmark","type":1,"url":"/system/role/save","seq":11},{"des":null,"modifydate":null,"name":"人事面试","pid":29,"id":36,"iconCls":"am-icon-download","type":2,"url":"/common/file/upload","seq":20},{"des":null,"modifydate":null,"name":"技术面试","pid":29,"id":63,"iconCls":"am-icon-bookmark-o","type":2,"url":"/system/user/freeze","seq":11},{"des":null,"modifydate":null,"name":"财务管理","pid":1,"id":146,"iconCls":"am-icon-folder","type":1,"url":"/system/user/list","seq":8},{"des":null,"modifydate":null,"name":"查看","pid":146,"id":147,"iconCls":"am-icon-folder","type":2,"url":"/system/user/save","seq":10},{"des":null,"modifydate":null,"name":"录入","pid":146,"id":148,"iconCls":"am-icon-folder","type":2,"url":"/system/res/batchDelete","seq":10},{"des":null,"modifydate":null,"name":"错误日志","pid":1,"id":149,"iconCls":"am-icon-file-text-o","type":1,"url":"#/system/error","seq":13},{"des":null,"modifydate":null,"name":"操作记录","pid":1,"id":150,"iconCls":"am-icon-building-o","type":1,"url":"#/system/log","seq":11},{"des":null,"modifydate":null,"name":"录入","pid":18,"id":155,"iconCls":"am-icon-file","type":2,"url":null,"seq":1},{"des":null,"modifydate":null,"name":"查看","pid":18,"id":156,"iconCls":"am-icon-file","type":2,"url":null,"seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-07-06 00:00:00","name":"","pid":18,"id":166,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-07-13 00:00:00","name":"","pid":1,"id":168,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"","pid":36,"id":169,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"","pid":36,"id":170,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"发","pid":36,"id":171,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"","pid":2,"id":172,"iconCls":"am-icon-file","type":2,"url":"","seq":1},{"des":"\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t","modifydate":"2018-02-04 00:00:00","name":"你好","pid":3,"id":173,"iconCls":"am-icon-file","type":2,"url":"","seq":1}]' in resp.text:
            print('设置窗口打开测试成功')
        else:
            print('设置窗口打开测试失败')
#每页显示条数设为25
    def page_size(self):
        data={"pageSize":"25","pageIndex":"1"}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/res/queryRes',data=data)
        if '"pageSize":25' in resp.text:
            print('每页显示条数设为25测试成功')
        else:
            print('每页显示条数设为25测试失败')
    #点击页码数2,跳转页面
    def page_num(self):
        data={"pageSize":"25","pageIndex":"2"}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/res/queryRes',data=data)
        if '"pageNumber":2' in resp.text:
            print('页面跳转到第2页测试成功')
        else:
            print('页面跳转到第2页测试失败')
    #角色管理板块打开测试
    def role_manage(self):
        data={"pageSize":"10","pageIndex":"1"}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/role/queryRole',data=data)
        if "研发总监" in resp.text:
            print('角色管理页面打开测试成功')
        else:
            print('角色管理页面打开测试失败')

    #打开授权窗口打开测试
    def open_accredit(self):
        data={}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/role/getResTreeNodeByRoleId?roleId=1',data=data)
        # print(resp.text)
        if '公共资源池'in resp.text:
            print('授权页面打开测试成功')
        else:
            print('授权页面打开测试失败')
    #用户管理板块打开测试
    def open_user_manage(self):
        data={'pageSize':'10','pageIndex':'1','userName':''}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/user/queryUser',data=data)
        # print(resp.text)
        if 'createdate'in resp.text:
            print('用户管理板块打开测试成功')
        else:
            print('用户管理板块打开测试失败')
    #设置窗口打开测试
    def open_set_up(self):
        data={}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/user/getTreeNode?id=1',data=data)
        if '总经理'in resp.text:
            print('设置窗口打开测试成功')
        else:
            print('设置窗口打开测试失败')
    #字典管理板块打开测试
    def dict_manage(self):
        data={'pageSize':'10','pageIndex':'1'}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/option/queryDictType',data=data)
        if '员工状态'in resp.text:
            print('字典管理板块打开测试成功')
        else:
            print('字典管理板块打开测试失败')
    #资源状态的新增按钮测试
    def open_newresource_status(self):
        data={'dd.dict_type_id':'1','dd.dict_value':'','dd.dict_key':'','dd.sort':'','dd.remarks':''}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/option/saveAddDictOption',data=data)
        # print(resp.text)
        if 'success'==resp.text:
            print('新增资源状态测试成功')
        else:
            print('新增资源状态测试失败')
    #启用停用按钮测试
    def Disable_enable(self):
        data={'typeId':'1','status':'%E5%81%9C%E7%94%A8'}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/option/updateDictTypeStatus',data=data)
        if 'success'==resp.text:
            print('启用按钮测试成功')
        else:
            print('启用按钮测试失败')
    #详情窗口测试
    def open_detail(self):
        data={'pageSize':'30','pageIndex':'1'}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/option/queryDictDetail?typeId=1',data=data)
        if '已报名'in resp.text:
            print('详情窗口测试成功')
        else:
            print('详情窗口测试失败')

    #详情窗口下的编辑窗口
    def open_detail_edit(self):
        data={'dd.dict_type_id':'1','dd.dict_data_id':'1','dict_typename':'%E8%B5%84%E6%BA%90%E7%8A%B6%E6%80%81','dd.dict_value':'%E6%96%B0%E5%85%A5%E5%BA%93','dd.sort':'10','dd.remarks':''}
        resp=self.session.post('http://192.168.1.122:8080/WoniuBoss2.5/option/saveEditDictDetail',data=data)
        if 'success'==resp.text:
            print('编辑窗口打开测试成功')
        else:
            print('编辑窗口打开测试失败')

if __name__=="__main__":
     bm=Bcak_Manage()
     bm.test_login()
     bm.open_backmanage()
     bm.open_accredit()
     bm.open_user_manage()
     bm.dict_manage()
     bm.open_newresource_status()
     bm.Disable_enable()
     bm.open_detail()