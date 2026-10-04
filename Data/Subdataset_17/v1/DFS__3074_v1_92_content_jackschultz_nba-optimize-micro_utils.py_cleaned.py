
import pymysql.cursors
def get_cursor():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        db='test_db',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection.cursor()