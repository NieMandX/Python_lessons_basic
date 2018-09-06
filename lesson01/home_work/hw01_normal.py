
__author__ = 'Akimov Yaroslav Vladimirovich'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
number = int(input("Enter an integer:"))
counter = maximum = 0
while counter < len(str(number)):
	if maximum < int(str(number)[counter]):
		maximum = int(str(number)[counter])
	counter += 1
print(maximum, "is a maximum digit in that number")	



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# -----VARIABLE INTERCHANGE. MATH METHOD -------

x = int(input("Enter X:"))
y = int(input("Enter Y:"))

x += y
y = x - y
x = x - y

print("X and Y are interchanged by math method, X =", x," Y =", y)

# -----VARIABLE INTERCHANGE. PYTHON METHOD WITH TEMPORARY TUPLE-------

x, y = y, x

print("X and Y are interchanged again by python method (temporary tuple), X =", x," Y =", y)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
print("\n")
print('*'*30)
print("Solving the Quadratic Equation")
print("       ax² + bx + c = 0")
print('*'*30)
coefficients = list(range(3))
for index in range(3): 
	print("Please, enter a coefficient "+ chr(ord('a') + index) + ":", end ='')
	while True:
		coefficients[index] = input()
		try:
			coefficients[index] = float(coefficients[index])
			break
		except ValueError:
			print ("Please be carefully, it must be a Number, enter %c:" % chr(ord('a') + index), end = '')
			pass
if coefficients[0] == 0:
	print('*'*30)
	print("   This is Linear Equation")
	print('*'*30)
	print("         %.1fx = %.1f" % (coefficients[1], -coefficients[2]))
	print("            x = %.1f" % (-coefficients[2] / coefficients[1]))
else:
	D = coefficients[1]**2 - 4 * coefficients[0] * coefficients[2]
	if D > 0:
		x1 = (-coefficients[1] + math.sqrt(D)) / (2 * coefficients[0])
		x2 = (-coefficients[1] - math.sqrt(D)) / (2 * coefficients[0])
		print('*'*30)
		print("This Equation has 2 roots:")
		print('*'*30)
		print("        x1 = %.1f" % x1)
		print("        x2 = %.1f" % x2)
		print('*'*30)
	elif D == 0:
		x1 = x2 = -coefficients[1] / (2 * coefficients[0])
		print('*'*30)
		print("This Equation has 1 root:")
		print('*'*30)
		print("       x1 = x2 = %.1f" % x1)
		print('*'*30)
	elif D < 0:
		print('*'*30)
		print("This Equation has no real roots!")
		print('*'*30)
