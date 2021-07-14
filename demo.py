n = int(input())
t = []

i = 0
while i < n:
    d = input().split()
    t.append(d)
    i = i+1

f = input()
for i in t:
    if i[0] == f:
        sum = float(i[1])+float(i[2])+float(i[3])
        print(%.2f % sum/3)

