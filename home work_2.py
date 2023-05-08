# дописать 5 условий, разобрать код программы
    # записать с нуля таблицу истинности для каждщго булевого оператора, перечислить 6 операторов сравнения,
    # объяснить что такое условия и где оно используется


#########   rock, paper, scissors   #########

# import random, sys
# print("pierre, ciseaux, feuille")
#
# win = 0
# losses = 0
# ties = 0
#
# while True:
#     print(f"{win}, {losses}, {ties}")
#
#     while True:
#         player_move = input("Enter")
#         if player_move == "q":
#             sys.exit()
#         if player_move == "p" or player_move == "c" or player_move == "f":
#             break
#
#     if player_move == "p":
#         print("pierre")
#     elif player_move == "c":
#         print("ciseaux")
#     elif player_move == "f":
#         print("feuille")
#
#     player2 = random.randint(1, 3)
#     if player2 == 1:
#         computer_move = "p"
#         print("pierre")
#     elif player2 == 2:
#         computer_move = "c"
#         print("ciseaux")
#     elif player2 == 3:
#         computer_move = "f"
#         print("feuille")
#
#     if player_move == computer_move:
#         print("Ties")
#         ties += 1
#     elif player_move == "p" and computer_move == "c":
#         print("You win!")
#         win += 1
#
#     elif player_move == "c" and computer_move == "p":
#         print("You lost!")
#         win += 1
#     elif player_move == "p" and computer_move == "f":
#         print("You lost!")
#         win += 1
#     elif player_move == "f" and computer_move == "p":
#         print("You win!")
#         win += 1
#     elif player_move == "c" and computer_move == "f":
#         print("You win!")
#         win += 1
#     elif player_move == "f" and computer_move == "c":
#         print("You lost!")
#         win += 1

# BOOLEAN OPERATOR
# and - и, работает с двумя булевыми значениями
# or - или (вернет true если один из опереандов true)
# not - не (применяется к одному булевуму значению, он называется унарным)

# ТАБЛИЦА ИСТИННОСТИ ДЛЯ ОПЕРАТОРА and
# выражение          результат
# True and True      True
# True and False     False
# False and True     False
# False and False    False

# ТАБЛИЦА ИСТИННОСТИ ДЛЯ ОПЕРАТОРА or

# выражение          результат
# True and True      True
# True and False     True
# False and True     True
# False and False    False

# ТАБЛИЦА ИСТИННОСТИ ДЛЯ УНАРНОГО ОПЕРАТОРА not

# выражение          результат
# not True              False
# not False             True

#Comparison operator - сопоставляет два значения и возвращает результат в виде булевого значения (True False)
# operator        operation
# 1  ==              égale
# ====            égale c проверкой типов данных
# 2  !=              non égale
# 3  <               moins
# 4  >               plus
# 5  <=              moins ou égale
# 6  >=              plus ou égale

# БЛОКИ КОДА
# if это заголовок инструкции, может существовать одна
#elif инструкция - иначе-если, содержит блок условий

# сделать цикл for с отрицательным шагом
for i in range(6, 0, -2):
    print("Natalia" + str(i))

# написать программу в зависимости от того, что храниться в get number = 1, print Hello! if get number = 2, Print good bye
get_number = 0
if get_number == 1:
    print("Hello!")
if get_number == 2:
    print("Good bye!")








