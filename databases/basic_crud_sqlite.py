import sqlite3

conn = sqlite3.connect('databases/sql1')
cur  = conn.cursor()

# cur.execute(' ') to execute query

entries = cur.execute('SELECT * FROM users where name = "sakthi"' )

for row in entries:
    print(row[0])

# conn.commit()

# cur.close()