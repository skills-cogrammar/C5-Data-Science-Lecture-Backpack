import sqlite3

conn = sqlite3.connect('resources/store.db')

with open('data/database_scripts.sql', 'r') as f:
    conn.cursor().executescript(f.read())


with open('data/product.sql', 'r') as f:
    conn.cursor().executescript(f.read())

