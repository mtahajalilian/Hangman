import os 
import random
import time


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def hangman_figures():
    global figure_1
    global figure_2
    global figure_3
    global figure_4
    global figure_5
    global figure_6

    figure_1 =  "  _____\n"\
                "  |   |\n"\
                "  |\n"\
                "  |\n"\
                "  |\n"\
                "  |\n"\
                "  |\n"\
                "__|______________\n"
    
    figure_2 =  "  _____\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |\n"\
                "  |\n"\
                "  |\n"\
                "  |\n"\
                "__|______________\n"
    
    figure_3 =  "  _____\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |\n"\
                "  |\n"\
                "  |\n"\
                "__|______________\n"

    figure_4 =  "  _____\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |   O\n"\
                "  |\n"\
                "  |\n"\
                "__|______________\n"

    figure_5 =  "  _____\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |   O\n"\
                "  |  /|\\\n"\
                "  |\n"\
                "__|______________\n"
    
    figure_6 =  "  _____\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |   |\n"\
                "  |   O\n"\
                "  |  /|\\\n"\
                "  |  / \\\n"\
                "__|______________\n"


def main():
    global guess_list
    global word
    with open('random_words.txt', 'r') as file:
        guess_list = []
        for i in range(10):
            guess_list.append(file.readline())
    word = random.choice(guess_list)[:-1] if random.choice(guess_list)[-1] == '\n' else random.choice(guess_list)


def hangman():
    count = 6
    score = 120
    clear_screen()
    print('\n* Welcome to Hangman!')
    print('* You have 6 chances to guess the correct answer.\n')
    time.sleep(1)
    start = input('* Do you want to play?(y,n): ')
    if start == 'y':
        while count > 0:
                for i in guess_list:
                    print(f'- {i}', end='')
                time.sleep(1)
                userguess = input("\n> What's your choice? ").lower()
                if userguess != word:
                    count -= 1
                    score -= 20
                    if count > 0:
                        clear_screen()
                        print(eval(f'figure_{6 - count}'))
                        print('> Wrong answer')
                        print(f'Remain chance: {count}\n')
                        print('*' * 50)
                        time.sleep(2)
                    else:
                        clear_screen()
                        print(eval(f'figure_{6 - count}'))
                        print('> Game over!\n')
                elif userguess == word:
                    time.sleep(2)
                    print('\n\n> Congratulations!\n')
                    print(f'> Your score is {score}')
                    print(f'Remain chance: {count}')
                    exit()

        
    else:
        print('\n> We expect you come again (:\n')
        exit()


hangman_figures()
main()
hangman()

