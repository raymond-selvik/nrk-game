from field import FieldType

def parse_board_file(path: str) -> list(list[FieldType]):

    fields = []
    with open(path) as f:
        for i, line in enumerate(f):  
            line = list(line.rstrip())
            fields.append([FieldType.parse(ch) for ch in line])
      
    fields = list(map(list, zip(*fields)))
    
    return fields

def get_cluster_indices(array, row, col):
    rows = len(array)
    cols = len(array[0])
    value = array[row][col]
    visited = set()
    stack = [(row, col)]
    cluster_indices = []

    while stack:
        r, c = stack.pop()
        if (r, c) not in visited and 0 <= r < rows and 0 <= c < cols and array[r][c] == value:
            visited.add((r, c))
            cluster_indices.append((r, c))
            # add neighbors to stack
            neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    return cluster_indices
