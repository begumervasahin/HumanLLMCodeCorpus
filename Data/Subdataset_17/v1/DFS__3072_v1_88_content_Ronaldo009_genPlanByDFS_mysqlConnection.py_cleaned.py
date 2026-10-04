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
    connection = local_connection()
    return connection
if __name__ == "__main__":
    online_conn = online_connection()
    print("Connected to the online database.")
    local_conn = local_connection()
    print("Connected to the local database.")
    default_conn = mysql_connection()
    print("Connected using the mysql_connection function.")
    online_conn.close()
    local_conn.close()
    default_conn.close()