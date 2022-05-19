import random

#function to play rock paper scissor
def play(user, comp):

    if user == comp:
        return "it is a tie"

    #winner
    if (user == 'r' and comp == 's') or (user == 's' and comp =='p') or (user == 'p' and comp == 'r'):
        return "you win!"

    return "You lost"



if __name__ == "__main__":
    print("--welcome to rock papper Scissor game--")
    user = input("Enter your choices, if rock type 'r' ,if scissor type 's', if paper type 'p'").lower()
    comp = random.choice(['r','s','p'])
    print(play(user,comp))
