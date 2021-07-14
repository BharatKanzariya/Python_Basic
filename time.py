import time
t1 = time.time()
def ran():
    s = 0
    for i in range(1,1000001):
        s = s + i

    t2 = time.time()

    return s

sum = ran()
print(sum)
t2 = time.time()
print(t2-t1)