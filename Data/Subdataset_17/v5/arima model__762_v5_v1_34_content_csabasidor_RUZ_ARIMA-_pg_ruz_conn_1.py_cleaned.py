import pandas as pd
import psycopg2 as pg
def fetch_data_from_db(db_params, query):
    conn = None
    try:
        conn = pg.connect(**db_params)
        print("Connected to the database!")
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn is not None:
            conn.close()
            print("Connection closed.")
if __name__ == "__main__":
    db_params = {
        'dbname': 'datahub',
        'user': 'CONTACT SLOVAKIA.DIGITAL',
        'host': 'sql.ekosystem.slovensko.digital',
        'port': 5432,
        'password': 'CONTACT SLOVENSKO.DIGITAL'
    }
    query = "SELECT * FROM your_table_name"
    df = fetch_data_from_db(db_params, query)
    if df is not None:
        print(df.head())