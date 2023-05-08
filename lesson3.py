# CYCLES

number = 0
if number < 5:
    print("Hello world1")
    number += 1
    # += это называется синтаксический сахар, little form
    # number = number + 1   long form

#####################   CYCLE while     #####################

number = 0
while number <= 5:
    print("Hello world")
    number += 1     # действие называетяс инкримент
    # iteratsia итерация каждый круг в цикле

#  istruction break -прерывает цикл, istruction continue  - возвращает в цикл

# name = ""
# count = 0  # переменная "счетчик"
# while name != "Natalia":
#     name = input("enter")
#     count += 1
#     if name == "Natalia":
#         print("vous avez deviné")
#         break
#     #print(count)
#     if count == 2:
#         print("Vous avez eu 2 essais")
#         break
    #if name != "Natalia":
        #continue

# number = 0  # number = 0 - это переменная в которой лежат четные числа
# while number <= 10:
#     number += 1
#     if number %  2 != 0:
#         continue
#     else:
#         print(number)

number = 1
while number <= 10:
    number += 1
    if number % 2 != 0:
        continue
    else:
        print(number)

number = 0
if number < 5:
    print("Hello world1")
    number += 1

#####################   CYCLE for   #####################

# в этом цикле лежат переменные которые относятся только к циклу for
# for i in..... - для переменной i в диапазоне - range(start,stop,step) - это функция, которая принимает три параметра - start stop step
# i - итерируемая переменная
# Если в функции range 1 параметр по индексам, то она бежит (stop n-1), итерация начинается с 0
# for i in range(5, 0, -1):
#     print("Natalia" + str(i))
    # Natalia0 # В программировании язык начинается с нуля
    # Natalia1
    # Natalia2
    # Natalia3
    # Natalia4
# for i in range(6, 0, -2):   # четные
#     print("Natalia" + str(i))

# for i in range(101):
#     print(i)

total = 0
for i in range(101):
    total += i - i + 1  # превратить i в ноль
    print(total)

###################     ИМПОРТИРОВАНИЕ МОДУЛЕЙ      #####################

# модуль это библиотека - ключевое слово import

import random

# c помощью модуля рандом вывести 5 раз на экран рандомные числа от 1 до 10 и познакомиться с инструкцией from import
# вывести с помощью цикла for четные числа от 1 до 100




















