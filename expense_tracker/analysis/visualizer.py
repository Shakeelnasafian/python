import matplotlib.pyplot as plt
from expense_tracker.models.expense import Expense

def plot_by_category(expenses):
    from collections import defaultdict
    data =  defaultdict(float)
    for exp in expenses:
        data[exp.category] += exp.amount
    plt.bar(data.keys(), data.values())
    plt.title('Expenses by Category')
    plt.show()


def show_graph():
    expenses = Expense.get_all_expenses()
    plot_by_category(expenses)