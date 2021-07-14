for i in range(80,83):
    for j in range(i,83):
        if i <= j:
            print(chr(j),end=' ')
        else:
            print(end=' ')
    print()