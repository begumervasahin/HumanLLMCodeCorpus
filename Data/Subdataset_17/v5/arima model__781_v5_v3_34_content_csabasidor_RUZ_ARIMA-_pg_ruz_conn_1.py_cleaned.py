import pandas as pd
import psycopg2 as pg
DB_PARAMS = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
def connect_to_database(params):
    try:
        connection = pg.connect(**params)
        print("Connected to the database!")
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None
def execute_query(connection, query):
    try:
        data_frame = pd.read_sql(query, connection)
        return data_frame
    except Exception as error:
        print(f"Error executing query: {error}")
        return None
def close_connection(connection):
    try:
        if connection is not None:
            connection.close()
            print("Connection closed.")
    except Exception as error:
        print(f"Error closing the connection: {error}")
def main():
    connection = connect_to_database(DB_PARAMS)
    if connection:
        try:
            query = "SELECT * FROM your_table_name"
            result_df = execute_query(connection, query)
            if result_df is not None:
                print(result_df.head())
        finally:
            close_connection(connection)
if __name__ == "__main__":
    main()