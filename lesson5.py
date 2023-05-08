for i in range(5):
    n = 0
    while n < 3:
        print("Hello world")
        n += 1

for i in range(1, 11):
    print(i)

n = 1
while n < 11:
    print(n)
    n += 1      # n = n + 1

# function def  - объявить функцию  def natalia() - заголовок функции : - тело функции или инструкции
# def natalia(word) - word - параметр функции
# Далее НУЖНО ВЫЗВАТЬ ФУНКЦИЮ! Код написанный  функциями - процедурное программирование
def natalia(number, operator):
    # return (f"Natalia is a {number} web developer")
    # return  None
# natalia("cool")       # вызов функции
# natalia("bad")       # вызов функции
    pass
    #natalia(number, operator)
number = 7
print(natalia(number, 10))

# инструкция return - покидает функцию и возвращает значение
# none  - это тип данных  - ничего
# вызов f самой себя , f - рекурсия

def hello_world(n):
    for i in range(n):
        return i
print(hello_world(5))


# Узнать что такое стек вызовов, порядок стек вызовов, написать калькулятор, обернуть в функцию и два операнда (напр x y) которые будут складывать и умножать
# return почему она не используется в цикла? Посмотреть что такое передача параметров по ссылке.
# написать функцию которая будет выводить 5 раз рандомное число (в range через n и три параметра функци n) перв параметр это n а вторые параметры старт стоп

# Calculator
a = int(input("первое число "))
operation = input("символ операции ")
b = int(input("второе число "))
def calculate(a, b, operation):    # при задании (a, b, operation) - параметры функции
    #pass  # пропускает операции, заглушка
    if operation == "+":
        sum(a, b)
    elif operation == "-":
        subtract(a, b)
    elif operation == "*":
        multiply(a, b)
    elif operation == "/":
        divide(a, b)
    else:
        print("неизвестная операция")
def sum(a, b):
    result = a + b
    print(result)
def subtract(a, b):
    result = a - b
    print(result)
def multiply(a, b):
    result = a * b
    print(result)
def divide(a, b):
    result = a / b
    print(result)

calculate(a, b, operation)  # при передаче значений (a, b, operation) - это аргументы функции

