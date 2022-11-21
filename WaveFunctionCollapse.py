import numpy as np

# Checks whether the matrix can be processed


def isValid(matrix):
    valid = True

    for row in matrix:
        valid = 1 in row
        if not valid:
            return False

    for coulmn in matrix.T:
        valid = 1 in coulmn
        if not valid:
            return False

    return True


def weightMatrix(matrix):
    for i, row in enumerate(matrix):
        nEntries = np.count_nonzero(row)
        matrix[i] = [1/nEntries if e != 0 else 0 for e in row]


def choose(i, j, matrix, resultArray):
    resultArray[i] = j

    cols, rows = matrix.shape

    for k in range(cols):
        matrix[k][j] = 0

    for k in range(rows):
        matrix[i][k] = 0


def matrixArgMax(matrix):
    maxI, maxJ = np.unravel_index(np.argmax(matrix), matrix.shape)

    row = matrix[maxI]

    chosenMaxJ = np.random.choice(np.flatnonzero(row == row.max()))

    return (maxI, chosenMaxJ)


def findMatches(adjacencyMatrix):
    result = np.zeros(len(adjacencyMatrix))
    if isValid(adjacencyMatrix):
        waveFunction = adjacencyMatrix.copy()
        while 1 in (waveFunction != 0):
            weightMatrix(waveFunction)
            i, j = matrixArgMax(waveFunction)
            choose(i, j, waveFunction, result)
        return result
    else:
        return "The matrix is not valid, make sure that there is at least a one per column and a one per row"


if __name__ == '__main__':
    # Given adjancy Matrix with preferencies
    adjacencyMatrix = np.array([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 1, 0],
    ], dtype=float)

    print(adjacencyMatrix)
    print(findMatches(adjacencyMatrix))
