from expense_tracker.models.expense import add_expense, get_all_expenses
from expense_tracker.analysis.visualizer import show_graph

def run_cli():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Show Graph\n4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            name = input("Name: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            desc = input("Description: ")
            add_expense(name, amount, category, date, desc)
        elif choice == '2':
            expenses = get_all_expenses()
            for exp in expenses:
                print(exp)
        elif choice == '3':
            show_graph()
        elif choice == '4':
            break