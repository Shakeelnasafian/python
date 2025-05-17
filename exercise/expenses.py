total = 0
expenses = []

num_expenses = int(input("How many expenses do you have? "))
for i in range(num_expenses):
    expense = float(input("Enter your expense: "))
    expenses.append(expense)

# sum = 0

# for expense in expenses:
#     sum = sum + expense

total = sum(expenses)

print("Total expenses: $", total, sep='')