"""
Exemplo da estratégia da Divisão e  Conquista.
"""


def merge_sort(elements: list) -> list:
    """
    Função que recebe uma lista não ordena, então
    usando o conceito de "divisão e consquista" fará
    a divisão da lista em sublista, até que reste
    somente 1 elemento na lista. Ao mesmo tempo fica
    responsavel por invocar a função merge, que irá
    juntar os elementos de forma ordenada
    """
    #Caso base = uma lista com um elemento
    if len(elements) == 1:
        return elements

    #Encontrar o meio da lista(divisão inteira)
    mid = len(elements) // 2

    #Dividir a lista
    first = elements[:mid]
    second = elements[mid:]

    #Caso recursivo - chamar a função até atingir caso base
    first_half = merge_sort(first)
    second_half = merge_sort(second)

    #Ordenar e retornar a lista
    return merge(first_half, second_half)


def merge(first: list, second: list):
    """
    Função que junta as listas de forma ordenada.
    """
    index1 = index2 = 0
    elements = []

    while index1 < len(first) and index2 < len(second):
        if first[index1] < second[index2]:
            elements.append(first[index1])
            index1 += 1
        else:
            elements.append(second[index2])
            index2 += 1

    while index1 < len(first):
        elements.append(first[index1])
        index1 += 1

    while index2 < len(second):
        elements.append(second[index2])
        index1 += 1

    return elements
            

elements = [10,1,20,3,5,2,18,0]
print(merge_sort(elements))
