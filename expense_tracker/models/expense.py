from expense_tracker.storage.database import insert_expense, fetch_all_expenses

class Expense:
    def __init__(self, name, amount, category, date, description):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __repr__(self):
        return f"{self.name} | {self.amount} | {self.category} | {self.date} | {self.description}"

def add_expense(name, amount, category, date, description):
    exp = Expense(name, amount, category, date, description)
    insert_expense(exp)

def get_all_expenses():
    rows = fetch_all_expenses()
    return [Expense(row[1], row[2], row[3], row[4], row[5]) for row in rows]