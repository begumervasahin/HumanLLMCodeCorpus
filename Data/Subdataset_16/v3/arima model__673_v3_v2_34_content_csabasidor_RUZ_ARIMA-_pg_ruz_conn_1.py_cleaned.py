import pandas as pd
import psycopg2 as pg
b1 = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
def fonk1(b4, db_params):
    b2 = None
    try:
        b2 = pg.connect(**db_params)
        print("Connected to the database!")
        b3 = pd.read_sql(b4, b2)
        return b3
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if b2 is not None:
            b2.close()
            print("Connection closed.")
def fonk2():
    b4 = "SELECT * FROM your_table_name"
    b3 = fonk1(b4, b1)
    if b3 is not None:
        print("Data fetched successfully:")
        print(b3.head())
    else:
        print("Failed to fetch data.")
if b5 = = "__main__":
    fonk2()