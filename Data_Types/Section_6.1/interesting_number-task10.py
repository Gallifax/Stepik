# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

# Формат входных данных
# На вход программе подается целое трехзначное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())
num1 = (n // 100) % 10
num2 = (n // 10) % 10
num3 = n % 10
if max(num1, num2, num3) - min(num1, num2, num3) == (num1 + num2 + num3) - (max(num1, num2, num3) + min(num1, num2, num3)) :
    print('Число интересное')
else :
    print('Число неинтересное')
