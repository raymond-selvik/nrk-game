from typing import Self



from field import FieldType
from board_utils import parse_board_file, get_cluster_indices

class Board:
    def setup_from_file(self,path: str) -> Self:
        self.path = path
        self.fields = parse_board_file(path)

    def try_choose_field(self,row, col) -> bool:
        if self.fields[row][col] is FieldType.EMPTY:
            return False

        cluster_indicies = get_cluster_indices(self.fields,row, col)

        for row,col in cluster_indicies:
            self.fields[row][col] = FieldType.EMPTY
        
        for row in self.fields:
            new_row = row
            for i,f in enumerate(row):
                if f == FieldType.EMPTY:
                    new_row.pop(i)
                    new_row.insert(0, FieldType.EMPTY)
        
        return True

    def is_empty(self) -> bool:
        for row in self.fields:
            for f in row:
                if f is not FieldType.EMPTY: return False
        
        return True

    def reset_board(self):
        self.fields = parse_board_file(self.path)
    def __repr__(self) -> str:
        board = "i|0|1|2|3|4|5|6|\n"

        fields = list(map(list, zip(*self.fields)))
        for i,row in enumerate(fields):
            row_fields = [f.value for f in row]
            row_field_string = '|'.join(row_fields)
            
            board+=f"{i}|{row_field_string}|\n"

        return board
