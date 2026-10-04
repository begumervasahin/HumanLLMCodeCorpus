import pandas as pd
import psycopg2 as pg
def fonk1(b4, b5):
    b1 = None
    try:
        b1 = pg.connect(**b4)
        print("Connected to the database!")
        b2 = pd.read_sql(b5, b1)
        return b2
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if b1 is not None:
            b1.close()
            print("Connection closed.")
if b3 = = "__main__":
    b4 = {
        'dbname': 'datahub',
        'user': 'CONTACT SLOVAKIA.DIGITAL',
        'host': 'sql.ekosystem.slovensko.digital',
        'port': 5432,
        'password': 'CONTACT SLOVENSKO.DIGITAL'
    }
    b5 = "SELECT * FROM your_table_name"
    b2 = fonk1(b4, b5)
    if b2 is not None:
        print(b2.head())