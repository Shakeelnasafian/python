money_owed = float(input("How much money do you owe?\n "))
apr = float(input("What is the annual percentage rate (APR)?\n "))
payment = float(input("What is your monthly payment?\n "))
months = int(input("How many months do you want to calculate?\n "))

monthly_rate = apr / 100 / 12

for i in range(months):
    interest_paid =  money_owed * monthly_rate

    money_owed = money_owed + interest_paid

    if money_owed - payment < 0:
        print("You paid too much!")
        print("Paid", payment, 'of which', interest_paid, 'was interest.', end='  ')
        break
    
    money_owed = money_owed - payment

    print("Paid", payment, 'of which', interest_paid, 'was interest.', end='  ')
    print("Now i owe", money_owed, "after", months, "months.")