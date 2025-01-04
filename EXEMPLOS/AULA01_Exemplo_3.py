import random
import time

# Contagem de Ocorrências
# Melhor Caso: O(n) -> O algoritmo percorre toda a lista uma vez para contar.
# Caso Médio: O(n) -> O número de ocorrências não afeta a complexidade.
# Pior Caso: O(n) -> A lista é longa, e o elemento é muito frequente.
def contar_ocorrencias(lista, elemento):
    return lista.count(elemento)

def testar_contagem_ocorrencias():
    tamanhos = [10000, 50000, 100000, 500000]  # Diferentes tamanhos de listas
    for tamanho in tamanhos:
        lista = [random.randint(0, 100) for _ in range(tamanho)]  # Lista aleatória com valores de 0 a 100
        elemento = random.choice(lista)  # Seleciona um elemento presente na lista
        print(f"\nContando ocorrências em lista de tamanho {tamanho}...")
        inicio = time.time()  # Início da medição
        contar_ocorrencias(lista, elemento)
        fim = time.time()  # Fim da medição
        print(f"Tempo para contar: {fim - inicio:.5f} segundos")

if __name__ == "__main__":
    testar_contagem_ocorrencias()
