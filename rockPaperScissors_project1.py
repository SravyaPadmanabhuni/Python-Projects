#to generate random choice from computer we need to import random module
import random
user_choice = int(input('Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: '))
if user_choice > 2 and user_choice < 0:
    print('You entered invalid, you lose!')
else:
    computer_choice = random.randint(0, 2)
    print('Computer Choice: ', computer_choice)
    if computer_choice == user_choice:
        print("It's a draw!!")
    elif computer_choice == 0 and user_choice == 2:
        print('You lose.')
    elif user_choice == 0 and computer_choice == 2:
        print('You win.')
    elif computer_choice > user_choice:
        print('You Lose.')
    elif user_choice > computer_choice:
        print('You win.')

