# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

# Формат входных данных
# На вход программе подаются три целых числа.

# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.

# Примечание. Если положительных чисел нет, то следует вывести 0.

a = int(input())
b = int(input())
c = int(input())
 
sum = 0;
if a > 0:
    sum += a
if b > 0:
    sum += b
if c > 0:
    sum += c
print(sum)
