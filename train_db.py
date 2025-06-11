import sqlite3 as sql

def create_tables():
    with sql.connect("train.db") as con:
        c = con.cursor()
        
        # Create users table
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        
        # Create trains table with a cost column
        c.execute('''
            CREATE TABLE IF NOT EXISTS trains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                train_number TEXT UNIQUE NOT NULL,
                train_name TEXT NOT NULL,
                departure_station TEXT NOT NULL,
                arrival_station TEXT NOT NULL,
                departure_time TEXT NOT NULL,
                arrival_time TEXT NOT NULL,
                cost REAL NOT NULL  -- Added cost column
            )
        ''')
        
        # Create bookings table
        c.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                train_id INTEGER NOT NULL,
                booking_date TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
                FOREIGN KEY (train_id) REFERENCES trains (id) ON DELETE CASCADE,
                -- Adding indexes to improve query performance
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (train_id) REFERENCES trains(id)
            )
        ''')
        
        # Create cancellations table
        c.execute('''
            CREATE TABLE IF NOT EXISTS cancellations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_id INTEGER NOT NULL,
                cancel_reason TEXT NOT NULL,
                cancel_date TEXT NOT NULL,
                FOREIGN KEY (booking_id) REFERENCES bookings (id) ON DELETE CASCADE
            )
        ''')
        
        con.commit()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")



