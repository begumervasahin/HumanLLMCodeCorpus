import pandas as pd
import psycopg2 as pg
db_params = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
def connect_to_db(params):
    try:
        conn = pg.connect(**params)
        print("Connected to the database!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
def execute_query(connection, query):
    try:
        df = pd.read_sql(query, connection)
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
def main():
    conn = connect_to_db(db_params)
    if conn:
        query = "SELECT * FROM your_table_name"
        df = execute_query(conn, query)
        if df is not None:
            print(df.head())
        conn.close()
        print("Connection closed.")
if __name__ == "__main__":
    main()