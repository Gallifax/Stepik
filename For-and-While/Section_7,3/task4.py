total = 0
n = int(input())
for i in range(1, n + 1) :
    m = ( i ** 2 ) % 10
    if m == 2 or m == 5 or m == 8 :
        total = total  + i             
print(total) 

        
