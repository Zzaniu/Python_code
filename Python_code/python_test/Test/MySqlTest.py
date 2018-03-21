# coding=utf-8


from hashlib import sha1
from MySQLdb import *


haxi = sha1()
haxi.update("!wenjunai93*")
a = haxi.hexdigest()
print a

try:
    conn = connect(host='192.168.6.66', port=3306, user='root', passwd='wenjunai93', db='python', charset='utf8')
    cursor1 = conn.cursor()

    # name = raw_input("请输入你要插入的姓名:")
    # birthday = raw_input("请输入你要插入的生日:")
    # params = [name, birthday]
    # sql = "insert into students(name,birthday) values(%s,%s)"
    # # sql = "delete from students where id>6"
    # cursor1.execute(sql, params)
    cursor1.execute("select * from students")
    result = cursor1.fetchall()
    for i in result:
        for ii in i:
            print ii

    conn.commit()

    cursor1.close()
    conn.close()
except Exception, e:
    print "错误..."
    print e.message