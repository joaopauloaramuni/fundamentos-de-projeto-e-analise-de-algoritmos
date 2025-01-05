import time

# Fatorial Iterativo
# Melhor Caso: O(n) -> Precisa iterar todos os números de 1 até n.
# Caso Médio: O(n) -> Não há variação na complexidade, pois depende linearmente de n.
# Pior Caso: O(n) -> Sempre executa n iterações.
def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Fatorial Recursivo
# Melhor Caso: O(1) -> Para n = 0 ou n = 1, o resultado é retornado imediatamente.
# Caso Médio: O(n) -> Todas as chamadas recursivas são necessárias até n = 1.
# Pior Caso: O(n) -> A profundidade da recursão é proporcional a n.
def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

# Função para medir o tempo de execução
def medir_tempo(func, n):
    inicio = time.time()
    resultado = func(n)
    fim = time.time()
    return resultado, fim - inicio

# Função principal
def main():
    n = 50  # Número para o qual o fatorial será calculado
    print(f"Calculando o fatorial de {n}...\n")

    # Fatorial Iterativo
    resultado_iterativo, tempo_iterativo = medir_tempo(fatorial_iterativo, n)
    print(f"Fatorial (Iterativo): {resultado_iterativo}")
    print(f"Tempo de execução (Iterativo): {tempo_iterativo:.5f} segundos\n")

    # Fatorial Recursivo
    resultado_recursivo, tempo_recursivo = medir_tempo(fatorial_recursivo, n)
    print(f"Fatorial (Recursivo): {resultado_recursivo}")
    print(f"Tempo de execução (Recursivo): {tempo_recursivo:.5f} segundos\n")

if __name__ == "__main__":
    main()
