import random
user_name = input('Your Username? ')
available_options = ['R','S','P']
print('The available options are:',available_options)
print('R-Rock, S-Scissors, P-Paper')
sys_choice = random.choice(available_options)

#To get the user input yes
def user_input():
    global user_choice
    user_choice = input('Pick a choice? ')
    user_choice = user_choice.upper().strip()
    if user_choice in available_options:
        my_choice(user_choice,sys_choice)
    else:
        print('Wrong choice, please try again!')
        user_input()

#To check conditions on the user choice and the CPU choice
def my_choice(user_choice, sys_choice):
    if user_choice == sys_choice:
        print(f'{user_name}({user_choice}) : CPU({sys_choice})')
        print('Same choices!!!')
        user_input()
    else:
        other_choices(user_choice,sys_choice)

def other_choices(user_choice, sys_choice):
    print(f'{user_name}({user_choice}) : CPU({sys_choice})')
    if user_choice == 'R':
        if sys_choice == 'S':
            print('You won! Rock smashes scissors')
        else:
            print('you lost! Paper covers rock')

    if user_choice == 'S':
        if sys_choice == 'P':
            print('You won! Scissors cuts paper')
        else:
            print('you lost! Rock smashes scissors')

    if user_choice == 'P':
        if sys_choice == 'R':
            print('You won! Paper covers Rock')
        else:
            print('you lost! Scissors cuts paper')
            

user_input()


