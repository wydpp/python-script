#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:wydpp

'''
pip3 install PyMySQL
'''

import pymysql

def query():
    #打开数据库连接
    db = pymysql.connect("127.0.0.1","root","root","wydpp")
    cursor = db.cursor()
    try:
        #执行sql
        cursor.execute("select * from user")
        #获取结果
        results = cursor.fetchall()
        #遍历数据
        for row in results:
            id = row[0]
            name=row[1]
            age=row[2]
            createTime = row[3]
            print(row,id,name,age,createTime)
    except:
        print("db execute error")
    #关闭连接
    db.close()


def insert():
    #打开数据库连接
    db = pymysql.connect("127.0.0.1","root","root","wydpp")
    cursor = db.cursor()
    try:
        #执行插入sql
        insertSql = "insert into user(name,age) values ('cat',38)"
        #updateSql= "update user set age = 40 where name = 'cat'"
        cursor.execute(insertSql)
        db.commit()
    except:
        db.rollback()
        print("db execute error")
    #关闭连接
    db.close()
