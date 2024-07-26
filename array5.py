n = int(input())
c = 0
a = 0
b = 1
myList = [0, 1]

for i in range(n - 2):
    myList.append(a + b)
    c = b
    b = a + b
    a = c
print(myList)