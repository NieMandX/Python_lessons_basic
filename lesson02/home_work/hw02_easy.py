# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# Homework N2. Level: Easy. Task 1.
print('\n'*3)
print('{:*^60}\n'.format('Homework N2. Level: Easy. Task 1.'))
fruits = ['apple','banana','kiwi','watermelon','orange','kiwi', 'apple']
number = 1
for fruit in fruits:
    print ("{}. {:>10}".format(number,fruit))
    number += 1
print()
input('{:-^60}'.format('press Enter to continue'))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Homework N2. Level: Easy. Task 2.

print('\n'*2)
print('{:*^60}\n'.format('Homework N2. Level: Easy. Task 2.'))

fruits = ['apple', 'apple', 'banana','orange', 'watermelon','kiwi', 'apple']
firms = ['apple', 'microsoft', 'IBM', 'amazon', 'orange']
a = 0
print ('fruits list: ', ' | '.join('{}'.format(fruit) for fruit in fruits))
print ('IT corporations: ',' | '.join('{}'.format(firm) for firm in firms))

for firm in firms:
    while firm in fruits:
        a += 1
        fruits.remove(firm)

print ()
print ('fruits list after removing items: ', ' | '.join('{}'.format(fruit) for fruit in fruits))

print()
input('{:-^60}'.format('press Enter to continue'))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


# Homework N2. Level: Easy. Task 3.

print('\n'*2)
print('{:*^60}\n'.format('Homework N2. Level: Easy. Task 3.'))

numbers1 = [i for i in range(1,100)]
numbers2 = []
for j in numbers1:
	if j%2 == 0:
		numbers2.append(j/4)
	else:
		numbers2.append(j*2)

print('\n'*2)
print (' | '.join('{}'.format(number) for number in numbers1))
print (' | '.join('{}'.format(number) for number in numbers2))

