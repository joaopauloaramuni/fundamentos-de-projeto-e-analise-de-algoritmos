import time

# Cálculo da Soma
# Melhor Caso: O(1) -> O Python usa otimizações internas para somar números rapidamente.
# Caso Médio: O(n) -> Soma é iterativa em sistemas menos otimizados.
# Pior Caso: O(n) -> Entrada grande requer mais iterações.
def soma_numeros(n):
    return sum(range(n))

def testar_soma_numeros():
    valores = [10**5, 10**6, 10**7, 10**8]  # Diferentes valores de n
    for valor in valores:
        print(f"\nCalculando soma de 0 até {valor}...")
        inicio = time.time()  # Início da medição
        soma_numeros(valor)
        fim = time.time()  # Fim da medição
        print(f"Tempo de cálculo: {fim - inicio:.5f} segundos")

if __name__ == "__main__":
    testar_soma_numeros()
