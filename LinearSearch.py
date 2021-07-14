pos = -1

def search(arr,n):

    for i in range (len(arr)):
        if arr[i] == n:
            globals()['pos'] = i
            return True


    return False



lis = [3,8,6,4,6,7,9]
n = 6
if search(lis,n):
    print('Found at', pos+1)
else:
    print('Not found.')