
rows, cols = (4,4)

A = [cols *[1]  for i in range(rows)]
print(A)

B = [cols * [2] for i in range(rows)]
print(B)

C = [cols * [0] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        C[i][j] = A[i][j] + B[i][j]

print(C)        
