def Selection(arr):

    for i in range(0,len(arr)):
        minpos = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[minpos]:
                minpos = j

        arr[i],arr[minpos]=arr[minpos],arr[i]
        print(arr)


arr = [7,2,5,4,8,2]
Selection(arr)

print(arr,'final')