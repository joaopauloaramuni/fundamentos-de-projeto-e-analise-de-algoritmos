import time

# Verificação de Números Primos
# Melhor Caso: O(1) -> O número é menor que 2 e não é primo.
# Caso Médio: O(sqrt(n)) -> A raiz quadrada de n determina o número de iterações.
# Pior Caso: O(sqrt(n)) -> Verifica múltiplos até √n sem encontrar divisores.
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def testar_primos():
    numeros = [10**6 + 1, 10**6 + 3, 10**6 + 7, 10**6 + 9]
    for numero in numeros:
        print(f"\nVerificando se {numero} é primo...")
        inicio = time.time()
        resultado = eh_primo(numero)
        fim = time.time()
        print(f"Resultado: {resultado}, Tempo de verificação: {fim - inicio:.5f} segundos")

if __name__ == "__main__":
    testar_primos()
