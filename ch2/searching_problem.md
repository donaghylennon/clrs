``
LinearSearch(A, v):

for i = 1 to A.length:
    if A[i] == v:
        return i

return nil
``


Loop invariant:

> At the start of each iteration of the loop, A[1..i-1] does not contain v

Initialization:

When i = 1, A[1..0] is an empty subarray, so it doesn't contain v

Maintenance:

If i-1 == v, then the loop will terminate and we do not get to i,
so it is certain that when the for loop increments i, A[1..i-1] does
not contain i

Termination:

The loop terminates if A[i] == v, so we know that v is in A and i is its
index. Otherwise, the loop will terminate because i == n + 1 and we return nil.
Since we know A[1..i-1] does not contain v, this means
A[1..(n+1)-1] => A[1..n] => A does not contain v
