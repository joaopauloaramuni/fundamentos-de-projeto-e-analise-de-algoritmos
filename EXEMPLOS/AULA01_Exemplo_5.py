import time

# Fibonacci Iterativo
# Melhor Caso: O(1) -> Para n = 0 ou n = 1, o resultado é retornado imediatamente.
# Caso Médio: O(n) -> Não há variação na complexidade, pois depende linearmente de n.
# Pior Caso: O(n) -> Sempre executa n iterações.
def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    anterior, atual = 0, 1  # Inicializando os dois primeiros números da sequência
    
    for _ in range(2, n + 1):  # Itera de 2 até n
        proximo = anterior + atual  # Soma dos dois números anteriores
        anterior, atual = atual, proximo  # Atualiza os valores
    
    return atual  # Retorna o n-ésimo número da sequência

# Fibonacci Recursivo
# Melhor Caso: O(1) -> Para n = 0 ou n = 1, o resultado é retornado imediatamente.
# Caso Médio: O(2^n) -> A árvore de chamadas cresce exponencialmente com n > 1.
# Pior Caso: O(2^n) -> Mesmo comportamento exponencial com alta redundância nas chamadas recursivas.
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Fibonacci Recursivo com memoização
# Melhor Caso: O(1) -> Cada valor é calculado apenas uma vez e armazenado.
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
