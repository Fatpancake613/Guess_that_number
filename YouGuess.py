import os
import re
import random
os.system("cls")
print("Welcome to guess that number!")
print("\n\nHere is how you play: \nThe computer makes a number in the parameters you put down.\nThe player guesses the parameters and if it is guessed wrong, you are deducted a try.\nIf you get it right, however, you win.\n\tIt may be worth noting that the computer will not set a decimal as the \n\tnumber.")

scale = input("1st parameter (Must be integer): ")
scale2 = input("2nd parameter (Must be integer): ")
if scale == "":
    scale = "1"
    print("Defaulted to \"1\"")
if scale2 == "":
    print("Defaulted to \"10\"")
    scale2 = "10"
if scale2 < scale or re.search('[a-zA-Z]', scale) == True or re.search('[a-zA-Z]', scale2) == True:
    print("Error.")
    quit()



num = random.randint(int(scale), int(scale2))
print("Guess a number. You get to decide how many tries you get. Make sure it is inside the 2 parameters that you put down.")
tries = int(input("How many tries do you want? "))
if tries > int(scale2) or tries == int(scale2) or str(tries) == "":
    print("Stop that!")
    quit()
while tries != 0:
    guess = input("Guess: ")
    if guess == "cheat":
        print("Number is " + str(num))
    if guess != str(num) and guess != "cheat":
        print("Wrong.")
        tries -= 1
        print("You have " + str(tries) + " left.")
        if tries == 0:
            break
    elif guess == str(num):
        print("Correct!")
        break
    else:
        print("You have not put in a valid integer.")

print("Your game has finished.")