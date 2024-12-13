from board import Board
from player import play_game

def main() -> None:
    board = Board()
    board.setup_from_file("boards/20241213.txt")


    play_game(board,100000)

if __name__ == '__main__':
    main()