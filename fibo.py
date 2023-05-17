def fib(n):
    if n < 0:
         return None
    if n < 2:
        return 1

    elem_1 = elem_2 = 1
    suma = 0
    for i in range(2, n + 1):
        suma = elem_1 + elem_2
        elem_1, elem_2 = elem_2, suma
    return suma


for n in range(1, 100): # test
    print(n, "->", fib(n), "->",fib(n) / fib(n-1))


#float(fib(n-1)) / float(fib(n))
