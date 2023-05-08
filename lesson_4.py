#########   IMPORT     #########

import random

# библиотека сус
# вызов метода это точечная нотация - .

import sys
# while True:
#     n = input("Enter")
#     if n == "exit":
#         # sys.exit()
#         break
#     print(n)

#########   ИГРА     #########

secret_number = random.randint(1, 20)
for guesses_number in range(5):  # guesses_number это та же i она бегает по range и хранит в себе индексы начинается с 0
    guess = int(input("enter"))

    if guess < secret_number:
         print("Загаданное число больше")
    elif guess > secret_number:
         print("Загаданное число меньше")
    else:
        print(f"вы угадали! Попыток {guesses_number}, загаданное число {secret_number}")
        break
if guess != secret_number:
     print(f"loser, number of attempts {guesses_number},загаданное число {secret_number}")
     

#########   pierre, feuille, ciseaux / rock, paper, scissors    #########

import random, sys
print("pierre, ciseaux, feuille")

win = 0
losses = 0
ties = 0

while True:
    print(f"{win}, {losses}, {ties}")

    while True:
        player_move = input("Enter")
        if player_move == "q":
            sys.exit()
        if player_move == "p" or player_move == "c" or player_move == "f":
            break

    if player_move == "p":
        print("pierre")
    elif player_move == "c":
        print("ciseaux")
    elif player_move == "f":
        print("feuille")

    player2 = random.randint(1, 3)
    if player2 == 1:
        computer_move = "p"
        print("pierre")
    elif player2 == 2:
        computer_move = "c"
        print("ciseaux")
    elif player2 == 3:
        computer_move = "f"
        print("feuille")

    if player_move == computer_move:
        print("Ties")
        ties += 1
    elif player_move == "p" and computer_move == "c":
        print("You win!")
        win += 1

    elif player_move == "c" and computer_move == "p":
        print("You lost!")
        win += 1
    elif player_move == "p" and computer_move == "f":
        print("You lost!")
        win += 1
    elif player_move == "f" and computer_move == "p":
        print("You win!")
        win += 1
    elif player_move == "c" and computer_move == "f":
        print("You win!")
        win += 1
    elif player_move == "f" and computer_move == "c":
        print("You lost!")
        win += 1

    # дописать 5 условий, разобрать код программы
    # записать с нуля таблицу истинности для каждщго булевого оператора, перечислить 6 операторов сравнения,
    # объяснить что такое условия и где оно используется

    # написать программу в зависимости от того, что храниться в get number = 1, print Hello! if get number = 2, Print good bye
    # сделать цикл for с отрицательным шагом







