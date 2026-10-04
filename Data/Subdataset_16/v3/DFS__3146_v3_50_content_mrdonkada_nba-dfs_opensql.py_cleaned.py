import MySQLdb
def fonk1(filepath):
    with open(filepath, 'r') as file:
        return file.read().replace('\n', ' ')
def fonk2(b4, b3):
    with b4.cursor() as cursor:
        cursor.execute(b3)
        b1 = cursor.fetchall()
        for row in b1:
            print(row)
def fonk3():
    b2 = 'sql/consistency.sql'
    b3 = fonk1(b2)
    print("Executing b3:")
    print(b3)
    b4 = MySQLdb.connect(host='localhost', user='root', passwd='', db='dfs-nba')
    try:
        fonk2(b4, b3)
    finally:
        b4.close()
if b5 = = "__main__":
    fonk3()