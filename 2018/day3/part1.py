#!/usr/bin/env python3

allGuesses = [line.rstrip('\n') for line in open('data.txt')]

def cleanGuess(rawGuess):
    rawGuessAsList = rawGuess.split(' ')
    cleanGuess = []
    cleanGuess.append(rawGuessAsList[0])
    distanceFromTopCorner = rawGuessAsList[2].replace(':','').split(',')
    cleanGuess.append((distanceFromTopCorner[0], distanceFromTopCorner[1]))
    size = rawGuessAsList[3].split('x')
    cleanGuess.append((size[0], size[1]))
    return cleanGuess

cleanGuesses = [cleanGuess(rawGuess) for rawGuess in allGuesses]

width = 1000
height = 1000

global fabric, counter
fabric = ["-"] * 1000000
counter = 0

def fillCoordinate(x, y):
    global fabric, counter
    coordinate = x + ((y - 1) * 999)
    if fabric[coordinate] == "-":
        fabric[coordinate] = "*"
    elif fabric[coordinate] == "*":
        fabric[coordinate] = "x"
        counter += 1


def fillFabric(guess):
    xmin = int(guess[1][0]) + 1
    xmax = xmin + int(guess[2][0])
    ymin = int(guess[1][1]) + 1
    ymax = ymin + int(guess[2][1])

    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            fillCoordinate(x, y)

for guess in cleanGuesses:
    fillFabric(guess)

print("Counter: {}".format(counter))
