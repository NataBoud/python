
# # Calculator
# a = int(input("первое число "))
# operation = input("символ операции ")
# b = int(input("второе число "))
# def calculate(a, b, operation):    # при задании (a, b, operation) - параметры функции
#     #pass  # пропускает операции, заглушка
#     if operation == "+":
#         sum(a, b)
#     elif operation == "-":
#         subtract(a, b)
#     elif operation == "*":
#         multiply(a, b)
#     elif operation == "/":
#         divide(a, b)
#     else:
#         print("неизвестная операция")
# def sum(a, b):
#     result = a + b
#     print(result)
# def subtract(a, b):
#     result = a - b
#     print(result)
# def multiply(a, b):
#     result = a * b
#     print(result)
# def divide(a, b):
#     result = a / b
#     print(result)
#
# calculate(a, b, operation)  # при передаче значений (a, b, operation) - это аргументы функции


sum = 1 + \
     2 + \
     3
print(sum)
sum = (1 +
       2 +
       3)
# print(sum)

name ="natalia+"
if "+" in name:         # in  - оператор членства (оператор сравнения)
    print("1")

# (Значение
# None,
# 0,
# "строка",
# [список] - структура данных,
# (кортеж),
# {словарь},
# set(пустое множество),
# 0.0) = False
# ВСЕ ОСТАЛЬНОE  True

text = "привет мир"
if "мир" in text:
    print("yes")

# текстовые строки
# АТРИБУТ end

# print(1, end='\n') - по умолчанию
print(56, end='')
print(1)




text = "привет мир"
if "мир" in text:
    print("yes")
# БУФЕРИЗАЦИЯ

import time

# . dot.notation

# for num in range(10):
#     print(1 + num, end="\n")
#     time.sleep(1)

# параметр flush - позволяет отключать буферизацию

for num in range(10):
    print(2 + num, end="", flush=True)
    time.sleep(1)

for num in range(10):
    print(2 + num, end="", flush=False)
    time.sleep(1)


# создать строку пре
#
# дложение извлечь по символу с помощью [] и составить новое слово
# functions - split, join, replace


