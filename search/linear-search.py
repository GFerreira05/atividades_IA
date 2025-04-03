"""
Busca Linear (sem ordenação).
"""

def search(input_list: list, element: int) -> int:
    for index , value in enumerate(input_list):
        if value == element:
            return index


input_list = [3,1,4,6,14]
index = search(input_list, 3)
print(index)
