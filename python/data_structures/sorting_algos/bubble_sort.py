

arr = [4,5,2,3,1]
print('unorded', arr)

for j in range(len(arr)):
    for i in range(len(arr)-1):

        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp


print('orded', arr)
