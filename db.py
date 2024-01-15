import sqlite3

class SQLHandler:
    
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables() 

    def create_tables(self):
        self.execute_query(""" CREATE TABLE IF NOT EXISTS Classes (
                        pk TEXT PRIMARY KEY,
                        class_name TEXT, 
                        category_list TEXT,
                        weight_list TEXT)
                        """
                        )
    #this executes the operation we want on our database
    def execute_query(self, query, params = None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        self.connection.commit()

    def insert_class(self, class_name, category_list, weight_list):
        self.execute_query("INSERT INTO Classes (class_name, category_list, weight_list) VALUES (?, ?, ?)", (class_name, category_list, weight_list))
        return self.cursor.lastrowid

    def close_connection(self):
        self.conection.close()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()