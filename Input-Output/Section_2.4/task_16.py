# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

# Формат входных данных
# На вход программе подаётся целое число.

# Формат выходных данных
# Программа должна вывести текст согласно условию задачи.

a = int(input())
b = int(a + 1)
c = int(a - 1)
print('Следующее за числом ', a, 'число: ', b)
print('Для числа ',a ,'предыдущее число:', c )
