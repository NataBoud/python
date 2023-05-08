#Блок схема: if name = natalia print natalia
# elif number == 13 print...le nombre est deviné
# else le nombre n'est pas deviné

# name = "Natalia"
# number = 13
# if name == "Natalia":
#     print("Bonjour Natalia")
# elif number == 14:
#     print("le nombre est deviné mais le prenom n'est pas deviné")
# else:
#     print("vous n'avez pas deviné")

# если меньше 18 доступ запрещен
# если возраст равен 18 мы подумаем
# если возраст больше 18 мы вход разрещен
# переменная h=18
#my_name = int(input("enter:"))

# h = int(input("Tapez votre âge"))
# if h < 18:
#     print("Accès interdit")
# if h == 18:
#     print("On va réfléchir")
# if h > 18:
#     print("L'entrée est autorisée")

# c помощью модуля рандом вывести 5 раз на экран рандомные числа от 1 до 10 и познакомиться с инструкцией from import

import random
# Щепотка цифр
str1 = '123456789'
# Щепотка строчных букв
str2 = 'qwertyuiopasdfghjklzxcvbnm'
# Щепотка прописных букв. Готовится преобразованием str2 в верхний     регистр.
str3 = str2.upper()
# print(str3) Выведет: 'QWERTYUIOPASDFGHJKLZXCVBNM'
# Соединяем все строки в одну
str4 = str1+str2+str3
# print(str4) Выведет: '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

# Преобразуем получившуюся строку в список
ls = list(str4)
# Тщательно перемешиваем список
random.shuffle(ls)
# Извлекаем из списка 12 произвольных значений
psw = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print(psw)


import random
print(''.join([random.choice(list('12345678910')) for x in range(5)]))

import random
psw = ''    # предварительно создаем переменную psw
for x in range(5):
    psw = psw + random.choice(list('12345678910'))

print(psw)
# Выведет: Ci7nU6343YGZ

# вывести с помощью цикла for четные числа от 1 до 100
# for i in range(0, 101, 2):
#     print(str(i))

print(psw)



number = 0
while number <= 100:
    number += 1
    if number % 2 == 0:
        print(number)


number = 1
while number <= 99:
    number += 1
    if number % 2 == 1:
        print(number)

# from random import *   - из библиотеки рандом импортирутся все
# print(randint(0, 10))

for i in range(5):
    print(random.randint(0, 10))      # все, что после точки называется метод

