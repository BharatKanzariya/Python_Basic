"""
short program
for i in range(1,101):
    if i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue

    print(i)
"""
i=1
while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
        i = i+1
    else:
        print(i)
        i = i+1
