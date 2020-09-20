arr = [6,5,4,3,2,1]

print('unordered', arr)

for i in range(len(arr)):

    temp = arr[i]
    blank_idx = i

    while blank_idx > 0 :

        if temp < arr[blank_idx-1]  :
            arr[blank_idx] = arr[blank_idx-1]

        blank_idx -= 1
    arr[blank_idx] = temp


print('sorted', arr)

