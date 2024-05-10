def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError('irregular matrix')

    result = []
    columns = list(zip(*matrix))
    
    for row_index, row in enumerate(matrix):
        for column_index, col in enumerate(columns):
            if max(row) == min(col):
                result.append({'row': row_index + 1, 'column': column_index + 1})
    return result