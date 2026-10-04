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
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None
def fonk2(b2, b5):
    try:
        b3 = pd.read_sql(b5, b2)
        return b3
    except Exception as error:
        print(f"Error executing b5: {error}")
        return None
def fonk3(b2):
    try:
        if b2 is not None:
            b2.close()
            print("Connection closed.")
    except Exception as error:
        print(f"Error closing the b2: {error}")
if b4 = = "__main__":
    b2 = fonk1(b1)
    if b2:
        try:
            b5 = "SELECT * FROM your_table_name"
            b6 = fonk2(b2, b5)
            if b6 is not None:
                print(b6.head())
        finally:
            fonk3(b2)