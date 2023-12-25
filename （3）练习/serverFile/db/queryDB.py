import pymysql

from conf.variable import dbInfo

# 查询用户信息
def selectAccountInfo(username):
    connect = pymysql.connect(host = dbInfo[0],user = dbInfo[1],password = dbInfo[2],db = dbInfo[3],port = dbInfo[4],charset = dbInfo[5])
    cursor = connect.cursor()
    # sql = "SELECT username,password FROM %s WHERE username='%s'" % (dbInfo[6、matplotlib学习],username)
    sql = "SELECT username,pwd FROM %s WHERE username = '%s'" % (dbInfo[6],username)
    cursor.execute(sql)
    result = cursor.fetchall()

    return result