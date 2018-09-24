# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import easy

def menu():
    print('---------------------------------')
    print('Select operation 1-4:')
    print('1. Change folder')
    print('2. Active folder list')
    print('3. Delete folder')
    print('4. Create folder')
    print('---------------------------------')
    print('Or press Enter for Quit')
    print('---------------------------------')

    action = input()
    return action


def handler(action):
    while action != '':
    
	    action_item = {
	        '1': easy.my_cd,
	        '2': easy.my_ls,
	        '3': easy.my_rmdir_name,
	        '4': easy.my_mkdir_name
	        }
	    item = None
	    try:
	        if int(action) in range(1, 5):
	            for item, key in action_item.items():
	                if item == action:
	                    key()
	        else:
	            print('"{}" wrong command.'.format(action))

	    except ValueError:
	        print('"{}" wrong command.'.format(action))

	    action = menu()
#    handler(menu()) if input('Enter "y" to continue:') == 'y' else handler('')


handler(menu()) 