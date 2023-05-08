text = "привет мир"
if "мир" in text:
    print("yes")

print(56, end='')
print(1)

phrase = "j'ai faim je vais manger"
print(phrase[8] + phrase[2] + phrase[18] + phrase[19] + phrase[20])
print(phrase.split())

result = phrase.split()
for i in result:
    print(i[0], end="")
print()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

name = "Natalia"
print(name[0] + "uage")

# define strings
firstname = "Natalia"
lastname = "Boudard"

# define our sequence
sequence = (firstname, lastname)
# join into new string
name = " ".join(sequence)
print(name)

words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)

name = "Natalia Kondruseva"
a = name.replace("Kondruseva", "Boudard")
print(a)











