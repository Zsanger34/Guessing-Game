""" This code will output the option to pick a number interval and then with the number interval the computer will pick
a random number and the user will have to guess it. It will allow you to choose the difficulty with:
1 being easy and unlimited tries
2 being medium and 10 tries
3 being hard and 3 tries
game will continue until user runs out of tries or quits"""

import random
import time


def main():
    stop = 0
    while stop == 0:
        hold = input(
            "Welcome to the Guessing Game \n enter t for Diffuclty Meaning\n pick 1 to play easy\n 2 for medium\n 3 for hard\n press q to quit\n")
        if hold == '1':
            print('Player Selected Easy Mode')
            hold = ''
            Generator1()
        elif hold == '2':
            print('Player Selected Medium Mode')
            hold = ''
            Generator2()
        elif hold == '3':
            print('Player Selected Hard Mode')
            hold = ''
            Generator3()
        elif hold == 't':
            print('''1 being easy and unlimited tries \n2 being medium and 10 tries\n3 being hard and 3 tries''')
            hold = input('Press any key to continue')
            time.sleep(2)
        elif hold == 'q':
            quit()


def Generator1():
    Beginning = int(input("Pick a Number \n"))
    Ending = int(input("Pick a second Number \n"))
    if Beginning<Ending:
        answer = random.randint(Beginning, Ending)
    else:
        answer = random.randint(Ending, Beginning)
    stop = 0
    while stop == 0:
        guess = int(input("Pick a number between " + str(Beginning) + " and " + str(Ending) + "\n"))
        if guess == answer:
            print("you got it")
            time.sleep(5)

            break

        else:
            print('Wrong')


def Generator2():
    Beginning = int(input("Pick a Number \n"))
    Ending = int(input("Pick a second Number \n"))
    if Beginning < Ending:
        answer = random.randint(Beginning, Ending)
    else:
        answer = random.randint(Ending, Beginning)
    stop = 0
    while stop != 11:
        guess = int(input("Pick a number between " + str(Beginning) + " and " + str(Ending) + "\n"))
        if guess == answer:
            print("you got it")
            time.sleep(5)

            break

        else:
            print('Wrong ' + str(10 - stop) + ' tries left')
            stop = stop + 1


def Generator3():
    Beginning = int(input("Pick a Number \n"))
    Ending = int(input("Pick a second Number \n"))
    if Beginning < Ending:
        answer = random.randint(Beginning, Ending)
    else:
        answer = random.randint(Ending, Beginning)
    stop = 0
    while stop != 4:
        guess = int(input("Pick a number between " + str(Beginning) + " and " + str(Ending) + "\n"))
        if guess == answer:
            print("you got it")
            time.sleep(5)

            break

        else:
            print('Wrong ' + str(3 - stop) + ' tries left')
            stop = stop + 1


main()
