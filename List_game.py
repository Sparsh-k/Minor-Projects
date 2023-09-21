# This is just a test program for validating user input
def user_choice():
    choice='WRONG'
    acceptable_range= range(0-10)
    within_range = False
    while choice.isdigit()==False or within_range==False:
         choice=input("Enter a number of your choice between 0-10: ")
         if choice.isdigit() == False:
             print("Sorry! That is not a digit")
         if choice.isdigit() == True:
             if int(choice) in acceptable_range:
                 within_range=True
             else:
                 print('Sorry! You are out of the acceptable range of 0-10')
                 within_range=False
                 break
    print(int(choice))
#user_choice()
# Simple user interaction program
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

def position_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice= input("Pick a position (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Pick a choice from (0,1,2)")
    return int(choice)
def replacement_choice(game_list, position):
    user_placement=input("Type the string that you want to change at the position: ")
    game_list[position]=user_placement
    print(game_list)
    return game_list
def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Do you want to continue? Y or N:")
        if choice not in ['Y','N']:
            print("Please choose from Y or N")
    if choice=='Y':
        return True
    else:
        return False

gameon = True
game_list=[0,1,2]
while gameon:
    display_game(game_list)
    position=position_choice()
    game_list=replacement_choice(game_list,position)
    display_game(game_list)
    gameon = gameon_choice()
