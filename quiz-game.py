import random
from termcolor import colored

QUESTION = "question"
CHOICES = "choices"
ANSWER = "correct_answer"

correct_text = colored("Correct!\n", "green")
wrong_text = colored("Wrong!", "red")

def ask_question(index, question, choices):
    print(f'Question {index}: {question}')
    for choice in choices:
        print(choice)

    return input("Your answer: ").lower().strip()

def run_quiz(quiz_questions):
    user_score = 0
    random.shuffle(quiz_questions)

    for index, question in enumerate(quiz_questions, 1):
        answer = ask_question(index, question[QUESTION], question[CHOICES])

        if answer == question[ANSWER]:
            print(correct_text)
            user_score += 1
        else:
            print(wrong_text + f"The correct answer is {question[ANSWER]}.\n")

    print(f"Your final score is: {user_score} out of {len(quiz_questions)}.")

def main():
    quiz_questions = [
        {QUESTION: "What year is it?",
         CHOICES: ["a: 2010", "b: 2025", "c: 2015", "d: 2026"],
         ANSWER: "b"},
        {QUESTION: "Square root of 9?",
         CHOICES: ["a: 9", "b: 6", "c: 3", "d: 4.5"],
         ANSWER: "c"},
        {QUESTION: "Capital of Belgium?",
         CHOICES: ["a: Brussels", "b: Berlin", "c: Vienna", "d: Prague"],
         ANSWER: "a"} ]

    run_quiz(quiz_questions)

if __name__ == "__main__":
    main()