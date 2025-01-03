import random
import time

# Função Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Testando a performance com listas grandes
def testar_bubble_sort():
    tamanhos = [1000, 5000, 10000, 20000]  # Tamanhos crescentes da lista
    for tamanho in tamanhos:
        lista = [random.randint(0, 1000000) for _ in range(tamanho)]  # Lista aleatória
        print(f"\nOrdenando lista de tamanho {tamanho}...")
        inicio = time.time()  # Início da medição
        bubble_sort(lista)  # Ordenação
        fim = time.time()  # Fim da medição
        print(f"Tempo para ordenar: {fim - inicio:.2f} segundos")

# Executar o teste
if __name__ == "__main__":
    testar_bubble_sort()
