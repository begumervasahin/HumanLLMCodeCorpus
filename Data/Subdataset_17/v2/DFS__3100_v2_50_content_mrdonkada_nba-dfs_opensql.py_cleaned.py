import MySQLdb
def read_sql_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().replace('\n', ' ')
def execute_query(query):
    con = MySQLdb.connect(host='localhost', user='root', passwd='', db='dfs-nba')
    try:
        with con.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        con.close()
def main():
    sqlfile = 'sql/consistency.sql'
    query = read_sql_file(sqlfile)
    print(query)
    execute_query(query)
if __name__ == "__main__":
    main()