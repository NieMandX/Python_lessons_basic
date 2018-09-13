# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	a = [1,1]
	for i in range(n-1):
		a[i%2] = a[i%2]+a[(i-1)%2]
	if not i%2:
		a.reverse()
	for i in range(1,m-n+1):
		a.append(a[i]+a[i-1])
	if n == m:
		a.pop(i-1)
	return (a)

print(fibonacci(6,15))
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
	n = 1 
	while n < len(origin_list):
		for i in range(len(origin_list)-n):
			if origin_list[i] > origin_list[i+1]:
				origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
		n += 1
	return (origin_list)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_map (f,i):
	return [k for k in i if f(k)]

a = [h for h in range(50)]
print (a)
print (my_map(lambda n:n**.5 == int(n**.5),a))
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def Parallelogram (a,b,c,d):
	if (a[0] + c[0] == b[0] + d[0] and a[1] + c[1] == b[1] + d[1]):
		return True
	else:
		return False
a =(0,0)
b =(10,20)
c =(60,20)
d =(50,0)
print (Parallelogram (a,b,c,d))
a =(14,0)
b =(35,20)
c =(60,70)
d =(50,20)
print (Parallelogram (a,b,c,d))
