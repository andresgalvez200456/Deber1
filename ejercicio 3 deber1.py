def func1(n):
    A = range(0,n)
    sum = 0
    i = 0
    for x in A[i:]:  #esto se ejecuta n veces    O(n)
        i += 1
        for j in range(i, len(A)):  # esto se ejecuta n-i veces     #loop anidado  for dentro de otro for    O(n)
            y = A[j]
            k = j
            while k < len(A):  #esto se ejecuta (n - 1 - k ) / 2      O(logn)
                z = A[k]
                k = 2*k
                if x + y <= z:
                    sum += 1
    return sum
#n * n * logn 
#n^2 * logn 

print(func1(100))