import random
import time

# Busca Linear
# Melhor Caso: O(1) -> O elemento está na primeira posição da lista.
# Caso Médio: O(n) -> O elemento está em uma posição aleatória.
# Pior Caso: O(n) -> O elemento não está na lista ou está na última posição.
def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

def testar_busca_linear():
    tamanhos = [10000, 50000, 100000, 500000]  # Diferentes tamanhos de listas
    for tamanho in tamanhos:
        lista = [random.randint(0, 1000000) for _ in range(tamanho)]  # Lista aleatória
        alvo = random.choice(lista)  # Seleciona um elemento da lista como alvo
        print(f"\nBuscando em lista de tamanho {tamanho}...")
        inicio = time.time()  # Início da medição
        busca_linear(lista, alvo)
        fim = time.time()  # Fim da medição
        print(f"Tempo de busca: {fim - inicio:.5f} segundos")

if __name__ == "__main__":
    testar_busca_linear()
