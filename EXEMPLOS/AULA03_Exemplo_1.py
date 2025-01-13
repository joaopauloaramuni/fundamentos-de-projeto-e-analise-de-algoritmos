# Busca Linear
# Melhor Caso: O(1) -> O elemento está na primeira posição da lista.
# Caso Médio: O(n) -> O elemento está em uma posição aleatória.
# Pior Caso: O(n) -> O elemento não está na lista ou está na última posição.
def sequential_search(arr, target):
    """
    Busca sequencial (força bruta).
    Percorre o array inteiro para encontrar o elemento alvo.

    :param arr: Lista de elementos
    :param target: Elemento a ser procurado
    :return: Índice do elemento encontrado ou -1 se não for encontrado
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Retorna o índice do elemento
    return -1  # Retorna -1 se não for encontrado

# Melhor Caso: O(n^2) -> Sempre será O(n^2) devido à repetição de busca exaustiva.
# Caso Médio: O(n^2) -> Sempre será O(n^2), independentemente da ordem inicial.
# Pior Caso: O(n^2) -> Sempre será O(n^2), independente da entrada inicial.
def sequential_sort(arr):
    """
    Ordenação sequencial (força bruta).
    Ordena o array de forma crescente usando força bruta e pesquisa exaustiva.

    :param arr: Lista de elementos
    :return: Lista ordenada
    """
    sorted_arr = []
    while arr:
        # Encontra o menor elemento da lista
        smallest = arr[0]
        for item in arr:
            if item < smallest:
                smallest = item
        # Remove o menor elemento da lista original e adiciona à ordenada
        arr.remove(smallest)
        sorted_arr.append(smallest)
    return sorted_arr


if __name__ == "__main__":
    lista = [29, 10, 14, 37, 13]
    alvo = 14

    # Busca sequencial
    indice = sequential_search(lista, alvo)
    print(f"Índice do elemento {alvo}: {indice}")

    # Ordenação sequencial
    lista_ordenada = sequential_sort(lista.copy())
    print(f"Lista ordenada: {lista_ordenada}")
