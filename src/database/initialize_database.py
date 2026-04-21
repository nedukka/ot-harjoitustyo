from src.database.database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS tasks''')
    cursor.execute('''DROP TABLE IF EXISTS users''')
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            task_type TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            week_created INTEGER,
            last_completed_week INTEGER
        );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == '__main__':
    initialize_database()
