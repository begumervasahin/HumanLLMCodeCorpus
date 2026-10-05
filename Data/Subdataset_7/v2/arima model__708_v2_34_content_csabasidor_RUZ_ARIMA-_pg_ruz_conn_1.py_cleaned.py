import pandas as pd
import psycopg2 as pg
b1 = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
try:
    b2 = pg.connect(**b1)
    print("Connected to the database!")
    b3 = "SELECT * FROM your_table_name"
    b4 = pd.read_sql(b3, b2)
    print(b4.head())
except Exception as e:
    print(f"Error: {e}")
finally:
    if b2 is not None:
        b2.close()
        print("Connection closed.")