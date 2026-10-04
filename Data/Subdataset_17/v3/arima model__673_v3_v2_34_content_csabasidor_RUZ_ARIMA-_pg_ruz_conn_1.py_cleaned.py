import pandas as pd
import psycopg2 as pg
DB_PARAMS = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
def fetch_data(query, db_params):
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
def main():
    query = "SELECT * FROM your_table_name"
    df = fetch_data(query, DB_PARAMS)
    if df is not None:
        print("Data fetched successfully:")
        print(df.head())
    else:
        print("Failed to fetch data.")
if __name__ == "__main__":
    main()