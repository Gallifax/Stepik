# Напишите программу, которая определяет наименьшее из четырёх чисел.

# Формат входных данных
# На вход программе подаётся четыре целых числа.

# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
min = a
if min > b:
    min = b
if min > c:
    min = c
if min > d:
    min = d
print(min)
