# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re
from random import randint

print('\n'*2)
print('{:*^60}\n'.format('Homework N4. Level: Normal. Task 1. Method 1 (without re)'))

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

word = ''
newlist = []
for letter in line:
    if letter.islower():
        word = word+letter
        flag = 1
    elif flag:
        newlist.append(word)
        word = ''
        flag = 0
    else:
        pass
else:
    newlist.append(word)

print (newlist)

print()
input('{:-^60}'.format('press Enter to continue'))

print('\n'*2)
print('{:*^60}\n'.format('Homework N4. Level: Normal. Task 1. Method 2 (with re)'))

newlist_re = re.split(r'[A-Z]+',line)
print (newlist_re)

print()
input('{:-^60}'.format('press Enter to continue'))
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

print('\n'*2)
print('{:*^60}\n'.format('Homework N4. Level: Normal. Task 2. Method 1 (without re)'))

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

new_list2 =[]
flag = 0
l = 0
b = 0
for index in range(len(line_2)):
    if line_2[index].islower():
        if l >= 2 and b >=3:
            new_list2.append(line_2[index-b:index-2])
            l = 0
            b = 0
            flag = 1
        elif flag == 0:
            l = 0
            b = 0
            flag = 1
        else:
            pass
        l = l + 1
    else:
        b = b + 1
        flag = 0
        
print (new_list2)
print()
input('{:-^60}'.format('press Enter to continue'))

print('\n'*2)
print('{:*^60}\n'.format('Homework N4. Level: Normal. Task 2. Method 2 (with re)'))

print ([i.group(1) for i in re.finditer(r'[a-z]{2}([A-Z]+)[A-Z]{2}',line_2)])

print()
input('{:-^60}'.format('press Enter to continue'))
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
print('\n'*2)
print('{:*^60}\n'.format('Homework N4. Level: Normal. Task 2. Method 1 (without re)'))

with open('random.txt', 'w', encoding = 'UTF-8') as f2:
    f2.write(''.join(str (i) for i in [randint(0,9) for _ in range(2500)]))

with open('random.txt', 'r', encoding = 'UTF-8') as f2:
    bignum = (f2.read()) 
    
offset = 0
start = 0
maxstart = 0
maxstarts = []
maxoffset = 0
flag = 0
for index in range(len(bignum)-1):
    if bignum [index] is bignum [index + 1]:
        if flag == 0:
            start = index
            offset = 1
            flag = 1
        else:
            flag = 1
            offset += 1
    else:
        flag = 0
        if offset > maxoffset:
            maxstart = start
            maxoffset = offset
            maxstarts.clear()
            
        elif offset == maxoffset:
            maxstarts.append(start)
            offset = 0
else:
    if offset > maxoffset:
        maxstart = start
        maxoffset = offset
        maxstarts.clear()
            
    elif offset == maxoffset:
        maxstarts.append(start)
       
print (bignum)
print ()
if len(maxstarts):
    for i in range(len(maxstarts)):
        print ('Maximum similar sequence is: {} it start at {}'.format(bignum[maxstarts[i]:maxstarts[i]+maxoffset+1], maxstarts[i]+1))
else:
    print ('Maximum similar sequence is: {} it start at {}'.format(bignum[maxstart:maxstart+maxoffset+1], maxstart+1))
   
