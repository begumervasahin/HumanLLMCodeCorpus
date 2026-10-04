import MySQLdb
def fonk1():
    b1 = 'sql/consistency.sql'
    with open(b1, 'r') as file:
        b2 = file.read().replace('\n', ' ')
    print(b2)
    b3 = MySQLdb.connect(host='localhost', user='root', passwd='', db='dfs-nba')
    try:
        with b3.cursor() as cursor:
            cursor.execute(b2)
            b4 = cursor.fetchall()
            for row in b4:
                print(row)
    finally:
        b3.close()
if b5 = = "__main__":
    fonk1()