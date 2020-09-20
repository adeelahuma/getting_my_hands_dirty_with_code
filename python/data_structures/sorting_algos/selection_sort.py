

arr = [4,5,2,3,1]
print ('unsorted', arr)

for i in range(len(arr)):

    min_idx = i
    for j in range(i+1, len(arr)):

        if arr[min_idx] > arr[j] :
            min_idx = j

    #arr[i] = min_elem
    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp

print('sorted', arr)
