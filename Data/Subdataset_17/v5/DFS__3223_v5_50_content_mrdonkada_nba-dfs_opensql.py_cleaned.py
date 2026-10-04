import MySQLdb
def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().replace('\n', ' ')
def execute_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
def main():
    sql_file_path = 'sql/consistency.sql'
    query = read_sql_file(sql_file_path)
    print("Executing query:")
    print(query)
    connection = MySQLdb.connect(host='localhost', user='root', passwd='', db='dfs-nba')
    try:
        execute_query(connection, query)
    finally:
        connection.close()
if __name__ == "__main__":
    main()