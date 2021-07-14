q = int(input())
arr = []

for i in range(q):
    a = input().split()
    arr.append(a)

for j in arr:
    x = int(j[0])
    y = int(j[1])
    z = int(j[2])
    s1 = abs(z - x)
    s2 = abs(z - y)
    if s1 == s2:
        print('Mouse C')
    elif s1 < s2:
        print('Cat A')
    else:
        print('Cat B')


"""
There is another trick to take 2d array as input in python as following:

size = int(input())
array_input = []
for x in range(size):
    array_input.append([int(y) for y in input().split()])
print(array_input)
"""