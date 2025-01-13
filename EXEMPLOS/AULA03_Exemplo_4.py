def insertion_sort(arr):
    """
    Ordena um array usando o método Insertion Sort (Decrementar para Conquistar).

    :param arr: Lista de elementos a ser ordenada
    :return: Lista ordenada
    """
    for i in range(1, len(arr)):
        # Pega o elemento atual
        key = arr[i]
        j = i - 1

        # Move os elementos maiores que a chave uma posição para frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere a chave na posição correta
        arr[j + 1] = key

    # Melhor Caso: O(n) -> A lista já está ordenada.
    # Caso Médio: O(n^2) -> Aproximadamente metade das comparações e movimentações ocorrem.
    # Pior Caso: O(n^2) -> A lista está em ordem inversa, exigindo movimentações máximas.
    return arr


def binary_search(arr, target, low, high):
    """
    Procura por um elemento em uma lista ordenada usando Binary Search (Decrementar para Conquistar).

    :param arr: Lista ordenada
    :param target: Elemento a ser procurado
    :param low: Índice inicial da busca
    :param high: Índice final da busca
    :return: Índice do elemento encontrado ou -1 se não encontrado
    """
    # Caso base: Elemento não encontrado
    if low > high:
        return -1

    # Encontra o meio do array
    mid = (low + high) // 2

    if arr[mid] == target:
        # Caso base: Elemento encontrado
        return mid
    elif arr[mid] > target:
        # Reduz a busca para a metade inferior
        return binary_search(arr, target, low, mid - 1)
    else:
        # Reduz a busca para a metade superior
        return binary_search(arr, target, mid + 1, high)

    # Melhor Caso: O(1) -> O elemento está no meio do array.
    # Caso Médio: O(log n) -> A cada passo, reduzimos a lista pela metade.
    # Pior Caso: O(log n) -> Quando o elemento está ausente ou na última divisão.


if __name__ == "__main__":
    # Testando Insertion Sort
    lista_insertion = [12, 11, 13, 5, 6]
    print(f"Lista original (Insertion Sort): {lista_insertion}")
    lista_ordenada = insertion_sort(lista_insertion)
    print(f"Lista ordenada (Insertion Sort): {lista_ordenada}")

    print()

    # Testando Binary Search
    lista_binary = [2, 3, 4, 10, 40]
    alvo = 10
    print(f"Lista ordenada (Binary Search): {lista_binary}")
    print(f"Alvo: {alvo}")
    resultado = binary_search(lista_binary, alvo, 0, len(lista_binary) - 1)
    if resultado != -1:
        print(f"Elemento encontrado no índice: {resultado}")
    else:
        print("Elemento não encontrado.")
