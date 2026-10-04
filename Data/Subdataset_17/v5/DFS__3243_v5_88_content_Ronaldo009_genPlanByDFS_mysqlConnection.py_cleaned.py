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
def get_online_connection():
    return create_connection(
        host='192.168.100.253',
        port=3306,
        user='unireader',
        password='7LWFu(RMYHKb>dWvM6gEE(GKFWwhL',
        db='uniqueway_production'
    )
def get_local_connection():
    return create_connection(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='uniqueway_development'
    )
def get_mysql_connection():
    return get_local_connection()
def print_connection_status(conn, name):
    if conn:
        print(f"Successfully connected to the {name} database.")
    else:
        print(f"Failed to connect to the {name} database.")
def close_connection(conn, name):
    if conn:
        conn.close()
        print(f"Closed the connection to the {name} database.")
if __name__ == "__main__":
    online_conn = get_online_connection()
    print_connection_status(online_conn, "online")
    local_conn = get_local_connection()
    print_connection_status(local_conn, "local")
    default_conn = get_mysql_connection()
    print_connection_status(default_conn, "default")
    close_connection(online_conn, "online")
    close_connection(local_conn, "local")
    close_connection(default_conn, "default")