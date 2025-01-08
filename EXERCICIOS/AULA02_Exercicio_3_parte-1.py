import itertools

def tsp_brute_force(distances):
    """
    Função que resolve o problema do caixeiro viajante usando força bruta.
    :param distances: matriz de distâncias entre as cidades.
    :return: menor custo e rota correspondente.
    """
    n = len(distances)  # Quantidade de cidades
    cities = range(n)  # Lista de índices das cidades

    # Gerar todas as permutações possíveis de rotas
    all_routes = itertools.permutations(cities)
        
    min_cost = float('inf')
    best_route = None

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
    Função principal para testar o algoritmo de força bruta no problema do caixeiro viajante.
    """
    # Exemplo de matriz de distâncias entre 4 cidades
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    min_cost, best_route = tsp_brute_force(distances)

    print("Menor custo:", min_cost)
    print("Melhor rota:", best_route)

# Executa o programa
if __name__ == "__main__":
    main()
