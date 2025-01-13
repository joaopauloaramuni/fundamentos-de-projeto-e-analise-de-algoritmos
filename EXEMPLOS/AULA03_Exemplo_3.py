def quick_sort(arr):
    """
    Ordena um array usando o método Quick Sort (Divisão e Conquista).
    
    :param arr: Lista de elementos a ser ordenada
    :return: Lista ordenada
    """
    # Caso base: Se o array tiver 0 ou 1 elementos, já está ordenado
    # Melhor Caso: O(n log n) -> A partição sempre divide o array ao meio.
    if len(arr) <= 1:
        return arr

    # Divisão: Escolhe o último elemento como pivô
    pivot = arr[-1]

    # Conquista: Particiona o array em menores e maiores que o pivô
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]

    # Combinação: Junta as partes ordenadas com o pivô no meio
    # Caso Médio: O(n log n) -> Divisões equilibradas na maioria das vezes.
    # Pior Caso: O(n^2) -> A partição é altamente desbalanceada (ex.: array já ordenado).
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


def merge_sort(arr):
    """
    Ordena um array usando o método Merge Sort (Divisão e Conquista).
    
    :param arr: Lista de elementos a ser ordenada
    :return: Lista ordenada
    """
    # Caso base: Se o array tiver 0 ou 1 elementos, já está ordenado
    # Melhor Caso: O(n log n) -> Sempre divide o array igualmente.
    if len(arr) <= 1:
        return arr

    # Divisão: Divide o array no meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquista: Resolve cada metade recursivamente
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combinação: Junta as duas metades ordenadas
    # Caso Médio: O(n log n) -> Partições sempre equilibradas.
    # Pior Caso: O(n log n) -> Igual ao caso médio, pois as divisões são sempre iguais.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Combina duas listas ordenadas em uma única lista ordenada.
    
    :param left: Lista ordenada
    :param right: Lista ordenada
    :return: Lista combinada e ordenada
    """
    merged = []
    i = j = 0

    # Junta os elementos das listas, mantendo a ordem
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Adiciona os elementos restantes
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    # Quick Sort
    lista_quick = [10, 7, 8, 9, 1, 5]
    print(f"Lista original (Quick Sort): {lista_quick}")
    lista_ordenada_quick = quick_sort(lista_quick)
    print(f"Lista ordenada (Quick Sort): {lista_ordenada_quick}")

    print()

    # Merge Sort
    lista_merge = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original (Merge Sort): {lista_merge}")
    lista_ordenada_merge = merge_sort(lista_merge)
    print(f"Lista ordenada (Merge Sort): {lista_ordenada_merge}")
