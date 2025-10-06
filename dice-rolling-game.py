#ask user for yes or n
#read input
#treat input
#positive: roll dice + display + repeat step 1
#negative: repeat step 1
import random

counter = 0

def rolldice():
    return random.randint(1,6)

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "n":
        print("kthxbye")
        print(f"Total rolls: {counter}")
        break
    elif choice == "y":
        qtd = int(input("How many dice do you want to roll?: "))
        counter += qtd
        numbers = [rolldice() for _ in range(0,qtd)]
        print(f"Rolling the dice... {numbers}")
        print(f"Total rolls: {counter}")
    else:
        print("Invalid input. Please try again.")