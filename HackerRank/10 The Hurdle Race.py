nk = input().split()
n = int(nk[0])
k = int(nk[1])

ar = input().split()
ar1 = []
for i in ar:
    ar1.append(int(i))

m = max(ar1)

if k > m:
    print('0')
else:
    print(m-k)