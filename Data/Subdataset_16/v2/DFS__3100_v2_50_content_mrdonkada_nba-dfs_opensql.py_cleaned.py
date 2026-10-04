import MySQLdb
def fonk1(filepath):
    with open(filepath, 'r') as file:
        return file.read().replace('\n', ' ')
def fonk2(b4):
    b1 = MySQLdb.connect(host='localhost', user='root', passwd='', db='dfs-nba')
    try:
        with b1.cursor() as cursor:
            cursor.execute(b4)
            b2 = cursor.fetchall()
            for row in b2:
                print(row)
    finally:
        b1.close()
def fonk3():
    b3 = 'sql/consistency.sql'
    b4 = fonk1(b3)
    print(b4)
    fonk2(b4)
if b5 = = "__main__":
    fonk3()