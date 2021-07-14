n = int(input())
ar = input().split()

how = []

a = 0
b = 0
c = 0
d = 0
e = 0
for i in ar:
    if int(i) == 1:
        a += 1
    elif int(i) == 2:
        b += 1
    elif int(i) == 3:
        c += 1
    elif int(i) == 4:
        d += 1
    elif int(i) == 5:
        e += 1

how.append(a)
how.append(b)
how.append(c)
how.append(d)
how.append(e)

maxv = max(how)

for j in range(100000):
    if how[j] == maxv:
        print(j + 1)
        break