import heapq  # Para usar a fila de prioridade (min-heap)

def dijkstra(graph, start):
    """
    Implementação do Algoritmo de Dijkstra para encontrar os caminhos mais curtos em um grafo.

    :param graph: Dicionário representando o grafo (vértices e suas arestas com pesos).
    :param start: Vértice inicial.
    :return: Dicionário com as menores distâncias de 'start' para todos os outros vértices.
    """
    # Dicionário para armazenar as menores distâncias
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Distância do vértice inicial para ele mesmo é 0

    # Fila de prioridade para processar os vértices pelo menor custo
    priority_queue = [(0, start)]  # Tupla (distância, vértice)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignora se a distância na fila for maior que a conhecida
        if current_distance > distances[current_vertex]:
            continue

        # Atualiza as distâncias dos vizinhos
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Se uma distância menor for encontrada, atualiza
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    # Exemplo de grafo representado como um dicionário
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 6},
        'C': {'A': 4, 'B': 2, 'D': 3},
        'D': {'B': 6, 'C': 3}
    }
    start_vertex = 'A'

    # Executa o algoritmo de Dijkstra
    shortest_paths = dijkstra(graph, start_vertex)

    # Exibe os caminhos mais curtos
    print(f"Menores distâncias a partir do vértice '{start_vertex}':")
    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")
