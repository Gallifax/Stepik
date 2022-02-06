# Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES», иначе выведите «NO».

# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

# Формат входных данных
# На вход программе подаётся натуральное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) :
    print('YES')
else : 
    print('NO')
