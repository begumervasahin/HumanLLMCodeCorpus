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
    return fonk2()
if b9 = = "__main__":
    try:
        b10 = fonk1()
        print("Successfully connected to the online database.")
    except Exception as e:
        print(f"Failed to connect to the online database: {e}")
    try:
        b11 = fonk2()
        print("Successfully connected to the local database.")
    except Exception as e:
        print(f"Failed to connect to the local database: {e}")
    try:
        b12 = fonk3()
        print("Successfully connected using the mysql_connection function.")
    except Exception as e:
        print(f"Failed to connect using the mysql_connection function: {e}")
    for conn, name in zip([b10, b11, b12], ["online", "local", "default"]):
        if conn:
            conn.close()
            print(f"Closed the b1 to the {name} database.")