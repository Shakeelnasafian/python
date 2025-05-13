import matplotlib.pyplot as plt

def plot_by_category(expenses):
    from collections import defaultdict
    data =  defaultdict(float)
    for exp in expenses:
        data[exp.category] += exp.amount
    plt.bar(data.keys(), data.values())
    plt.title('Expenses by Category')
    plt.show()

if __name__ == "__main__":
    # quick demo data
    from models.expense import Expense
    demo_expenses = [
        Expense(amount=10.0, category="Food", date="2025-05-13"),
        Expense(amount=25.0, category="Transport", date="2025-05-13"),
        Expense(amount=15.0, category="Food", date="2025-05-13"),
    ]
    plot_by_category(demo_expenses)