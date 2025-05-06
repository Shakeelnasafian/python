import random

computer = random.choice(['rock', 'paper', 'scissors'])
user = input("Enter your choice rock, paper, scissors? ")

print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif user == 'rock' and computer == 'scissors':
    print("Rock crushes scissors! You win!")
elif user == 'paper' and computer == 'rock':
    print("Paper covers rock! You win!")
elif user == 'scissors' and computer == 'paper':
    print("Scissors cut paper! You win!")
elif user == 'rock' and computer == 'paper':
    print("Paper covers rock! You lose!")
else:
    print("Scissors cut paper! You lose!")

