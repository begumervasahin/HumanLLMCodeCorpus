
import pymysql.cursors
def fonk1():
    return pymysql.connect(
        b1 = 'localhost',
        b2 = 'root',
        b3 = 'b3',
        b4 = 'test_db',
        b5 = 'utf8',
        b6 = pymysql.cursors.DictCursor
    )
def fonk2():
    b7 = fonk1()
    return b7.cursor()