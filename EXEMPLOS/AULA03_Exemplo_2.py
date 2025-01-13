def transform_to_last_digit_and_rest(n):
    """
    Transforma o número separando o último dígito e o restante.

    :param n: Número inteiro
    :return: Tupla (último dígito, restante do número)
    """
    # Último dígito (n % 10) e restante (n // 10)
    return n % 10, n // 10


def sum_of_digits_recursive(n):
    """
    Calcula a soma dos dígitos de um número de forma recursiva.
    Utiliza a estratégia de transformação e redução.

    :param n: Número inteiro
    :return: Soma dos dígitos
    """
    # Caso base: Se n é menor que 10, retorna ele mesmo (não há mais dígitos a somar)
    # Melhor Caso: O(1) -> Quando o número já é um único dígito (n < 10).
    if n < 10:
        return n

    # Transformação: Separa o último dígito e o restante
    last_digit, remaining = transform_to_last_digit_and_rest(n)

    # Redução: Soma o último dígito com a soma recursiva dos dígitos restantes
    # Caso Médio: O(d) -> Onde d é o número de dígitos no número.
    # Pior Caso: O(d) -> Todos os dígitos precisam ser processados recursivamente.
    return last_digit + sum_of_digits_recursive(remaining)


if __name__ == "__main__":
    numero = 12345
    print(f"Número: {numero}")

    # Soma dos dígitos recursivamente
    soma = sum_of_digits_recursive(numero)
    print(f"Soma dos dígitos: {soma}")
