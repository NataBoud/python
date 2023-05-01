#Блок схема: if name = natalia print natalia
# elif number == 13 print...le nombre est deviné
# else le nombre n'est pas deviné

name = "Natalia"
number = 13
if name == "Natalia":
    print("Bonjour Natalia")
elif number == 14:
    print("le nombre est deviné mais le prenom n'est pas deviné")
else:
    print("vous n'avez pas deviné")

# если меньше 18 доступ запрещен
# если возраст равен 18 мы подумаем
# если возраст больше 18 мы вход разрещен
# переменная h=18
#my_name = int(input("enter:"))

h = int(input("Tapez votre âge"))
if h < 18:
    print("Accès interdit")
if h == 18:
    print("On va réfléchir")
if h > 18:
    print("L'entrée est autorisée")
