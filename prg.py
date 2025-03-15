class TicTacToe:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print([cell if cell is not None else "-" for cell in row])
        print()

    def is_winner(self, player):
        # Check rows and columns
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(
            self.board[i][2 - i] == player for i in range(3)
        ):
            return True
        return False

    def is_draw(self):
        return all(cell is not None for row in self.board for cell in row) and \
               not self.is_winner("X") and not self.is_winner("O")

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def minimax(self, is_maximizing):
        if self.is_winner("X"):
            return 1
        if self.is_winner("O"):
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for row, col in self.get_available_moves():
                self.board[row][col] = "X"
                score = self.minimax(False)
                self.board[row][col] = None
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for row, col in self.get_available_moves():
                self.board[row][col] = "O"
                score = self.minimax(True)
                self.board[row][col] = None
                best_score = min(best_score, score)
            return best_score

    def find_best_move(self):
        best_score = float("-inf")
        best_move = None
        for row, col in self.get_available_moves():
            self.board[row][col] = "X"
            score = self.minimax(False)
            self.board[row][col] = None
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move

def main():
    game = TicTacToe()
    game.print_board()
    while True:
        row, col = map(int, input("Enter row and column for O (0-2): ").split())
        game.make_move(row, col, "O")
        game.print_board()
        if game.is_winner("O"):
            print("O wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

        print("AI is making a move...")
        row, col = game.find_best_move()
        game.make_move(row, col, "X")
        game.print_board()
        if game.is_winner("X"):
            print("X wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
