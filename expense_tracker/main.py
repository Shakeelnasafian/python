from ui.cli import main_menu
from models.expense import Expense
from storage.database import create_table, insert_expense, fetch_all_expenses
from analysis.visualizer import plot_by_category

def load_demo():
    return [
        Expense(amount=10.0, category="Food",      date="2025-05-13"),
        Expense(amount=25.0, category="Transport", date="2025-05-13"),
        Expense(amount=15.0, category="Food",      date="2025-05-13"),
    ]

def main():
    create_table()
    while True:
        main_menu()
        choice = input("Select an option:")
        if choice == '1':
            name = input("Expense name:")
            amount = float(input("Expense amount:"))
            category = input("Expense category:")
            date = input("Expense date (YYYY-MM-DD):")
            description = input("Expense description:")
            exp = Expense(name=name, amount=amount, category=category, date=date, description=description)
            insert_expense(exp)
        elif choice == '2':
            expense = fetch_all_expenses()
            for e in expense:
                print(e)
        elif choice == '3':
            expense_rows = fetch_all_expenses()
            expenses = [
                Expense(
                    name=row[1],
                    amount=row[2],
                    category=row[3],
                    date=row[4],
                    description=row[5]
                )
                for row in expense_rows
            ]
            plot_by_category(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()