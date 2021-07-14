n = int(input())
ar = input().split()

min = int(ar[0])
max = int(ar[0])
min_count = 0
max_count = 0

i = 1
while i < range(ar):
    if int(ar[i]) < min:
        min = int(ar[i])
        min_count += 1
    elif int(ar[i]) > max:
        max = int(ar[i])
        max_count += 1
    i += 1

print(min_count, max_count)