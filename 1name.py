for r in range(5):
    for c in range(9):
        if (c==0 and r<5) or (c==1 and r%2==0) or (c==2 and r%2==0) or (c==3 and r%2!=0) or (c==5 and r<5) or (r==2 and 5<c<8) or (c==8 and r<5):
            print('*',end='')
        else:
            print(' ',end='')

    print()