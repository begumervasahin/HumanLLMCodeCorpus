import pandas as pd
import psycopg2 as pg
db_params = {
    'dbname': 'datahub',
    'user': 'CONTACT SLOVAKIA.DIGITAL',
    'host': 'sql.ekosystem.slovensko.digital',
    'port': 5432,
    'password': 'CONTACT SLOVENSKO.DIGITAL'
}
def connect_to_database(connection_params):
    try:
        connection = pg.connect(**connection_params)
        print("Connected to the database!")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
def execute_query(connection, query):
    try:
        data_frame = pd.read_sql(query, connection)
        return data_frame
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
def close_connection(connection):
    try:
        if connection is not None:
            connection.close()
            print("Connection closed.")
    except Exception as e:
        print(f"Error closing the connection: {e}")
if __name__ == "__main__":
    connection = connect_to_database(db_params)
    if connection:
        try:
            query = "SELECT * FROM your_table_name"
            result_df = execute_query(connection, query)
            print(result_df.head())
        finally:
            close_connection(connection)