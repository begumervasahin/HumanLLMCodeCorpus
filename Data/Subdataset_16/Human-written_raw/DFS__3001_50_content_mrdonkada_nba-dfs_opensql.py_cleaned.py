import MySQLdb
b1 = 'sql/consistency.sql'
with open(b1) as f:
    b2 = f.read()
    b3 = b2.replace('\n',' ')
    print b3
b4 = MySQLdb.connect('localhost', 'root', '', 'dfs-nba')
with b4:
    b5 = b4.cursor()
    b5.execute(b3)
    b6 = b5.fetchall()
    for row in b6:
        print row