# -*- coding: utf-8 -*-

"""
    1.在终端上手动输入学校代理服务器/教室基站变量，每输完一个学校代理服务器/教室基站的环境变量，保存到一个变量中，返回给数据库函数操作，存入到数据库中:
        其中:1>输入值必须有效，不能为空；
            2>输入quit/exit退出程序，并当输入的学校环境变量不完整时，不会插入到数据库中。
            注释:a.对于学校/教室ID及IP等，还可以根据规则进行进一步的输入判定，此暂不考虑它的逻辑代码实现
            注释:b.此未做防止重复插入操作的逻辑实现
"""

import sys
import pymysql


class DB():
    def __init__(self, host='10.0.5.229', port=3307, db='campusenv', user='root', passwd='lqx20191125', charset='utf8mb4'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


def getCampusEnv(envList):
    getAllVariable = []
    campusenvList = envList
    for i in range(len(campusenvList)):
        inputContext = "------请输入学校的" + campusenvList[i] + "(如需退出程序，请入输入exit/quit):------\n"
        getValue = input(inputContext)
        try:
            while True:
                if getValue == "":
                    print("------不能输入空值，请重新输入------")
                    getValue = input(inputContext)
                else:
                    break
        except:
            pass
        if getValue == "exit" or getValue == "quit":
            sys.exit()
        getAllVariable.append(getValue)
    return getAllVariable

def enterMysql(envList, sqlStr, sqlTable):
    getList = getCampusEnv(envList)
    insertSql = "INSERT INTO " + sqlTable + sqlStr +  " VALUES " + str(tuple(getList))
    with DB() as db:
        db.execute(insertSql)

def getImportValue(getNext):
    if getNext == "N" or getNext == "n":
        sys.exit()
    elif getNext == "L" or getNext == "l":
        disposeSchool()
    elif getNext == "Y" or getNext == "y":
        disposeClass()
    else:
        sys.exit()

def disposeSchool():
    while True:
        schoolenvList = ["学校名称", "代理服务器远程连接端口", "学校部署环境", "学校代理服务器IP", "学校代理服务器ID", "学校SIGNATURE_KEY", "cjcbs版本", "cjpadc版本", "apk版本", "教室IP白名单"]
        insertSqlStr = "(school_name, frpc_remote_port, campus_env, school_ip, school_id, signature_key, cjcbs_docker_version, cjpadc_docker_version, cjpad_docker_version, ip_whitelist)"
        enterMysql(envList=schoolenvList, sqlStr=insertSqlStr, sqlTable="school_env")
        inputStr = "你已输入一所学校部署代理服务器的变量，您是否还继续?如果:\n" \
                   "1.想继续输入同一所学校，相应班级的部署变量，请输入:'Y/y'\n" \
                   "2.想继续输入另一所学校，请输入:'L/l'\n" \
                   "3.想结束此次会话，请输入:'N/n'，或其它操作\n" \
                   "-----------nature----------\n"
        getNext = input(inputStr)
        getImportValue(getNext)

def disposeClass():
    while True:
        classenvList = ["学校教室名称", "教室远程连接端口", "教室IP", "教室ID", "AP连接IP"]
        insertSqlStr = "(class_name, frpc_remote_port, class_ip, class_id, cjpadc_cbs_host)"
        enterMysql(envList=classenvList, sqlStr=insertSqlStr, sqlTable="class_env")
        inputStr = "你已输入一所学校部署基站服务器的变量，您是否还继续?如果:\n" \
                   "1.想继续输入同一所学校，其它班级的部署变量，请输入:'Y/y'\n" \
                   "2.想继续输入另一所学校，请输入:'L/l'\n" \
                   "3.想结束此次会话，请输入:'N/n'，或其它操作\n" \
                   "-----------nature----------\n"
        getNext = input(inputStr)
        getImportValue(getNext)

if __name__ == "__main__":
    getNext = "--------您将输入学校，还是教室，如果:\n" \
             "1.想输入学校，请输入:'L/l'\n" \
             "2.想输入教室，请输入:'Y/y\n" \
             "3.想结束会话，请输入:'N/n'，或其它操作----------\n"
    getNext = input(getNext)
    getImportValue(getNext)