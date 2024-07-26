a = int(input())
d = int(input())

n = int(input())
myList = []

for i in range(1, n + 1):
    myList.append(a*d**i)

print(myList)