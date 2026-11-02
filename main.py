n = int(input("Enter a positive number: "))
list = []
h = 1
for i in range(1, n+1):
    if n%i == 0:
        list.append(i)
for j in list:
    h = h * j
print(h)        
