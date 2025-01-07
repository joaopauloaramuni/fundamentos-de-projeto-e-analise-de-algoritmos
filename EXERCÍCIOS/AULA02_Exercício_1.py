def knight_tour(n, x, y, move_x, move_y, board, move_count):
    if move_count == n * n:
        return True

    for i in range(8):  # O cavalo tem 8 movimentos possíveis
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0 <= next_x < n and 0 <= next_y < n and board[next_x][next_y] == -1:
            board[next_x][next_y] = move_count
            if knight_tour(n, next_x, next_y, move_x, move_y, board, move_count + 1):
                return True
            board[next_x][next_y] = -1  # Backtrack
    return False

def solve_knight_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    if knight_tour(n, 0, 0, move_x, move_y, board, 1):
        print("Caminho encontrado:")
        for row in board:
            print(row)
    else:
        print("Caminho não encontrado.")

if __name__ == "__main__":
    solve_knight_tour(5)
