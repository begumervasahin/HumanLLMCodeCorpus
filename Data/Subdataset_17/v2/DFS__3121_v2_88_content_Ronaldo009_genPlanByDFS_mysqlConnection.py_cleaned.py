import pymysql.cursors
def online_connection():
    connection = pymysql.connect(
        host='192.168.100.253',
        port=3306,
        user='unireader',
        password='7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
        db='uniqueway_production',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
def local_connection():
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='uniqueway_development',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
def mysql_connection():
    return local_connection()
if __name__ == "__main__":
    try:
        online_conn = online_connection()
        print("Successfully connected to the online database.")
    except Exception as e:
        print(f"Failed to connect to the online database: {e}")
    try:
        local_conn = local_connection()
        print("Successfully connected to the local database.")
    except Exception as e:
        print(f"Failed to connect to the local database: {e}")
    try:
        default_conn = mysql_connection()
        print("Successfully connected using the mysql_connection function.")
    except Exception as e:
        print(f"Failed to connect using the mysql_connection function: {e}")
    for conn, name in zip([online_conn, local_conn, default_conn], ["online", "local", "default"]):
        if conn:
            conn.close()
            print(f"Closed the connection to the {name} database.")