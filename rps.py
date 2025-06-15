""" scissors beats paper,
paper beats rock,
rock beats scissors"""
# we have to input player choice get the compute choice from random and create lists and dictionaries too
import random
def play():
    while True:
        decision= input("Do you want to play?")
        if decision == " no":
            print(" okay bye")
        else:

            def get_choices():
                options=["rock","paper","scissors"]
                player_choice=input("Enter a choice(rock, paper,scissors):")
                computer_choice=random.choice(options)
                print(f"You chose {player_choice},computer chose {computer_choice}")
                choices={"player":player_choice,"computer":computer_choice}
                return(choices)
            def CheckWin(player,computer):

                if player=="rock"and computer=="scissors":
                        return("rock beats scissors, you win")

                elif player==computer:
                    return("draw!!")

                elif player=="paper":
                    if computer=="rock":
                        return("paper beats rock, you win")
                    else:
                        return("you lose")

                elif player == "scissors":
                    if computer == "paper":
                        return ("scissors beats paper, you win")
                    else:
                        return ("you lose")


            choices= get_choices()
            result=CheckWin(choices["player"],choices["computer"])
            print(result)
play()


