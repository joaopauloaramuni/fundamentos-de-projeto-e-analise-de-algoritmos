def generate_permutations(cities):
    """
    Função recursiva para gerar todas as permutações de uma lista de cidades.
    :param cities: Lista de cidades (índices).
    :return: Lista com todas as permutações possíveis.
    """
    def permute(current, remaining, result):
        # Caso base: se não há mais cidades para adicionar
        if not remaining:
            result.append(current)
            return

        # Passo recursivo: tenta cada cidade restante como próximo elemento
        for i in range(len(remaining)):
            next_city = remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]  # Remove a cidade atual
            permute(current + [next_city], new_remaining, result)

    # Inicializa a lista de permutações e chama a função recursiva
    permutations = []
    permute([], cities, permutations)
    return permutations

def tsp_brute_force(distances):
    """
    Função que resolve o problema do caixeiro viajante usando força bruta
    com geração recursiva de permutações.
    :param distances: Matriz de distâncias entre as cidades.
    :return: Menor custo e rota correspondente.
    """
    n = len(distances)  # Quantidade de cidades
    cities = list(range(n))  # Lista de índices das cidades

    # Gerar todas as permutações usando a função recursiva
    all_routes = generate_permutations(cities)
    
    min_cost = float('inf')
    best_route = None

    # Calcular o custo para cada rota
    for route in all_routes:
        cost = 0
        for i in range(n):
            cost += distances[route[i]][route[(i + 1) % n]]  # Ciclo fechado
        if cost < min_cost:
            min_cost = cost
            best_route = route

    return min_cost, best_route

def main():
    """
    Função principal para testar o algoritmo reformulado do problema do caixeiro viajante.
    """
    # Exemplo de matriz de distâncias entre 4 cidades
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    min_cost, best_route = tsp_brute_force(distances)

    print("\nMenor custo:", min_cost)
    print("Melhor rota:", best_route)

# Executa o programa
if __name__ == "__main__":
    main()
