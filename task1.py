import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE data  (timestamp TEXT, player_id TEXT, event_id TEXT, error_id TEXT, json_server TEXT, json_client TEXT)''')

conn.commit()
conn.close()
