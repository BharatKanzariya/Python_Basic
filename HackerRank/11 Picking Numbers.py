n = int(input())
ar = input().split()
ar1 = []
for i in ar:
    ar1.append(int(i))

ar1.sort()

maximum = 0
for i in range(n - 1):
    ct = 1
    for j in range(i + 1, n):
        if ar1[j] - ar1[i] <= 1:
            ct += 1
    if ct > maximum:
        maximum = ct
    if maximum > 50:
        break

print(maximum)
