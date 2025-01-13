def fibonacci_iterativo(n):
    """
    Calcula o n-ésimo número de Fibonacci utilizando programação dinâmica (Bottom-Up).

    :param n: O índice do número de Fibonacci a ser calculado (n >= 0)
    :return: O n-ésimo número de Fibonacci
    """
    # Caso base: Fibonacci de 0 e 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Inicializa os dois primeiros números da sequência
    fib_prev = 0  # F(0)
    fib_curr = 1  # F(1)

    # Calcula os próximos números de Fibonacci iterativamente
    for i in range(2, n + 1):
        fib_next = fib_prev + fib_curr  # F(n) = F(n-1) + F(n-2)
        fib_prev = fib_curr  # Atualiza F(n-2)
        fib_curr = fib_next  # Atualiza F(n-1)

    return fib_curr


if __name__ == "__main__":
    # Exemplo de uso
    n = 10  # Número de Fibonacci a ser calculado
    resultado = fibonacci_iterativo(n)
    print(f"O {n}-ésimo número de Fibonacci é: {resultado}")
