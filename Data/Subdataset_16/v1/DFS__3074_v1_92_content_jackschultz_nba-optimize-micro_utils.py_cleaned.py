
import pymysql.cursors
def fonk1():
    b1 = pymysql.connect(
        b2 = 'localhost',
        b3 = 'root',
        b4 = 'b4',
        b5 = 'test_db',
        b6 = 'utf8',
        b7 = pymysql.cursors.DictCursor
    )
    return b1.cursor()