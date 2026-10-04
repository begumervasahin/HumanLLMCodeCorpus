import sqlite3
class DBTable:
    DB_NAME = "commodity_prices.db"
    def __init__(self, name, schema):
        if not name:
            raise RuntimeError("Invalid table name")
        if not schema:
            raise RuntimeError("Invalid database schema")
        self.name = name
        self.schema = schema
        self.db_conn = sqlite3.connect(self.DB_NAME)
        self.create_table()
    def create_table(self):
        columns_query_string = ', '.join([f"{k} {v}" for k, v in self.schema.items()])
        self.db_conn.execute(f"CREATE TABLE IF NOT EXISTS {self.name} ({columns_query_string})")
        self.db_conn.commit()
    def select(self, columns=None, where=None):
        if columns is None:
            columns = list(self.schema.keys())
        columns_query_string = ", ".join(columns)
        query = f"SELECT {columns_query_string} FROM {self.name}"
        if where:
            where_query_string = " AND ".join([f"{k} = '{v}'" for k, v in where.items()])
            query += f" WHERE {where_query_string}"
        result = []
        for row in self.db_conn.execute(query):
            result.append(dict(zip(columns, row)))
        return result
    def insert(self, item):
        columns_query = ", ".join(item.keys())
        values_query = ", ".join([f"'{v}'" for v in item.values()])
        cursor = self.db_conn.cursor()
        cursor.execute(f"INSERT OR IGNORE INTO {self.name} ({columns_query}) VALUES ({values_query})")
        self.db_conn.commit()
        return cursor.lastrowid
    def update(self, values, where):
        set_query = ", ".join([f"{k} = '{v}'" for k, v in values.items()])
        where_query = " AND ".join([f"{k} = '{v}'" for k, v in where.items()])
        cursor = self.db_conn.cursor()
        cursor.execute(f"UPDATE {self.name} SET {set_query} WHERE {where_query}")
        self.db_conn.commit()
        return cursor.rowcount
    def select_prices_between_dates(self, start_date, end_date, commodity_type):
        sql = f"SELECT Date, {commodity_type} FROM Prices WHERE Date BETWEEN '{start_date}' AND '{end_date}'"
        results = []
        for result in self.db_conn.execute(sql):
            results.append(result)
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