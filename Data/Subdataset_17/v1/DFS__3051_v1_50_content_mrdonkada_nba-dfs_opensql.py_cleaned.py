import MySQLdb
def main():
    sqlfile = 'sql/consistency.sql'
    with open(sqlfile, 'r') as file:
        query = file.read().replace('\n', ' ')
    print(query)
    con = MySQLdb.connect(host='localhost', user='root', passwd='', db='dfs-nba')
    try:
        with con.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        con.close()
if __name__ == "__main__":
    main()