import json

def save_expenses(expenses, file_path):
    with open(file_path, 'w') as file:
        json.dump([e.to_dict() for e in expenses], file, indent=4)

def load_expenses(file_path):
    from models.expense import Expense
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Expense(**item) for item in data]