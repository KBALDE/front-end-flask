import sqlite3

conn= sqlite3.connect("books.sqlite")

cursor = conn.cursor()

sql_command = """ CREATE TABLE books(
    id INTEGER PRIMARY KEY,
    authors VARCHAR(50),
    country VARCHAR(50),
    language VARCHAR(50)
);"""
cursor.execute(sql_command)
