import random

roll = random.randint(1, 6)
guess = int(input("Guess the number on the dice (1-6): "))

if guess == roll:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {roll}. Better luck next time!")