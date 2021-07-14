steps = int(input())
path = input()

ct = valus = 0

for i in path:
    if i == 'U':
        ct += 1
    else:
        ct -= 1
    if ct == 0 and i == 'U':
        valus += 1

print(valus)