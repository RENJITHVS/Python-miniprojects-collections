import random

def my_guess(x):
    rand_num= random.randint(1, x)
    guess = 0
    while guess!= rand_num:
        guess = int(input(f"geuss number betweenn 1 and {x} \t"))
        if guess < rand_num:
            print("sorry , guess agin, too low")
        elif guess > rand_num:
            print("sorry, guess agin, too high")

    print(f"yay ! got it {rand_num}")

def comp_guess(x):
    low = 1
    high =x
    feedback =" "
    while feedback != "c":
        if low!=high:
            # guess= (low+high)//2
            guess= random.randint(low,high)
        else:
            guess = low
        feedback = input(f"is {guess}, if too high type 'h',if too low type 'l',if correct type 'c").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1

    print(f'hurray computer got the {guess} correctly')


comp_guess(1000)
