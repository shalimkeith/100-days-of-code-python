even = list(range (0, 100, 2)) 
even.append(100)
even[0] = 1
print(sum(even))

total = 0
for number in range(2,100,2):
    total += number 
print(total)

total2=0
for number in range (1,101):
    if number % 2 == 0:
        total2 += number
print(total2)