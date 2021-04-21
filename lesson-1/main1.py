# Переменная - это ячейка в памяти. Переменные можем запрашивать от пользователя
# или сами устанавливать. Переменные позволяют хранить информацию и использовать ее в дальнейшем.

# Типы переменных в Python не обьявляются очевидно, но они присутствуют.
# name_1 = 'Hello World!'
# name_2 = 100
# word = "м'яч"
#
# print(word)
#
# name = input("Введите Ваше имя: ")
# surname = input("Please, enter your surname: ")
# age = input("Please, enter your age: ")
# print("Ваше имя и фамилия: ", name, surname)
# print("Возраст: ", age)
#
# city = input("укажите свой город: ")
# print("city: ", city)


#
# print("Enter your city: ")
# your_locate=input()
# print("Your city is ", your_locate)
#
# name = input("Please, enter your name: ")
# surname = input("Please, enter your surname: ")
# print("Name: {1}, surname: {0}.". format(name, surname))


surname = input("Укажите вашу фамилию: ")
name = input("Введите ваше имя: ")
otchestvo = input("Укажите ваше отчество: ")
telephon = input("Укажите свой номер телефона: ")
age = input("Укажите ваш возраст: ")
city = input("Укажите свой город: ")
music = input("Укажите ваш любимый жанр музыки: ")
street = input("Укажите улицу на которой вы живёте: ")
print("Ваше имя и фамилия и отчество: ", name, surname, otchestvo)
print("Ваш возраст: ", age)
print("Ваша улица: ", street)
print("Ваш город: ", city)
print("Ваш номер телефон: ", telephon)
print("Ваш любимый жанр: ", music)

#or

# name = input("Введите ваше имя: ")
# surname = input("Введите вашу фамилию: ")
# otchestvo = input("Укажите ваше отчество: ")
# print("Name: {0}, surname: {1}, patronymic: {2}.". format(name, surname, patronymic))