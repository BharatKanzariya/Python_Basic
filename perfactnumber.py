import time

t1 = time.time()
a = range(1, 1000)
for j in a:
    num = j
    sum = 0
    for i in range(1, num):
        if (num % i == 0):
            sum = sum + i
    if (sum == num):
        print('perfact number:', sum)

t2 = time.time()
print(t2 - t1)
