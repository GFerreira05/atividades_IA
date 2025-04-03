"""
Busca Binária
"""


def search(array, start, end, key):
    while start <= end:
        #TODO : dividir um array no meio
        mid = start + (end - start) // 2

        if array[mid] == key:
            return mid
        elif array[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return "Elemento não encontrado"


# Problema: Array não ordenado representa um problema
# para a Busca binária
# array = [18,14,24,21,38,4,6,9,13]

array = [4,6,9,13,14,18,21,24,38]
key = 180

result = search(array, 0, len(array) - 1, key)
print(result)