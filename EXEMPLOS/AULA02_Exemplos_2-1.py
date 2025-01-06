# Exemplo 1 - Algoritmos Polinomiais
# Complexidade assintótica: O(n)
def soma_vetor(arr):
    soma = 0
    for elemento in arr:
        soma += elemento
    return soma

# Exemplo 2 - Algoritmos Polinomiais
# Complexidade assintótica: O(n^2)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exemplo 3 - Algoritmos Exponenciais
# Complexidade assintótica: O(2^n)
def soma_subconjuntos(arr, soma):
    if soma == 0:
        return True
    if not arr:
        return False
    return (soma_subconjuntos(arr[1:], soma - arr[0]) or
            soma_subconjuntos(arr[1:], soma))

# Exemplo 4 - Algoritmos Exponenciais
# Complexidade assintótica: O(2^n)
def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    torres_de_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mover disco {n} de {origem} para {destino}")
    torres_de_hanoi(n-1, auxiliar, destino, origem)

def main():
    # Exemplo 1: Soma de Elementos em um Vetor (Polinomial, O(n))
    print("Exemplo 1: Soma de Elementos em um Vetor")
    vetor = [1, 2, 3, 4, 5]
    resultado_soma = soma_vetor(vetor)
    print(f"Vetor: {vetor}")
    print(f"Soma dos elementos: {resultado_soma}")
    print()

    # Exemplo 2: Ordenação por Seleção (Polinomial, O(n^2))
    print("Exemplo 2: Ordenação por Seleção")
    vetor_desordenado = [64, 25, 12, 22, 11]
    print(f"Vetor antes da ordenação: {vetor_desordenado}")
    vetor_ordenado = selection_sort(vetor_desordenado)
    print(f"Vetor após a ordenação: {vetor_ordenado}")
    print()

    # Exemplo 3: Soma de Subconjuntos (Exponencial, O(2^n))
    print("Exemplo 3: Soma de Subconjuntos")
    conjunto = [3, 34, 4, 12, 5, 2]
    alvo = 9
    print(f"Conjunto: {conjunto}")
    print(f"Soma alvo: {alvo}")
    existe_soma = soma_subconjuntos(conjunto, alvo)
    print(f"Existe subconjunto com soma {alvo}? {'Sim' if existe_soma else 'Não'}")
    print()

    # Exemplo 4: Torres de Hanói (Exponencial, O(2^n))
    print("Exemplo 4: Torres de Hanói")
    num_discos = 3
    print(f"Resolvendo Torres de Hanói para {num_discos} discos:")
    torres_de_hanoi(num_discos, 'Origem', 'Destino', 'Auxiliar')

# Chamando a função main
if __name__ == "__main__":
    main()
