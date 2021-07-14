nk = input().split()
n = int(nk[0])
k = int(nk[1])

ar = input().split()
count = 0

for i in range(n-1):
    for j in range(i+1,n):
        t = int(ar[i]) + int(ar[j])
        if t % k == 0:
            count += 1

print(count)