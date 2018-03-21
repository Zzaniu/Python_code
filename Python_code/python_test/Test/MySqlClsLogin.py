# coding=utf-8


from MySqlCls import MySqlCls
from hashlib import sha1


def in_put():
    user = raw_input("请输入用户名:")
    password = raw_input("请输入密码:")
    encrypt = sha1()
    encrypt.update(password)
    up_password = encrypt.hexdigest()
    return user, password, up_password


def login(t_login):
    user, password, up_password = in_put()
    sql = 'select users.password from users where user=%s'
    params = (user,)
    result = t_login.query(sql, params)

    if len(result) == 0:
        print "用户名错误..."
    elif result[0][0] == up_password:
        print "登陆成功..."
    else:
        print "密码错误..."


def register(t_login):
    user, password, up_password = in_put()
    sql = "select users.user from users where user=%s"
    result = t_login.query(sql, (user,))
    if 0 == len(result):
        sql = 'insert into users(user, password) value(%s,%s)'
        params = (user, up_password)
        t_login.cute(sql, params)
        print "注册成功..."
    else:
        print "用户名 '%s' 已注册，请换个别的用户名..."%user


def account_cancellation(t_login):
    '''销户'''
    user = raw_input("请输入想要销户的用户名:")

    sql = 'delete from users where user=%s'
    params = (user,)
    t_login.cute(sql, params)
    print "销户成功..."


def main():
    user_flg = raw_input(r"你想要注册还是登陆？\r\n1：登陆\r\n2:注册\r\n3:销户\r\n请输入对应数字(默认登陆):")
    t_login = MySqlCls('192.168.6.66', 3306, 'root', 'wenjunai93', 'python')
    if "1" == user_flg or '' == user_flg:
        login(t_login)
    elif "2" == user_flg:
        register(t_login)
    elif '3' == user_flg:
        account_cancellation(t_login)
    else:
        print "输入有误，程序退出..."


if __name__ == "__main__":
    main()
