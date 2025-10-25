class TicTacToe:
    def __init__(self):
        # Игровое поле 3x3
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.current_player = 'X'
        self.game_over = False

    def print_board(self):
        print("\n  0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i} {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("  ---------")
        print()

    def get_player_input(self, player):
        while True:
            try:
                move = input(f"игрок {player}, введите строку и столбец (например: 0 1): ")
    def get_player_input(self):
        while True:
            try:
                move = input(f"игрок {self.current_player}, введите строку и столбец (например: 0 1): ")

                coordinates = move.split()

                if len(coordinates) != 2:
                    print("error: нужно ввести ДВА числа через пробел!")
                    continue

                row = int(coordinates[0])
                col = int(coordinates[1])

                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("error: числа должны быть от 0 до 2")
                    continue

                if self.board[row][col] != ' ':
                    print("error: эта клетка уже занята")
                    continue

                print(f"nice! ставим в клетку [{row}, {col}]")
                    print("error: числа должны быть от 0 до 2!")
                    continue

                if self.board[row][col] != ' ':
                    print("error: эта клетка уже занята!")
                    continue

                return row, col

            except ValueError:
                print("error: введите ЦЕЛЫЕ числа (например: 1 2)")
            except Exception as e:
                print(f"error: {e}")
                print(f"неожиданный error: {e}")

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        print(f"игрок {self.current_player} походил в [{row}, {col}]")

        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

        print(f"теперь ход игрока {self.current_player}")

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return self.board[row][0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True


def main():
    print("=== КРЕСТИКИ-НОЛИКИ ===")
    print("Тестируем определение победителя...")

    game = TicTacToe()

    print("\n--- ТЕСТ 1: Победитель по первой строке ---")
    game.board = [
        ['X', 'X', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ]
    game.print_board()
    winner = game.check_winner()
    print(f"winner: {winner}" if winner else "Победителя нет")

    print("\n--- ТЕСТ 2: Победитель по второму столбцу ---")
    game.board = [
        ['X', 'O', 'X'],
        [' ', 'O', ' '],
        ['X', 'O', ' ']
    ]
    game.print_board()
    winner = game.check_winner()
    print(f"winner: {winner}" if winner else "Победителя нет")

    print("\n--- ТЕСТ 3: Победитель по главной диагонали ---")
    game.board = [
        ['O', 'X', ' '],
        ['X', 'O', ' '],
        [' ', ' ', 'O']
    ]
    game.print_board()
    winner = game.check_winner()
    print(f"winner: {winner}" if winner else "Победителя нет")

    print("\n--- ТЕСТ 4: Нет победителя ---")
    game.board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', ' ']
    ]
    game.print_board()
    winner = game.check_winner()
    print(f"winner: {winner}" if winner else "Победителя нет")
    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False


def main():
    game = TicTacToe()

    while True:
        game.print_board()

        winner = game.check_winner()
        if winner:
            print(f"победил игрок {winner}!")
            break

        if game.is_board_full():
            print("ничья!!!!")
            break

        row, col = game.get_player_input()
        game.make_move(row, col)

def main():
    print("=== КРЕСТИКИ-НОЛИКИ ===")
    game = TicTacToe()

    print("Давайте протестируем ввод данных...")
    game.print_board()

    row, col = game.get_player_input("X")
    print(f"Вы выбрали: строка {row}, столбец {col}")

    game.board[row][col] = 'X'
    game.print_board()
    print("демка поочередных ходов:")
    game.print_board()

    for turn in range(3):
        print(f"\n--- ход {turn + 1} ---")
        row, col = game.get_player_input()
        game.make_move(row, col)
        game.print_board()


if __name__ == "__main__":
    main()