
__author__ = 'Akimov Yaroslav Vladimirovich'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
random_number = 1280497000737375
count = 0
while count < len(str(random_number)):
	print(str(random_number)[count])
	count += 1



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


# -----VARIABLE INTERCHANGE. MATH METHOD -------

x = int(input("Enter X:"))
y = int(input("Enter Y:"))

x += y
y = x - y
x = x - y

print("X and Y are interchanged by math method, X =", x," Y =", y)

# -----VARIABLE INTERCHANGE. PYTHON METHOD WITH TEMPORARY TUPLE-------

x, y = y, x

print("X and Y are changed again by python method (temporary tuple), X =", x," Y =", y)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

