import sqlite3
# storing to sqlite
def sqlCon(data):
    
    ''' connecting to the sqlite'''
    conn = sqlite3.connect("theverge.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                    (id INTEGER PRIMARY KEY,
                    headline TEXT,
                    url TEXT,
                    author TEXT,
                    date TEXT)''')

    for i, row in enumerate(data):
        cursor.execute("INSERT INTO articles (id, headline,  url,  author, date) VALUES (?, ?, ?, ?, ?)",
                    (i+1, row[0], row[1], row[2], row[3]))