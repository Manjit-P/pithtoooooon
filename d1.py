import random
def getchoices():
    playerchoice=input("enter your choice ")
    option=["rock","paper","scissors"]
    computerchoice=random.choice(option)
    choices = {"player" : playerchoice, "computer": computerchoice}
    return choices
choice=getchoices()
def check(player,computer):
    print(f"your choice {player} and computer chose {computer}")
    if player==computer:
        return "its a tie"
    elif player=="rock" and computer == "scissors":
        return "you won"
    elif player=="paper" and computer == "rock":
        return "you won"
    elif player=="scissors" and computer == "paper":
        return "you won"
    elif player=="rock" and computer == "paper":
        return "you lost"
    elif player=="paper" and computer == "scissors":
        return "you lost"
    elif player=="scissors" and computer == "rock":
        return "you lost"
    else:
        return"invalid"
result=check(choice["player"],choice["computer"])
print(result)