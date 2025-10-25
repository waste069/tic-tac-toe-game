class TicTacToe:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

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
                return row, col

            except ValueError:
                print("error: введите ЦЕЛЫЕ числа (например: 1 2)")
            except Exception as e:
                print(f"неожиданный error: {e}")


def main():
    print("=== КРЕСТИКИ-НОЛИКИ ===")
    game = TicTacToe()

    print("Давайте протестируем ввод данных...")
    game.print_board()

    row, col = game.get_player_input("X")
    print(f"Вы выбрали: строка {row}, столбец {col}")

    game.board[row][col] = 'X'
    game.print_board()


if __name__ == "__main__":
    main()