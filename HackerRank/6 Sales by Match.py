n = int(input())
ar = input().split()
ar1 = set(ar)

time = []

for i in ar1:
    ct = 0
    for j in ar:
        if int(i) == int(j):
            ct += 1
    time.append(ct)

sum = 0
for k in time:
    t = k // 2
    sum = sum + t

print(sum)
