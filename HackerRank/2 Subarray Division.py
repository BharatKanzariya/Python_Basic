"""
1'st types of code
"""
n = int(input())
ar = input().split()
dm = input().split()
d = int(dm[0])
m = int(dm[1])

i = 0
count = 0
if n == 1:
    while i < n:
        sm = 0
        j = 0
        while j < m:
            sm = sm + int(ar[i+j])
            j = j + 1
        if sm == d:
            count += 1
        i += 1
else:
    while i < n-m+1:
        sm = 0
        j = 0
        while j < m:
            sm = sm + int(ar[i+j])
            j = j + 1
        if sm == d:
            count += 1
        i += 1

print(count)

"""
2nd types of code

n = int(input())
ar = input().split()
dm = input().split()
d = int(dm[0])
m = int(dm[1])

count = 0
if n == 1:
    for i in range(n):
        sm = 0
        j = 0
        while j < m:
            sm = sm + int(ar[i+j])
            j += 1
        if sm == d:
            count += 1
else:
    for i in range(n-m+1):
        sm = 0
        j = 0
        while j < m:
            sm = sm + int(ar[i+j])
            j += 1
        if sm == d:
            count += 1

print(count)
"""