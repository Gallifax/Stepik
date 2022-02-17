c1 = input()

c2 = input()

c3 = input()

city_list = [c1, c2, c3]

len_min = 2147483647

len_max = 0

min_city = max_city = ''

for city in city_list:

   if len(city) < len_min:

       min_city = city

       len_min = len(city)

   if len(city) > len_max:

       max_city = city

       len_max = len(city)

print(min_city)

print(max_city)




