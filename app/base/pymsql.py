# -*- coding:utf-8 -*-
import pymysql
from app.util.operation_excel import OperationExcel
#获取更新sql数据


# 链接数据库
conn = pymysql.connect(user='code_test', password='reVvtDiN2g3JaCxc',
                       host='zljsz-testenvironmentdb.mysql.rds.aliyuncs.com',
                       port=3306,database='panda')
# 使用cursor()方法创建一个游标对象cursor
cursor = conn.cursor()
#SQL 更新语句
sql = "sql"
try:
    #执行SQL语句
    cursor.execute(sql)
    conn.commit()
    print("updata ok")
except:
    # 发生错误时回滚
    conn.rollback()
#关闭数据库链接
conn.close()