#loop
#generate number
#ask user for input
#compare input to generated number

import random

def random_number():
    return random.randint(1, 100)

attempts = 10

while True:
    answer = random_number()
    minimum_value = int(input("Minimum value: "))
    maximum_value = int(input("Maximum value: "))
    while True and attempts > 0:
        try:
            choice = int(input(f"Guess a number between {minimum_value} and {maximum_value}: "))
            if choice == answer:
                print("Correct!")
                break
            elif choice > answer:
                attempts-=1
                print(f"Too high! {attempts} attempts remaining.")
            elif choice < answer:
                print(f"Too low! {attempts} attempts remaining.")
                attempts-=1
        except ValueError:
            print("Please enter a number.")
    answer = input("Play again? (y/n): ")
    if answer == "n":
        break