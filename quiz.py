import csv
import os
from random import *
from platform import platform


def checkos():
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

        questions_array.remove(questions_array[randvalue])
        answers_array.remove(answers_array[randvalue])
        checkos()
    return corr


questions_array = []
answers_array = []

openquestionsfile()
openanswersfile()

correct = 0
result = quizgame(correct)
