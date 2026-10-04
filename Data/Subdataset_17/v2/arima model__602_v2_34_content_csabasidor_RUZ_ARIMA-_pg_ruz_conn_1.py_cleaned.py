import pandas as pd
import psycopg2 as pg
db_params = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
try:
    conn = pg.connect(**db_params)
    print("Connected to the database!")
    query = "SELECT * FROM your_table_name"
    df = pd.read_sql(query, conn)
    print(df.head())
except Exception as e:
    print(f"Error: {e}")
finally:
    if conn is not None:
        conn.close()
        print("Connection closed.")