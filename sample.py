import sqlite3

class SqliteManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute_query(self, query, data: tuple = None):
        if data != None:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

if __name__ == "__main__":
    db_manager = SqliteManager('tutorial.db')
    # table_name = 'Persons'
    insert_data = ("Mate",)
    db_manager.connect()

    # Example queries

    db_manager.execute_query('INSERT INTO Persons(name) VALUES(?)', insert_data)


    data = db_manager.fetch_data('SELECT * FROM Persons')
    print("Persons:", data)

    db_manager.close()