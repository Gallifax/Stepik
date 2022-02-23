total = 0 
from math import log 
n = int(input())
for i in range(0, n) :
    num = 1 / (i + 1)
    total = total + num
    lg = log(n)
print(total - lg)
