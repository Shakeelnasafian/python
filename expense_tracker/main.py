from models.expense import Expense
from analysis.visualizer import plot_by_category

def load_demo():
    return [
        Expense(amount=10.0, category="Food",      date="2025-05-13"),
        Expense(amount=25.0, category="Transport", date="2025-05-13"),
        Expense(amount=15.0, category="Food",      date="2025-05-13"),
    ]

def main():
    expenses = load_demo()
    plot_by_category(expenses)

if __name__ == "__main__":
    main()