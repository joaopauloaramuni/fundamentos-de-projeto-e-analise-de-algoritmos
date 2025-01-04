import time

# Busca Binária
# Melhor Caso: O(1) -> O elemento está no meio da lista logo na primeira tentativa.
# Caso Médio: O(log n) -> A lista é dividida repetidamente até encontrar o elemento.
# Pior Caso: O(log n) -> O elemento está em uma extremidade ou não está presente.
def busca_binaria(lista, elemento):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

def testar_busca_binaria():
    tamanhos = [10000, 50000, 100000, 500000]
    for tamanho in tamanhos:
        lista = sorted([i for i in range(tamanho)])  # Lista ordenada
        elemento = lista[tamanho // 2]  # Escolhe um elemento no meio
        print(f"\nBuscando elemento em lista de tamanho {tamanho}...")
        inicio = time.time()
        busca_binaria(lista, elemento)
        fim = time.time()
        print(f"Tempo de busca: {fim - inicio:.5f} segundos")

if __name__ == "__main__":
    testar_busca_binaria()
