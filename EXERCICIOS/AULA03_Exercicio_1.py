def is_safe(board, row, col):
    """
    Verifica se é seguro colocar uma rainha na posição (row, col).
    
    :param board: Tabuleiro atual com as posições das rainhas.
    :param row: Linha para colocar a rainha.
    :param col: Coluna para colocar a rainha.
    :return: True se for seguro, False caso contrário.
    """
    # Verifica a coluna acima
    for i in range(row):
        if board[i] == col:
            return False

    # Verifica a diagonal principal acima
    # zip combina as linhas e colunas correspondentes na diagonal principal.
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Verifica a diagonal secundária acima
    # zip combina as linhas e colunas correspondentes na diagonal secundária.
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_n_queens(board, row, solutions):
    """
    Resolve o problema das N Rainhas utilizando Backtracking.

    :param board: Tabuleiro atual com as posições das rainhas.
    :param row: Linha atual para colocar a rainha.
    :param solutions: Lista para armazenar as soluções encontradas.
    """
    # Caso base: Todas as rainhas foram colocadas
    if row == len(board):
        solutions.append(board[:])  # Adiciona uma cópia da solução
        return

    # Tenta colocar uma rainha em cada coluna da linha atual
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col  # Coloca a rainha na posição (row, col)
            solve_n_queens(board, row + 1, solutions)  # Resolve para a próxima linha
            # Backtracking: Remove a rainha e tenta outra posição
            board[row] = -1


def print_solutions(solutions):
    """
    Imprime as soluções do problema das N Rainhas.
    
    :param solutions: Lista de soluções, cada uma representada por uma configuração do tabuleiro.
    """
    for solution in solutions:
        print("\nTabuleiro:")
        for row in solution:
            line = ['.'] * len(solution)  # Cria uma linha de '.' para casas vazias
            line[row] = 'Q'  # Marca a posição da rainha com 'Q'
            print(" ".join(line))  # Junta a linha em uma string para exibição


if __name__ == "__main__":
    # Configuração inicial
    N = 8  # Tamanho do tabuleiro (8x8 para o problema das 8 rainhas)
    board = [-1] * N  # Inicializa o tabuleiro vazio
    solutions = []  # Lista para armazenar as soluções

    # Resolve o problema
    solve_n_queens(board, 0, solutions)

    # Melhor Caso: O(N!) -> No melhor caso, o algoritmo encontra uma solução válida rapidamente,
    # mas ainda precisa verificar pelo menos parte do espaço de busca. Mesmo nesse caso,
    # devido à natureza combinatória do problema, as tentativas iniciais exigem verificações
    # sistemáticas para cada rainha. O número de verificações diminui significativamente
    # em relação ao pior caso, mas ainda está relacionado a N!.

    # Caso Médio: O(N!) -> No caso médio, o algoritmo precisa explorar várias combinações,
    # retrocedendo (backtracking) em muitos momentos até encontrar soluções válidas. A
    # complexidade permanece combinatória porque, em média, várias permutações são testadas
    # para resolver o problema, especialmente à medida que N aumenta.

    # Pior Caso: O(N!) -> No pior caso, o algoritmo precisa explorar todas as combinações
    # possíveis do tabuleiro antes de encontrar todas as soluções ou concluir que não há solução.
    # Isso ocorre porque, para cada linha, ele tenta colocar a rainha em todas as colunas
    # e verifica conflitos com as linhas anteriores. Cada tentativa errada resulta em
    # retrocesso, mas o número de possibilidades exploradas permanece fatorial.

    # Imprime o número de soluções encontradas e as soluções
    print(f"Número de soluções encontradas: {len(solutions)}")
    print_solutions(solutions)
