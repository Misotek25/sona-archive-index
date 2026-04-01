import sqlite3

class Indexer:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY,
            data TEXT NOT NULL
        )''')
        self.conn.commit()

    def insert_record(self, data):
        self.cursor.execute('INSERT INTO records (data) VALUES (?)', (data,))
        self.conn.commit()

    def search(self, query):
        self.cursor.execute('SELECT * FROM records WHERE data LIKE ?', ('%'+query+'%',))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == '__main__':
    indexer = Indexer('example.db')
    indexer.insert_record('This is a sample record.')
    results = indexer.search('sample')
    print('Search Results:', results)
    indexer.close()