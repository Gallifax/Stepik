# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:

# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, который получится в результате.

# Формат входных данных
# На вход программе подаются две строки, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.

a = str(input())
b = str(input())

if a == b and ((a == 'красный' or a == 'синий' or a == 'желтый') and (b == 'красный' or b == 'синий' or b == 'желтый')) :
    print(a)
elif (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный') : 
    print('фиолетовый')
elif (a == 'желтый' and b == 'синий') or (a == 'синий' and b == 'желтый') :
    print('зеленый')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный') :
    print('оранжевый')
else : 
    print('ошибка цвета')
