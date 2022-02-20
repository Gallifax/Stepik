a, b = int(input()), int(input())
counter = 0

for i in range(a, b + 1) :
    lastNumber = (i **3) % 10

    if lastNumber == 4 or lastNumber == 9:
        counter = counter + 1

print(counter)
