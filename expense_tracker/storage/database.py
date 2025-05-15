import sqlite3
import os

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

conn = sqlite3.connect('data/expenses.db')
cursor = conn.cursor()

def create_table(): 
    cursor.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, name TEXT, amount REAL, category TEXT, date TEXT, description TEXT)")
    conn.commit()

def insert_expense(expense):
    cursor.execute("INSERT INTO expenses (name, amount, category, date, description) VALUES (?, ?, ?, ?, ?)", (expense.name, expense.amount, expense.category, expense.date, expense.description))
    conn.commit()

def fetch_all_expenses():
    cursor.execute("SELECT * FROM expenses")
    return cursor.fetchall()

