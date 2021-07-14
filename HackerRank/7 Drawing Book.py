n = int(input())
p = int(input())
ar = []

for i in range(1,n+1):
    ar.append(i)

m = n // 2
ar1 = ar[0:m]
ar2 = ar[m:]

if p <= m:
    ct = 0
    for j in ar1:
        if j % 2 != 0:
            if j == p:
                print(ct)
                break
            else:
                ct += 1
        else:
            if j == p:
                print(ct)
else:
    ct = 0
    for j in reversed(ar2):
        if j % 2 == 0:
            if j == p:
                print(ct)
                break
            else:
                ct += 1
        else:
            if j == p:
                print(ct)
