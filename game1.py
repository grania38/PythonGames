#This is rock paper and scissors game
import random

def rock_paper_scissors():
    r = "rock"
    p = "paper"
    sc = "scissors"
    all_choices = [r, p, sc]

    user = input(f"Enter a valid choice({r}, {p}, {sc}):")
    if user not in all_choices:
        print("Invalid choice!")

    computer = random.choice(all_choices)

    print(f"User chose {user} and computer chose {computer}")

    #r>p r>sc sc>p

    if user == computer:
        print("Tie")
    elif(user==r and computer==p) or (user == r and computer==sc) or (user == sc and computer == p):
        print("You won!")
    else:
        print("You lost!")

if __name__ == "__main__":
    rock_paper_scissors()