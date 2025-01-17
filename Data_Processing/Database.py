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

    def print_table(self):
        print(self.cursor.execute("SELECT * FROM crash_data").fetchall())

    def get_all_data(self):
        self.cursor.execute("SELECT crash_point FROM crash_data")
        data = self.cursor.fetchall()
        return [row[0] for row in data]

    def insert_data(self, crash_point: float):
        self.cursor.execute("INSERT INTO crash_data (crash_point) VALUES (?)", (crash_point,))
        self.connection.commit()

    def clear_table(self):
        self.cursor.execute("DELETE FROM crash_data")
        self.connection.commit()

    def process_file(self):
        with open("Raw data.txt") as file:
            raw_data = file.read()
            data_values = raw_data.split()
            for value in data_values:
                crash_point = float(value)
                self.insert_data(crash_point)
        open('file.txt', 'w').close() # clear the file after processing
                
    def add_from_file_without_clearing(self):
        with open("Raw data.txt") as file:
            raw_data = file.read()
            data_values = raw_data.split()
            for value in data_values:
                crash_point = float(value)
                self.insert_data(crash_point)

    def table_size(self):
        size = self.cursor.execute("SELECT COUNT(*) FROM crash_data").fetchone()[0]
        return size
    
    def close(self):
        self.connection.close()