def add_matrices(matrix1, matrix2):
    return [[i + j for i, j in zip(row1, row2)] 
            for row1, row2 in zip(matrix1, matrix2)]

def subtract_matrices(matrix1, matrix2):
    return [[i - j for i, j in zip(row1, row2)] 
            for row1, row2 in zip(matrix1, matrix2)]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))
