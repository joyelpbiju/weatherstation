import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    # Create a table for weather data
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 city TEXT,
                 temperature REAL,
                 humidity REAL,
                 wind_speed REAL,
                 description TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
               )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
