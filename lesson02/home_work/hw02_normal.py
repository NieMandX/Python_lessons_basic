# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

# Homework N2. Level: Normal. Task 1.
import random
from math import sqrt

print('\n'*2)
print('{:*^60}\n'.format('Homework N2. Level: Normal. Task 1.'))

numbers1 = [random.randint(-25,25) for k in range(50)]
numbers3 = [m for m in numbers1 if m >= 0 and m**.5 == int(m**.5)]
numbers2 = [int(k**.5) for k in numbers1 if k >= 0 and sqrt(k) == int(sqrt(k))]

print ()
print ('random integer list: ', ' | '.join('{}'.format(n) for n in numbers1))
print ()
print ('Square roots list: ', ' | '.join('{}'.format(n) for n in numbers2))

print()
input('{:-^60}'.format('press Enter to continue'))


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print('\n')
print('{:*^60}\n'.format('Homework N2. Level: Normal. Task 2.'))
print ()

days = {'01': 'first', '02': 'second', '03': 'third', '04': 'fourth', '05': 'fifth',
		'06': 'sixth', '07': 'seventh', '08': 'eighth', '09': 'ninth', '10': 'tenth',
		'11': 'eleventh', '12': 'twelfth', '13': 'thirteenth', '014': 'fourteenth', '15': 'fifteenth',
		'16': 'sixteenth', '17': 'seventeenth', '018': 'eighteenth', '19': 'nineteenth', '20': 'twentieth',
		'21': 'twenty-first', '22': 'twenty-second', '23': 'twenty-third', '24': 'twenty-fourth', '25': 'twenty-fifth',
		'26': 'twenty-sixth', '27': 'twenty-seventh', '28': 'twenty-eighth', '29': 'twenty-ninth', '30': 'thirtieth',
		'31': 'thirty-first'}

month = {	'01': 'January', '02': 'February', '03': 'March', '04': 'April',
			'05': 'May', '06': 'June', '07': 'July', '08': 'August',
			'09': 'September', '10': 'October', '11': 'November', '12': 'December'}

dig_date = input("Please, enter date in format dd.mm.yyyy:")

datelist = dig_date.split('.')

print('Current data is : {} of {} {} year'.format(days.get(datelist[0]),month.get(datelist[1]),datelist[2]))

print()
input('{:-^60}'.format('press Enter to continue'))




# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random



print('\n')
print('{:*^60}\n'.format('Homework N2. Level: Normal. Task 3.'))
print ()

print ("Please, Enter lenght of random list:", end = '')

while True:
		lenlist = input ()
		try:
			lenlist = int(lenlist)
			break
		except ValueError:
			print ("Please, be carefully, it must be an Integer number, enter lenght:", end = '')
			pass

randomlist = [random.randint(-100,100) for k in range(lenlist)]

print ()
print ('random integer list: ', ' | '.join('{}'.format(n) for n in randomlist))
print()
input('{:-^60}'.format('press Enter to continue'))


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print ()
print('{:*^60}\n'.format('Homework N2. Level: Normal. Task 4.'))
print ()

print ("Please, Enter lenght of random list:", end = '')

while True:
		lenlist2 = input ()
		try:
			lenlist2 = int(lenlist2)
			break
		except ValueError:
			print ("Please, be carefully, it must be an Integer number, enter lenght:", end = '')
			pass

randomlist2 = [random.randint(-5,5) for r in range(lenlist2)]
list1 = list(set(randomlist2))
list2 = [z for z in randomlist2 if randomlist2.count(z) == 1]

print(randomlist2)
print(list1)
print(list2)