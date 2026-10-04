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
        connection = pg.connect(**params)
        print("Connected to the database!")
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None
def fetch_data_from_db(query, connection):
    try:
        df = pd.read_sql(query, connection)
        return df
    except Exception as error:
        print(f"Error executing query: {error}")
        return None
def main():
    query = "SELECT * FROM your_table_name"
    connection = connect_to_db(db_params)
    if connection is not None:
        df = fetch_data_from_db(query, connection)
        connection.close()
        print("Connection closed.")
        if df is not None:
            print(df.head())
        else:
            print("No data fetched.")
    else:
        print("Failed to connect to the database.")
if __name__ == "__main__":
    main()