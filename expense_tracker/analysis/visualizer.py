import matplotlib.pyplot as plt

def plot_by_category(expenses):
    from collections import defaultdict
    data =  defaultdict(float)
    for exp in expenses:
        data[exp.category] += exp.amount
    plt.bar(data.keys(), data.values())
    plt.title('Expenses by Category')
    plt.show()
