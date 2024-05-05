#Welcome to the Rock,Paper,Scissor game.
#The rules of the game is declared below:
"""
First Rule is:
Rock vs Paper -> Paper Wins
Second Rule is:
Rock vs Scissor -> Rock Wins
Third Rule is:
Paper vs Scissor -> Scissor Wins
Fourth Rule is:
If userchoice(rock,paper,scissor) and computerchoice(rock,paper,scissor) is same then the game will tie.
"""
import random
option=("rock","paper","scissor")
while True:
    userchoice=input("Whether you want to play game or not.Give answer in (Yes or No):")
    if(userchoice=="No"):
        break
    #Implemntation of rule is done below:
    userchoice=input("Choose the element(rock,paper,scissor):")
    computerchoice=random.choice(option)
    print("Your Choice is:",userchoice)
    print("Computer Choice is:",computerchoice)
    if(userchoice==computerchoice):
        print("It's Tie.")
    elif(userchoice=="rock" and computerchoice=="scissor"):
        print("You Won!")
    elif(userchoice=="paper" and computerchoice=="rock"):
        print("You Won!")
    elif(userchoice=="scissor" and computerchoice=="paper"):
        print("You Won!")
    else:
        print("You Lose!.Please try again.")
print("-----GAME OVER-----")