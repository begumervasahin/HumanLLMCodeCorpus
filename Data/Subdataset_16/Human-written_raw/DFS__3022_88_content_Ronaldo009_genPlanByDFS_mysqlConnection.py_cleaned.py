import pymysql.cursors
def fonk1():
    b1 = pymysql.connect(host='192.168.100.253',
                                 b2 = 3306,
                                 b3 = 'unireader',
                                 b4 = '7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
                                 b5 = 'uniqueway_production',
                                 b6 = 'utf8',
                                 b7 = pymysql.cursors.DictCursor)
    return b1
def fonk2():
    b1 = pymysql.connect(host='localhost',
                                 b2 = 3306,
                                 b3 = 'root',
                                 b5 = 'uniqueway_development',
                                 b7 = pymysql.cursors.DictCursor,
                                 b6 = 'utf8')
    return b1
def fonk3():
    b1 = fonk2()
    return b1