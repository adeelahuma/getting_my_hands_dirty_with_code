# edge cases :
# all positive
# all negative

arr = [13, 10, 21, 20] # 1
#arr = [6, 3, 4, 5] # 1
#arr = [8, 5, 11, 4, 6] # 2
#arr = [2,4,6,8]
#arr = [1,3,5,7]

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,0]

odd_idx = []
count_moves = 0

for i in range(len(arr)):

    if arr[i] % 2 != 0 :
        odd_idx.append(i)

mid_idx = int(len(arr)/2)
#mid_idx =  mid_idx-1 if len(arr)% 2 == 0 else mid_idx
#print(odd_idx)
if not(len(odd_idx) == 0 or len(odd_idx) == len(arr)):

    for i in range(mid_idx, len(arr)):

        #swap scenario
        if arr[i]% 2 == 0 :

            # pop the index of first odd element
            j = odd_idx[0]

            if j < i:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                count_moves +=1

                odd_idx.pop(0)

print(count_moves)
print(arr)


def countCounterfeit(serialNumber):
    # Write your code here
    valid_denominations = [10, 20, 50, 100, 200, 500, 1000]
    denomination_sum = 0

    # tokenize parts of each serial number
    # validate each part
    # if valid serial number, extract the denomination value

    for sample in serialNumber:
        # print(sample, len(sample))
        if len(sample) >= 10 and len(sample) <= 12:

            sect_1 = sample[0:3] # all distinct uppercase english letters
            sect_2 = sample[3: 7] # year , so only numbers between 1900 - 2019
            sect_3 = sample[7: len(sample)-1] # denomination of given type
            sect_4 = sample[-1]  # uppercase english letter

            # print(sect_1, sect_2, sect_3, sect_4)

            if (sect_1.isalpha() and sect_1.isupper() and len(set(sect_1)) == 3) and (sect_2.isnumeric() and (int(sect_2) >= 1900 and int(sect_2) <= 2019)) and (sect_3.isnumeric() and (int(sect_3) in valid_denominations))and (sect_4.isalpha() and sect_4.isupper()):
                denomination_sum += int(sect_3)

    # print(denomination_sum)

    return denomination_sum
