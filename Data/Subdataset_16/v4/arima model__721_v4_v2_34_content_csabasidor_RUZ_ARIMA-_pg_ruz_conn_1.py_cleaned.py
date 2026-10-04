import pandas as pd
import psycopg2 as pg
b1 = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
def fonk1(params):
    try:
        b2 = pg.connect(**params)
        print("Connected to the database!")
        return b2
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
def fonk2(connection, b4):
    try:
        b3 = pd.read_sql(b4, connection)
        return b3
    except Exception as e:
        print(f"Error executing b4: {e}")
        return None
def fonk3():
    b2 = fonk1(b1)
    if b2:
        b4 = "SELECT * FROM your_table_name"
        b3 = fonk2(b2, b4)
        if b3 is not None:
            print(b3.head())
        b2.close()
        print("Connection closed.")
if b5 = = "__main__":
    fonk3()