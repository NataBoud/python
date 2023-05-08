# slice() can take 3 parameters:
# start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
# stop - Integer until which the slicing takes place. ...
# step (optional) - Integer value which determines the increment between each index for slicing.
# (slice)[start:stop:step:]

# split()  - переменная.функция(аргументы), принимает строку возвращает список
text_1 = "Bonjour je m'appelle Natalia"
convert_in_list = text_1.split()
print(convert_in_list)

# join()  - строка.функция(список - это аргумент), принимает список возвращает строку
list = ['Bonjour', 'je', "m'appelle", 'Natalia']
convert_to_string = '!'.join(list)
print(convert_to_string)

# replace() method accepts a maximum of 3 parameters:
# old – the old substring (подстрока) to be replaced (найти и заменить в строке подстроку)
# new – the new substring to replace the old one
# count (optional) – integer value specifying the number of times we want to replace the old substring with the new substring
# syntax for replace - variable.function("old", "new", count)
text_1 = "Bonjour je m'appelle Natalia"
replace = text_1.replace("Bonjour", "Coucou")
print(replace)

# strip() - устраняет символы с обоих концов строки (пробел, таб, \n )
# syntax - variable.function()
text_1 = " Bonjour je m'appelle Natalia!"
x = text_1.replace("Bonjour", "Coucou")
print(x.strip("a!"))


# Понятие 'Строковые литералы' в python начинаются и заканчиваются одинарными кавычками
# Экранированый символ (выводиться на экран)
# \' - апостроф
# \" - двойная кавычка
# \t - табуляция
# \n - новая строка в разрыв строки
# \\ - обратная косая черта


# (r'') - r string- необработанные строки -интерпритатор воспринимает буквально и все выводит на экран
print(r'mgcmh hkffkdcgf \'')

text_new = "hfdehfc cfkief" \
           " kefkfcjn ckjlkc"   # \ newline - escape sequence (последовательность)
print(text_new)

word = 