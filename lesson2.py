word = len("hello world")
print(word)
#Boolean Logic булев тип данных True False в кавычки не заключаются и с большой буквы
chek = True
chek_1 = False
print(chek)
print(chek_1)
#Comparison operator - сопоставляет два значения и возвращает результат в виде булевого значения (True False)
# operator        operation
# ==              égale
# ====            égale c проверкой типов данных
# !=              non égale
# <               moins
# >               plus
# <=              moins ou égale
# >=              plus ou égale
print(1 == 1)
print(1 != 1)
print(1 <= 1)
print(True != False)
print(1 == 1.0)
print(1 == "1.0")
#строгое сравнение
# ====            égale c проверкой типов данных

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
print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))
print((1 == 2) or (2 == 2))

# БЛОКИ КОДА
# if это заголовок инструкции, может существовать одна
#elif инструкция - иначе-если, содержит блок условий

natalia = True
if not True:
    print("Bonjour Natalia")# это тело инструкции
elif not natalia:
    print("verite")
elif natalia == True:
    print("verite 2")
else:
    print("non")

name = "natasha"
number = 13
if name == "natasha" and number == 13:
    print("vous avez deviné")
else:
    print("vous n'avez pas deviné")
