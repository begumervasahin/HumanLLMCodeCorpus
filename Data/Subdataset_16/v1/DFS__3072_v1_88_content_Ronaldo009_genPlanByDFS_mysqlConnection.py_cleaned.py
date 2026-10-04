import pymysql.cursors
def fonk1():
    b1 = pymysql.connect(
        b2 = '192.168.100.253',
        b3 = 3306,
        b4 = 'unireader',
        b5 = '7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
        b6 = 'uniqueway_production',
        b7 = 'utf8',
        b8 = pymysql.cursors.DictCursor
    )
    return b1
def fonk2():
    b1 = pymysql.connect(
        b2 = 'localhost',
        b3 = 3306,
        b4 = 'root',
        b6 = 'uniqueway_development',
        b7 = 'utf8',
        b8 = pymysql.cursors.DictCursor
    )
    return b1
def fonk3():
    b1 = fonk2()
    return b1
if b9 = = "__main__":
    b10 = fonk1()
    print("Connected to the online database.")
    b11 = fonk2()
    print("Connected to the local database.")
    b12 = fonk3()
    print("Connected using the mysql_connection function.")
    b10.close()
    b11.close()
    b12.close()