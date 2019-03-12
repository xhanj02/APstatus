import sqlite3
conn = sqlite3.connect("hostnames.db")
c = conn.cursor()
db=c.execute("SELECT * FROM ips")
print(db.fetchall())