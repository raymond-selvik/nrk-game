import random

from board import Board


def play_game(board: Board,n:int = 1) -> list((int,int)):
    total_choices = []
    for i in range(n):
        print(f"Game: {i}")
        choices = []
        while not board.is_empty():
            col = random.randint(0,6)
            row = random.randint(0,8)

            if board.try_choose_field(col,row):
                choices.append((col,row))
        

        board.reset_board()
        total_choices.append(choices)
    
    shortest_list = min(total_choices, key=len)

    print(f"Shortest Play: {len(shortest_list)}")

    [print(x) for x in shortest_list]

    
  
