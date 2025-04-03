"""
Exemplo de fibonacci utilizando arquitetura de algoritmo Top-down, com
memorização
"""


def fib(n):
    if n == 0 or n == 1:
        return n

    if memory[n] is not None:
        return memory[n]
    
    memory[n] = fib(n - 1) + fib(n - 2)
    return memory[n]

memory = [None] * 1000
for n in range(40):
    print(fib(n), end = " ")