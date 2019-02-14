import numpy as np


def getMatrix():
    row1, col1 = input(
        "Enter the number of rows and columns of 1st matrix : ").split(",")
    row1, col1 = int(row1), int(col1)
    print(f"Enter {row1*col1} numbers for the matrix 1 : ")
    Matrix = np.array(list(map(int, input().split(",")))).reshape(row1, col1)
    return np.matrix(Matrix)


def printMatrix(Matrix):
    row, col = np.shape(Matrix)
    for i in range(0, row):
        for j in range(0, col):
            print(Matrix[i, j], end=" ")
        print()


def getDiagonalElements(Matrix):
    return np.diagonal(Matrix)


def isSquareMatrix(Matrix):
    row, col = np.shape(Matrix)
    return row == col


firstMatrix = getMatrix()
secondMatrix = getMatrix()
print("\nEntered Matrix 1: ")
printMatrix(firstMatrix)

print("\nEntered Matrix 2  : ")
printMatrix(secondMatrix)

matrixMultiply = firstMatrix * secondMatrix

print("\nMultiplication matrix : ")
printMatrix(matrixMultiply)

print("For Matrix 1 -------->")

print(
    f"\nDiagonal Elements  of First Matrix are => {getDiagonalElements(firstMatrix)}")

if isSquareMatrix(firstMatrix):
    print("It is a Square matrix")
else:
    print("It is Not a Square matrix")


print("For Matrix 2 -------->")

print(
    f"\nDiagonal Elements  of Second Matrix are => {getDiagonalElements(secondMatrix)}")

if isSquareMatrix(secondMatrix):
    print("It is a Square matrix")
else:
    print("It is Not a Square matrix")
