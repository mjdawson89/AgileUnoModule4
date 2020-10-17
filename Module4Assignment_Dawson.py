#Matthew Dawson
#Module 4 Assignment

#import from required libraries
from sys import exit
from random import randint

"""initializing variables"""
#myData dictionary (stores my name)
myData = {}
myData["first_name"]="Matt"
#guesses variable (starts at 0)
guesses = 0 
#wins variable (starts at 0)
wins = 0

"""context manager (running code in the context that the file is open,
once completed the file is automatically closed)"""
with open("questions.txt", "r") as infile:
    #read each line in the questions.txt file and store them as a list of 'questions'
    questions = infile.readlines()
    #for each question if the list of questions...
    for question in questions:
        #if the string "first" is in the question
        if "first" in question:
            #prompt the user with the question and save the input to the myData dictionary as the variable "first_name"
            myData["first_name"] = input(question)
        #if the string "last" is in the question
        elif "last" in question:
            #prompt the user with the question and save the input to the myData dictionary as the variable "last_name"
            myData["last_name"] = input(question)
        #if none of the above is true the questions.txt file is incorrect
        else:
            print("bad question in input file")
            exit()

"""for loop for each play of the guessing game out of 10 plays"""
for play in range(10):
    #pick a random number between 0 and 100
    number = randint(0,100)
    #initialize the solved variable as False (not yet solved)
    solved = False
    #while solved is False
    while not solved:
        #prompt user to guess an integer from 0 to 100
        guess = int(input(f"Guess a number from 0 to 100 : "))
        #add 1 to the number of guesses after each guess
        guesses += 1
        #if guess is the number (user won the game)
        if guess == number:
            #print congratulatory statement
            print("Great job," + myData["first_name"] + f"your guess of {guess} is correct!")
            #add 1 to the number of wins
            wins += 1
            #change the solved variable to True
            solved = True
            #end the for loop
            break
        # guess is not the number, print that the guess is incorrect.
        else:
            print(f"Your guess of {guess} is incorrect!")
        #if guess is greater than the number
        if guess > number:
            #tell the user their guess was too high
            print(f"Sorry, you guessed too high!")
        #if guess was less than the number
        elif guess < number:
            #tell the user their guess was too low
            print(f"Sorry, you guessed too low!")
        #if non of the above are true
        else:
            #tell the program to pass on to the next part of the code
            pass
    #if the game was solved        
    if solved:
        #show the user the number of completed plays
        print(f"Lets play again, you have completted {wins} out of 10 plays.")
        #continue the for loop
        continue

#print the final results and exit the program..
print(myData["first_name"] + " " + myData["last_name"] + f" guessed the correct number {wins} out of 10 plays.")
print("It took " + myData["first_name"] + " " + myData["last_name"] + f"{guesses} guesses to do this!")
exit()