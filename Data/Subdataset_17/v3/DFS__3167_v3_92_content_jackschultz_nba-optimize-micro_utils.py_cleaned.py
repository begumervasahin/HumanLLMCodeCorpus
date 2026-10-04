
import pymysql.cursors
def create_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        db='test_db',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
def get_cursor():
    connection = create_connection()
    return connection.cursor()