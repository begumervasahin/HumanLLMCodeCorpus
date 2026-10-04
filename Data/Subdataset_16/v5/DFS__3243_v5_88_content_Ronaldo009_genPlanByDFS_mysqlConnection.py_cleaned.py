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
def fonk5(conn, name):
    if conn:
        print(f"Successfully connected to the {name} database.")
    else:
        print(f"Failed to connect to the {name} database.")
def fonk6(conn, name):
    if conn:
        conn.close()
        print(f"Closed the connection to the {name} database.")
if b8 = = "__main__":
    b9 = fonk2()
    fonk5(b9, "online")
    b10 = fonk3()
    fonk5(b10, "local")
    b11 = fonk4()
    fonk5(b11, "default")
    fonk6(b9, "online")
    fonk6(b10, "local")
    fonk6(b11, "default")