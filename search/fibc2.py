def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

    
for n in range(30):
    print(fib(n), end = " ")