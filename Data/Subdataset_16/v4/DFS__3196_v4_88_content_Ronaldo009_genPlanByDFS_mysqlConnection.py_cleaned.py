import pymysql.cursors
def fonk1():
    return pymysql.connect(
        b1 = '192.168.100.253',
        b2 = 3306,
        b3 = 'unireader',
        b4 = '7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
        b5 = 'uniqueway_production',
        b6 = 'utf8',
        b7 = pymysql.cursors.DictCursor
    )
def fonk2():
    return pymysql.connect(
        b1 = 'localhost',
        b2 = 3306,
        b3 = 'root',
        b5 = 'uniqueway_development',
        b6 = 'utf8',
        b7 = pymysql.cursors.DictCursor
    )
def fonk3():
    return fonk2()
if b8 = = "__main__":
    b9 = fonk1()
    print("Connected to the online database.")
    b10 = fonk2()
    print("Connected to the local database.")
    b11 = fonk3()
    print("Connected using the default connection function.")
    b9.close()
    b10.close()
    b11.close()
    print("Closed all connections.")