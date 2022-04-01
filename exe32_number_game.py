#Guess the number game

from my_functions import conv_numbers
from my_functions import give_rand

def main_game():
    print('Lets play a number game\n')

    while True:
        difficul = conv_numbers(input("Choose difficulty between 1, 2, 3 :"))
        if difficul >= 1 and difficul <= 3:
            break
    num = give_rand(difficul)

    print("""Lets start the game. 
            I have my number.\n""")
    print(f'your num is {num}')

    guess = 0
    while True:
        get_inp = conv_numbers(input("What is your guess? "))
        guess += 1
        
        if get_inp == num:
            print(f"you got {num} it in {guess} guesses")
            break
        
        if difficul == 1:
            if abs(get_inp - num) > 5:
                print("very high")
            else:
                print("very low")
        
        elif difficul == 2:
            if abs(get_inp - num) > 50:
                print("very high")
            else:
                print("very low")
        
        else:
            if abs(get_inp - num) > 500:
                print("very high")
            else:
                print("very low")
    play = input('Want to play again? y / n : ')
    return play

while True:
    play = main_game()

    if play != 'y':
        print("Good Bye")
        break
