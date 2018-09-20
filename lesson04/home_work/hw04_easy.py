# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
from random import randint

print('\n')
print('{:*^60}\n'.format('Homework N4. Level: Easy. Task 1.'))

numlist = [randint(0,50) for _ in range(20)]
print (numlist)
sqrlist = [i**2 for i in numlist]
print(sqrlist)

# ------------------------ONE LINE METHOD------------------------------

# sqrlist = [i**2 for i in [randint(0,50) for _ in range(20)]]

# ------------------------ONE LINE METHOD------------------------------

input('Press Enter to continue...')



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('\n')
print('{:*^60}\n'.format('Homework N4. Level: Easy. Task 2.'))



f1 = ['apple', 'orange', 'peach', 'kiwi', 'lemom', 'apricot', 'pineapple']
f2 = ['mango', 'tangerine', 'avocado', 'papaya', 'kiwi', 'orange', 'peach', 'apple']
print (f1)
print (f2)

f3 = [i for i in f1 if i in f2]
print (f3)

input('Press Enter to continue...')
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('\n')
print('{:*^60}\n'.format('Homework N4. Level: Easy. Task 3.'))

numlist = [randint(-0,20) for _ in range(30)]
print (numlist)
sortlist = [i for i in numlist if (i%3==0 and i%4 != 0 and i>0) ]
print(sortlist)



input('Press Enter to continue...')

