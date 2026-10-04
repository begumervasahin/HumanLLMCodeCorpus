import pymysql.cursors
def get_online_connection():
    return pymysql.connect(
        host='192.168.100.253',
        port=3306,
        user='unireader',
        password='7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
        db='uniqueway_production',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
def get_local_connection():
    return pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='uniqueway_development',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
def get_mysql_connection():
    return get_local_connection()
if __name__ == "__main__":
    online_conn = get_online_connection()
    print("Connected to the online database.")
    local_conn = get_local_connection()
    print("Connected to the local database.")
    default_conn = get_mysql_connection()
    print("Connected using the default connection function.")
    online_conn.close()
    local_conn.close()
    default_conn.close()
    print("Closed all connections.")