import time

# Fibonacci Iterativo
# Melhor Caso: O(n) -> Precisa iterar n vezes para calcular o valor de Fibonacci.
# Caso Médio: O(n) -> Não há variação na complexidade, pois depende linearmente de n.
# Pior Caso: O(n) -> Sempre executa n iterações.
def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Fibonacci Recursivo
# Melhor Caso: O(2^n) -> Precisa calcular todas as combinações de subproblemas.
# Caso Médio: O(2^n) -> Mesmo para valores médios de n, há grande sobreposição de subproblemas.
# Pior Caso: O(2^n) -> Altíssima redundância nas chamadas recursivas.
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Fibonacci Recursivo com memoização
# Melhor Caso: O(n) -> Cada valor é calculado apenas uma vez e armazenado.
# Caso Médio: O(n) -> A reutilização de resultados evita cálculos redundantes mesmo para valores médios de n.
# Pior Caso: O(n) -> Todos os subproblemas são resolvidos no máximo uma vez, resultando em complexidade linear.
def fibonacci_memoizado(n, memo={}):
    if n in memo:  # Verifica se o resultado já foi calculado
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoizado(n - 1, memo) + fibonacci_memoizado(n - 2, memo)  # Armazena o resultado
    return memo[n]

# Função para medir o tempo de execução
def medir_tempo(func, n):
    inicio = time.time()
    resultado = func(n)
    fim = time.time()
    return resultado, fim - inicio

# Função principal
def main():
    n = 30  # Número para o qual o Fibonacci será calculado
    print(f"Calculando o Fibonacci de {n}...\n")

    # Fibonacci Iterativo
    resultado_iterativo, tempo_iterativo = medir_tempo(fibonacci_iterativo, n)
    print(f"Fibonacci (Iterativo): {resultado_iterativo}")
    print(f"Tempo de execução (Iterativo): {tempo_iterativo:.5f} segundos\n")

    # Fibonacci Recursivo
    resultado_recursivo, tempo_recursivo = medir_tempo(fibonacci_recursivo, n)
    print(f"Fibonacci (Recursivo): {resultado_recursivo}")
    print(f"Tempo de execução (Recursivo): {tempo_recursivo:.5f} segundos\n")
    
    # Fibonacci Recursivo com memoização
    resultado_recursivo, tempo_recursivo = medir_tempo(fibonacci_memoizado, n)
    print(f"Fibonacci (Recursivo) com memoização: {resultado_recursivo}")
    print(f"Tempo de execução (Recursivo) com memoização: {tempo_recursivo:.5f} segundos\n")

if __name__ == "__main__":
    main()
