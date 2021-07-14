pos = -1
count = 0

list = []

for i in range(1, 1001):
    list.append(i)


def search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        globals()['count'] += 1
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

n = 530 
if search(list, n):
    print('Found at', pos + 1)
else:
    print('Not Found.')

print(count)