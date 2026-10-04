import pymysql.cursors
def create_connection(host, port, user, password, db):
    return pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
def online_connection():
    return create_connection(
        host='192.168.100.253',
        port=3306,
        user='unireader',
        password='7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
        db='uniqueway_production'
    )
def local_connection():
    return create_connection(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='uniqueway_development'
    )
def mysql_connection():
    return local_connection()
def connect_and_print_status(connection_func, name):
    try:
        conn = connection_func()
        print(f"Successfully connected to the {name} database.")
        return conn
    except Exception as e:
        print(f"Failed to connect to the {name} database: {e}")
        return None
def close_connection(conn, name):
    if conn:
        conn.close()
        print(f"Closed the connection to the {name} database.")
if __name__ == "__main__":
    online_conn = connect_and_print_status(online_connection, "online")
    local_conn = connect_and_print_status(local_connection, "local")
    default_conn = connect_and_print_status(mysql_connection, "default")
    close_connection(online_conn, "online")
    close_connection(local_conn, "local")
    close_connection(default_conn, "default")