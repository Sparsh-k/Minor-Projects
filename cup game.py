from random import shuffle
mylist=['','O','']
def randomizer(mylist):
    shuffle(mylist)
def player_guess():
    guess=''
    while guess not in [0,1,2]:
        guess = input("Choose on of the cups from 0, 1, 2 : ")
        return int(guess)
    print(guess)
def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("Correct!")
    else:
        print("Incorrect! Better luck next time")
        print(mylist)
mixed_list=randomizer(mylist)
guess=player_guess()
check_guess(mylist,guess)