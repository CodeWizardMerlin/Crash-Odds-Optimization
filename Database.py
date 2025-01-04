import sqlite3

class Database:
    def __init__(self, db_name='data.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        table_create = "CREATE TABLE IF NOT EXISTS crash_data(crash_point REAL)"
        self.cursor.execute(table_create)
        self.connection.commit()

    def read_table(self):
        return self.cursor.execute("SELECT * FROM crash_data").fetchall()

    def insert_data(self, crash_point):
        self.cursor.execute("INSERT INTO crash_data (crash_point) VALUES (?)", (crash_point,))
        self.connection.commit()

    def close(self):
        self.connection.close()