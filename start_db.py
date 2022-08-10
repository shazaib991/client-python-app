import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False) # permanent database
cursor = conn.cursor()
#This script only to be run once to initialize (create) the db.

cursor.executescript('''

    CREATE TABLE data (
    language json NOT NULL,
    device json NOT NULL, 
    browserName json NOT NULL, 
    browserDimentions json NOT NULL, 
    ipAddress json NOT NULL UNIQUE, 
    cookieStatus json NOT NULL,
    publicKey TEXT NOT NULL
    )
    ''');