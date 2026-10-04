import sqlite3
class DBTable:
    DB_NAME = "commodity_prices.db"
    def __init__(self, name, schema):
        if not name:
            raise ValueError("Invalid table name")
        if not schema:
            raise ValueError("Invalid database schema")
        self.name = name
        self.schema = schema
        self.db_conn = sqlite3.connect(self.DB_NAME)
        self.create_table()
    def create_table(self):
        columns_query = ', '.join([f"{col_name} {col_type}" for col_name, col_type in self.schema.items()])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.name} ({columns_query})"
        self.db_conn.execute(create_table_query)
        self.db_conn.commit()
    def select(self, columns=None, where=None):
        if columns is None:
            columns = list(self.schema.keys())
        columns_query = ", ".join(columns)
        query = f"SELECT {columns_query} FROM {self.name}"
        if where:
            where_query = " AND ".join([f"{col} = '{val}'" for col, val in where.items()])
            query += f" WHERE {where_query}"
        results = [dict(zip(columns, row)) for row in self.db_conn.execute(query)]
        return results
    def insert(self, item):
        columns_query = ", ".join(item.keys())
        values_query = ", ".join([f"'{val}'" for val in item.values()])
        insert_query = f"INSERT OR IGNORE INTO {self.name} ({columns_query}) VALUES ({values_query})"
        cursor = self.db_conn.cursor()
        cursor.execute(insert_query)
        self.db_conn.commit()
        return cursor.lastrowid
    def update(self, values, where):
        set_query = ", ".join([f"{col} = '{val}'" for col, val in values.items()])
        where_query = " AND ".join([f"{col} = '{val}'" for col, val in where.items()])
        update_query = f"UPDATE {self.name} SET {set_query} WHERE {where_query}"
        cursor = self.db_conn.cursor()
        cursor.execute(update_query)
        self.db_conn.commit()
        return cursor.rowcount
    def select_prices_between_dates(self, start_date, end_date, commodity_type):
        query = f
        results = [row for row in self.db_conn.execute(query)]
        return results
    def close(self):
        self.db_conn.close()
schema = {
    'Date': 'TEXT',
    'Commodity': 'TEXT',
    'Price': 'REAL'
}
prices_table = DBTable('Prices', schema)
prices_table.insert({'Date': '2024-07-22', 'Commodity': 'Gold', 'Price': 1800.0})
print(prices_table.select())
prices_table.update({'Price': 1850.0}, {'Date': '2024-07-22', 'Commodity': 'Gold'})
print(prices_table.select_prices_between_dates('2024-07-20', '2024-07-23', 'Gold'))
prices_table.close()