def rotate(matrix):
    rotated = []
    for col_idx in range(len(matrix[0])):
        new_row = [matrix[row_idx][col_idx] for row_idx, _ in enumerate(matrix)][::-1]
        rotated.append(new_row)
    return rotated

matrix = [[1, 2],[3, 4]]
print(f'Before Rotation{matrix}')
print(rotate(matrix))