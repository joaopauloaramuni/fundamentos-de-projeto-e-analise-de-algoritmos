# 1. Pesquisa: Encontrar um elemento (𝑂(𝑛))
def encontrar_elemento(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
    return False

# 2. Seleção: Encontrar o menor número (𝑂(𝑛))
def menor_numero(lista):
    if not lista:  # Retorna None se a lista estiver vazia
        return None
    menor = lista[0]
    for item in lista[1:]:
        if item < menor:
            menor = item
    return menor

# 2. Seleção: Encontrar o menor número (𝑂(𝑛))
def selecionar_pares(lista):
    resultado = []
    for numero in lista:
        if numero % 2 == 0:
            resultado.append(numero)
    return resultado

# 3. Ordenação: Bubble Sort (𝑂(𝑛²) no caso médio)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Troca os elementos de lugar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# 3. Ordenação: Quick Sort (𝑂(𝑛 log 𝑛) no caso médio)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)

# 3. Ordenação: Merge Sort (𝑂(𝑛 log 𝑛) no caso médio)
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Divisão da lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    # Combinação (merge) diretamente na mesma função
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# Função principal (main)
def main():
    lista = [42, 15, 23, 8, 4, 16]
    print("Lista original:", lista)

    # Pesquisa
    print("\n# Pesquisa")
    elemento = 42
    print(f"Elemento {elemento} está na lista?", encontrar_elemento(lista, elemento))
    elemento = 100
    print(f"Elemento {elemento} está na lista?", encontrar_elemento(lista, elemento))

    # Seleção: Menor número
    print("\n# Seleção: Menor número")
    print("Menor número na lista:", menor_numero(lista))

    # Seleção: Números pares
    print("\n# Seleção: Números pares")
    print("Números pares na lista:", selecionar_pares(lista))

    # Ordenação Bubble Sort
    print("\n# Ordenação: Bubble Sort")
    # Usar uma cópia para não alterar a lista original
    lista_bubble = bubble_sort(lista.copy())
    print("Lista ordenada com Bubble Sort:", lista_bubble)
    
    # Ordenação: Quick Sort
    print("\n# Ordenação: Quick Sort")
    lista_quick = quick_sort(lista.copy())
    print("Lista ordenada com Quick Sort:", lista_quick)
    
    # Ordenação: Merge Sort
    print("\n# Ordenação: Merge Sort")
    lista_merge = merge_sort(lista.copy())
    print("Lista ordenada com Merge Sort:", lista_merge)

# Executar o programa principal
if __name__ == "__main__":
    main()
