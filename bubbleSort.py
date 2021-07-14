
def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t


arr = [7,6,5,4,3,2]
bubble(arr)

print(arr)