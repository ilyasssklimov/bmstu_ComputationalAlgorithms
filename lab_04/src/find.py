def get_system(table, degree):
    degree += 1
    n = len(table)
    zeros = [0 for _ in range(degree)]
    system = [zeros[:] for _ in range(degree)]
    free_column = zeros[:]

    for i in range(degree):
        for j in range(n):
            tmp = table[j][2] * (table[j][0] ** i)
            for z in range(degree):
                system[i][z] += tmp * (table[j][0] ** z)
            free_column[i] += tmp * table[j][1]

    return system, free_column


def get_inverse_matrix(matrix):
    n = len(matrix)
    zeros = [0 for _ in range(n)]
    inverse_matrix = [zeros[:] for _ in range(n)]
    for i in range(n):
        column = convert_column(matrix, i)
        for j in range(n):
            inverse_matrix[j][i] = column[j]

    return inverse_matrix


def convert_column(matrix, index):
    n = len(matrix)
    extended_matrix = [matrix[i][:] for i in range(n)]
    new_column = [0 for _ in range(n)]

    for i in range(n):
        extended_matrix[i] += [1.0] if i == index else [0.0]

    for i in range(n):
        if not extended_matrix[i][i]:
            for j in range(i + 1, n):
                if extended_matrix[j][j]:
                    extended_matrix[i], extended_matrix[j] = extended_matrix[j], extended_matrix[i]

        for j in range(i + 1, n):
            d = -extended_matrix[j][i] / extended_matrix[i][i]
            for z in range(n + 1):
                extended_matrix[j][z] += d * extended_matrix[i][z]

    for i in range(n - 1, -1, -1):
        result = 0
        for j in range(n):
            result += extended_matrix[i][j] * new_column[j]

        new_column[i] = (extended_matrix[i][n] - result) / extended_matrix[i][i]

    return new_column


def multiply(inverse_matrix, free_column):
    n = len(free_column)
    result = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i] += free_column[j] * inverse_matrix[i][j]

    return result


def find_coefficients(table, degree):
    system, free_column = get_system(table, degree)
    inverse_matrix = get_inverse_matrix(system)
    coefficients = multiply(inverse_matrix, free_column)

    return coefficients
