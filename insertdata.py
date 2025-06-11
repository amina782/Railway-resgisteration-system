import sqlite3 as sql

def insert_sample_data():
    with sql.connect("train.db") as con:
        c = con.cursor()
        # Insert sample trains data
        sample_trains = [
            ('12345', 'Express Train', 'Station A', 'Station B', '08:00', '12:00'),
            ('67890', 'Fast Train', 'Station C', 'Station D', '09:00', '13:00')
        ]
        c.executemany('''
            INSERT OR IGNORE INTO trains (train_number, train_name, departure_station, arrival_station, departure_time, arrival_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', sample_trains)
        con.commit()

        # Confirm the data was inserted by querying the database
        c.execute('SELECT * FROM trains')
        trains = c.fetchall()
        print("Trains in database after insertion:")
        for train in trains:
            print(train)

if __name__ == "__main__":
    insert_sample_data()

