import sqlite3

class Database_Handler():
    def __init__(self, file,table_name):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        self.table_name=table_name

    def create_table(self, fields):
        # Dynamically create the SQL query to create a table
        fields_query = ", ".join(fields)
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({fields_query});"
        self.cursor.execute(query)
        self.connection.commit()
    
    def insert_data(self, data):
        for product in data:
            self.cursor.execute('''INSERT INTO products (Product_SKU, Product_Name, Brand, Quantity) 
                            VALUES (?, ?, ?, ?)''', 
                            (product["Product SKU"], 
                            product["Product Name"], 
                            product["Brand"], 
                            product["Quantity"]))
        print("Data inserted successfully!")

    def insert_value(self, data):
        # Prepare placeholders for the number of fields
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {self.table_name} VALUES ({placeholders});"
        self.cursor.execute(query, data)
        self.connection.commit()

    def fetch_all(self):
        query = f"SELECT * FROM {self.table_name};"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def update_value(self, product_sku, field, new_value):
        query = f"UPDATE {self.table_name} SET {field} = ? WHERE Product_SKU = ?;"
        self.cursor.execute(query, (new_value, product_sku))
        self.connection.commit()

    def delete_value(self, product_sku):
        query = f"DELETE FROM {self.table_name} WHERE Product_SKU = ?;"
        self.cursor.execute(query, (product_sku,))
        self.connection.commit()

    def sort_products(self, sort_by, ascending=True):
        order = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM {self.table_name} ORDER BY {sort_by} {order};"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_products(self, search_value):
        query = f"SELECT * FROM {self.table_name} WHERE Product_Name LIKE ?;"
        self.cursor.execute(query, (f"%{search_value}%",))
        return self.cursor.fetchall()

    def total_number_of_products(self):
        query = f"SELECT COUNT(*) FROM {self.table_name};"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def close_connection(self):
        self.connection.close()