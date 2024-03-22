import csv
import os
from random import *
from platform import platform


def clearscreen():
    if platform() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def openquestionsfile():

    qfile = "questions.txt"

    try:
        with open(qfile, "r") as file:

            for line in file:

                questions_array.append(line)
    except FileNotFoundError:
        print("File not found!")


def openanswersfile():
    afile = "answers.csv"

    try:
        with open(afile, "r", newline="") as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                answers_array.append(row)
    except FileNotFoundError:
        print(f"File not found!")


def quizgame(corr):
    for questions in range(0, len(questions_array)):
        randvalue = randint(0, len(questions_array) - 1)
        print(questions_array[randvalue] + "\n")

        numbers = [1, 2, 3, 4]
        indices = list(range(len(numbers)))
        shuffle(indices)
        for i in indices:
            print(answers_array[randvalue][i])

        user_answer = str(input("\nYour answer: "))
        if user_answer.upper() == answers_array[randvalue][2]:
            corr += 1
        else:
            falsequestions.append(questions_array[randvalue])
            falseanswers.append(user_answer)
            correctanswers.append(answers_array[randvalue][2])

        questions_array.remove(questions_array[randvalue])
        answers_array.remove(answers_array[randvalue])
        clearscreen()
    return corr

def printfalseanswers(res):
    print("Questions you answered incorrectly: \n")
    for i in range(0,len(falsequestions)):
        print(str(i+1) + ". " + falsequestions[i])
        print("You answered: " + str(falseanswers[i]).upper())
        print("Correct Answer: " + correctanswers[i] + "\n")
    print(f"Total correct answers: {res}")
        
questions_array = []
answers_array = []

openquestionsfile()
openanswersfile()

falsequestions = []
falseanswers = []
correctanswers = []

correct = 0
result = quizgame(correct)

printfalseanswers(result)
