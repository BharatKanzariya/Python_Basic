for i in range(1,500):
    num = i
    sum = 0
    j = 1
    while j < i:
        r = i % j
        if r == 0:
            sum = sum + j
        j = j + 1
    if (num == sum):
        print(num)