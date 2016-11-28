import math
import random
import datetime

__author__ = "Денис Азаркин"

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список, элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print('='*40) # Разделитель

a = [2, -5, 8, 9, -25, 25, 4]
# [9, 25, 4]
a = list(filter(lambda x: x == ((x**0.5)**2), a))

for i in range(0, len(a)):
    a[i] = int(math.sqrt(a[i]))

print(a)

print('='*40) # Разделитель
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = datetime.date(2013, 11, 2)
print(date.strftime("%A, %d. %B %Y"))


print('='*40) # Разделитель
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random

n = 10
b = []
for i in range(1, n):
    b.insert(i, random.randint(-100, 100))
print(b)

print('='*40) # Разделитель
# Задача-4: Дан список, заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного
# Например, lst = [1,2,4,5,6,2,5,2], нужно получить lst2 = [1,4,6]

print('Так и не понял как сделать')

# lst = sorted([1, 2, 4, 5, 6, 2, 5, 2])
# lst2 = []

# i = 0

# for i in range(0, len(lst)):
#     if lst[i - 1] & lst[i + 1] != lst[i]:
#         lst2.insert(i, lst[i])
#         print('if', lst2)
#
# print('print', lst2)
# print(lst)
# print('='*40) # Разделитель