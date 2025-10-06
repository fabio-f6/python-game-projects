import random

def random_number(low, high):
    return random.randint(low, high)

def best_attempts(f_bestattempts, f_attempts):
    if f_bestattempts == 0:
        return f_attempts
    elif attempts < f_bestattempts:
        return f_attempts
    else:
        return f_bestattempts

bestAttempts = 0

while True:
    minimum_value = int(input("Minimum value: "))
    maximum_value = int(input("Maximum value: "))
    answer = random_number(minimum_value, maximum_value)
    print(f"DEBUG: {answer}")
    attemptsLeft = 2
    attempts = 0
    while True and attemptsLeft > 0:
        try:
            choice = int(input(f"Guess a number between {minimum_value} and {maximum_value}: "))
            if choice == answer:
                attempts+=1
                bestAttempts = best_attempts(bestAttempts, attempts)
                print(f"Correct! You guessed the number is {attempts} attempts. Your best game was {bestAttempts} attempts.")
                break
            elif choice > answer:
                attemptsLeft-=1
                attempts+=1
                print(f"Too high! {attemptsLeft} attempts remaining.")
            else:
                attemptsLeft -= 1
                attempts+=1
                print(f"Too low! {attemptsLeft} attempts remaining.")
        except ValueError:
            print("Please enter a number.")
    if attemptsLeft == 0:
        print(f"Game Over! The answer was {answer}.")
    answer = input("Play again? (y/n): ").lower()
    if answer == "n":
        break