Input:
Two arrays of n numbers A = [a1, a2, ..., an], B = [b1,...,bn] where
ai, bi  are in  [0, 1]

Output:
An array of n + 1 numbers C = [c1, ..., cn] where ci in [0, 1]


BinaryAdd(A, B):

C = []
carry = 0
for i = n to 0:
    if A[i] + B[i] + carry == 3:
        C[i+1] = 1
        carry = 1
    elseif A[i] + B[i] + carry == 2:
        C[i+1] = 0
        carry = 1
    elseif A[i] + B[i] + carry == 1:
        C[i+1] = 1
        carry = 0
    else
        C[i+1] = 0

C[i+1] = carry


BinaryAdd(A, B):

C = []
C[A.length+1] = 0
for i = A.length to 0:
    if A[i] + B[i] + C[i] == 3:
        C[i+1] = 1
        C[i] = 1
    elseif A[i] + B[i] + C[i] == 2:
        C[i+1] = 0
        C[i] = 1
    elseif A[i] + B[i] + C[i] == 1:
        C[i+1] = 1
        C[i] = 0
    else
        C[i+1] = 0


