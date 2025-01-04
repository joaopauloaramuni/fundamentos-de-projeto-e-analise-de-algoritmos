import random
import time

# QuickSort
# Melhor Caso: O(n log n) -> A lista é dividida em partes aproximadamente iguais.
# Caso Médio: O(n log n) -> Divisões aleatórias equilibradas na média.
# Pior Caso: O(n^2) -> A lista está ordenada ou desordenada de forma desfavorável.
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

def testar_quicksort():
    tamanhos = [1000, 5000, 10000, 20000]
    for tamanho in tamanhos:
        lista = [random.randint(0, 1000000) for _ in range(tamanho)]
        print(f"\nOrdenando lista de tamanho {tamanho}...")
        inicio = time.time()
        quicksort(lista)
        fim = time.time()
        print(f"Tempo de ordenação: {fim - inicio:.5f} segundos")

if __name__ == "__main__":
    testar_quicksort()
