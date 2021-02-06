import os
import time
import random
import re
#>>>>>>>>>>>>>>>>>>>>>setup<<<<<<<<<<<<<<<<<<<<<<<<<
os.system("cls")
print("\n\nWelcome to guess that number!")
print("Rules are simple:\nYou choose a number, the range, and how many guesses the computer can take \nbefore failing.")
#answer define
#error 2
answer = input("What is the number the computer will try to guess? ")
if re.search("[a-zA-Z]", answer) == True:
    print("Error 2: Invalid syntax to variable 'answer'.")
    quit()
if answer == "":
    answer = "5"
    print("Defaulted to \"" + answer + "\"")
if re.search("[a-zA-Z]", answer) == True:
    print("Error 2: Invalid syntax to variable 'answer'.")
    quit()
#scale1 
#error3 
scale = input("1st parameter (Must be integer): ")
if scale == "":
    scale = "1"
    print("Defaulted to \"" + scale + "\"")
if (answer < scale) == True:
    print("Error 3: Answer is outside parameters (Smaller)")
    quit()
#scale2
scale2 = input("2nd parameter (Must be integer): ")

if scale2 == "":
    scale2 = "10"
    print("Defaulted to \"" + scale2 + "\"")
#validating answer
if scale2 < scale or re.search('[a-zA-Z]', scale) == True or re.search('[a-zA-Z]', scale2) == True:
    print("Error 1: invalid parameters.")
    quit()
#error 3 also
if (answer < scale2) == True:
    print("Error 3: Answer is outside parameters (Larger)")
#tries define
tries = int(input("How many attempts does the computer get? "))
if str(tries) == "":
    tries = 3
    print("Defaulted to " + str(tries) +".")
#error 4
if scale == scale2:
    print("Error 4: Variable 'scale' equals the same as 'scale2'")

attempts = 0

#guessing
while int(tries) != 0:

    guess = random.randint(int(scale), int(scale2))
    print("Guess " + str(attempts) + " is " + str(guess))
    #time.sleep(0.00000000000001)
 
    if (guess == int(answer)):
        print("The computer got it right!")
        print("Computer won!")
        print("\n\n\nIt took " + str(attempts) + " attempts to guess the \"password\".")
        break
        
    else:
        print("The computer got it incorrect.")
        tries -= 1
        print("The computer has " + str(tries) + " left.")
        attempts += 1
    if (tries == 0):
        print("Player won!")
print("The game has finished.")