# Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.

# Формат входных данных
# На вход программе подаётся целое число – количество минут.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.


n = int(input())
m = n // 60
b = n % 60 
print(f"{n} мин - это {m} час {b} минут. ")
