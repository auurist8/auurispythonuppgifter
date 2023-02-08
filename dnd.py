import random

for number in range(0, 10):
    print(random.randint(30, 50))

for number in range(0, 5):
    print(round(random.uniform(1, 10)))

for number in range(0, 7):
    print(random.gauss(50, 25))

numbers = (1, 2, 3, 5, 10)
times = 2
print(random.sample(numbers, times))

for number in range(100):
    if number == 51:
        break
    print(str(number))

    try:
        A = int(input("input int"))
        B = (input("input str"))

        print(A + B)

    except:
        print("you can not add an interger and a string")

    try:
        C = int(input("input int"))
        D = int(input("input str"))
        E = C / D
        print(E)

    except ZeroDivisionError:
        print("you can not divide a number by zero")

import fileinput

file = open("song.txt", "r")
song = file.read()
print(song)

f = open("gg", "a")
f.write("w")
f.close()
f = open("C:\users\Auuris\desktop\song.txt", "w")

f = open("gg", "r")
print(f.read())

for line in fileinput.input(files = 'gg'):
    print(line)
