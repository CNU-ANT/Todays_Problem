def matrixPow(matrix):
    return [[matrix[0][0] * matrix[0][0] % 1000000007 + matrix[0][1] * matrix[1][0] % 1000000007,
             matrix[0][0] * matrix[0][1] % 1000000007 + matrix[0][1] * matrix[1][1] % 1000000007],
            [matrix[1][0] * matrix[0][0] % 1000000007 + matrix[1][1] * matrix[1][0] % 1000000007,
             matrix[1][0] * matrix[0][1] % 1000000007 + matrix[1][1] * matrix[1][1] % 1000000007]]


def matrixMul(matrixA, matrixB):
    return [[matrixA[0][0] * matrixB[0][0] % 1000000007 + matrixA[0][1] * matrixB[1][0] % 1000000007,
             matrixA[0][0] * matrixB[0][1] % 1000000007 + matrixA[0][1] * matrixB[1][1] % 1000000007],
            [matrixA[1][0] * matrixB[0][0] % 1000000007 + matrixA[1][1] * matrixB[1][0] % 1000000007,
             matrixA[1][0] * matrixB[0][1] % 1000000007 + matrixA[1][1] * matrixB[1][1] % 1000000007]]


def piboMatrix(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    elif n % 2 == 0:
        return matrixPow(piboMatrix(n // 2))
    else:
        return matrixMul(matrixPow(piboMatrix(n // 2)), [[1, 1], [1, 0]])


n = int(input())
print(piboMatrix(n)[0][1] % 1000000007)
