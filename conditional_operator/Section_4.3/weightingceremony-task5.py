# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:

# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

# Формат входных данных
# На вход программе подаётся одно целое число.


mass = int(input())

if mass < 60 :
    print('Легкий вес')
elif 60 <= mass < 64 :
    print('Первый полусредний вес')
else : 
    print('Полусредний вес')
