import pymysql.cursors
def fonk1(b1, b2, b3, b4, b5):
    return pymysql.connect(
        b1 = b1,
        b2 = b2,
        b3 = b3,
        b4 = b4,
        b5 = b5,
        b6 = 'utf8',
        b7 = pymysql.cursors.DictCursor
    )
def fonk2():
    return fonk1(
        b1 = '192.168.100.253',
        b2 = 3306,
        b3 = 'unireader',
        b4 = '7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
        b5 = 'uniqueway_production'
    )
def fonk3():
    return fonk1(
        b1 = 'localhost',
        b2 = 3306,
        b3 = 'root',
        b4 = '',
        b5 = 'uniqueway_development'
    )
def fonk4():
    return fonk3()
def fonk5(connection_func, name):
    try:
        b8 = connection_func()
        print(f"Successfully connected to the {name} database.")
        return b8
    except Exception as e:
        print(f"Failed to connect to the {name} database: {e}")
        return None
def fonk6(b8, name):
    if b8:
        b8.close()
        print(f"Closed the connection to the {name} database.")
if b9 = = "__main__":
    b10 = fonk5(online_connection, "online")
    b11 = fonk5(local_connection, "local")
    b12 = fonk5(mysql_connection, "default")
    fonk6(b10, "online")
    fonk6(b11, "local")
    fonk6(b12, "default")