def contar_positivos(lista_de_listas):
    total_positivos = 0  # Inicializa o contador total
    for sublista in lista_de_listas:  # Laço externo: percorre cada sublista
        for numero in sublista:  # Laço interno: percorre os números da sublista
            if numero > 0:  # Verifica se o número é positivo
                total_positivos += 1  # Incrementa o contador
    return total_positivos  # Retorna o total de números positivos

def main():
    # Exemplo de lista de listas
    lista_de_listas = [
        [1, -2, 3, 4],
        [-5, 6, -7, 8],
        [9, -10, 12, -11]
    ] # Total de números positivos: 7
    
    # Chama a função contar_positivos e armazena o resultado
    total_positivos = contar_positivos(lista_de_listas)
    
    # Exibe o resultado
    print(f"O total de números positivos na lista de listas é: {total_positivos}")

# Chamada ao main
if __name__ == "__main__":
    main()
