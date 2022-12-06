import math
import matplotlib.pyplot as plt
import pandas as pd

tableX = []
tableI = []
k = 11
B = []
alpha = []
beta = []
Y = [0 for x in range(k - 1)]
I, N, K, N1 = 11, 11, 11, 11
matrix = [[0 for x in range(k)] for y in range(k)]
matrix[0][0] = - 0.099684
matrix[0][1] = 1
B.append(0.059834)
for i in range(2, 9):
    matrix[0][i] = 0


def func(x0, h, a, b):
    print("X values: ", end=' ')
    for i in range(1, 11):
        tableX.append(round(h * i, 1))
        print(tableX[i - 1], '\t', end=' ')
    while a < b:
        tableY = [round(((tableX[int(a * 10) - 1] + 0.4) * 2 - h * 0.5) / h ** 2 * (tableX[int(a * 10) - 1] + 0.4), 3),
                  round((-2 - math.sqrt(tableX[int(a * 10) - 1] + 0.4) * h ** 2) / h ** 2, 3),
                  round(
                      (2 * (tableX[int(a * 10) - 1] + 0.4) + 0.5 * h) / (2 * h ** 2 * (tableX[int(a * 10) - 1] + 0.4)),
                      3),
                  round(2 / 3 * (tableX[int(a * 10) - 1] + 0.4) ** 2, 3)]
        tableI.append(tableY)
        B.append(tableY[3])
        a = round(a + h, 1)
    print('\n')
    for i in range(0, 9):
        print("i =", i + 1, ":", '\t', end=' ')
        for j in range(0, 4):
            if j == 3:
                print(tableI[i][j], '\t', "= 0", end=' ')
            else:
                print("y[" + str(2 - j + i) + "] *", tableI[i][j], '\t', "+", '\t', end=' ')
        print('\n')
    for i in range(1, 9):
        for j in range(0, 9):
            if (j >= i - 1) and (j <= i + 1):
                matrix[i][j] = tableI[i - 1][1 - j + i]
            else:
                matrix[i][j] = 0


func(0.1, 0.1, 0.1, 1)
print("y[1] - 0.099684 * y[0] = 0.059834")
print('\n')
matrix[8][9] = 282.0
matrix[9][8], matrix[9][9], matrix[9][10] = 101.923, -201.1, 331.5
matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 1, ])
B.append(1)
print("MATRIX", matrix)
print("b-values", B)
print('\n')
N = N1 - 1
alpha.append(-matrix[0][1] / matrix[0][0])
beta.append(B[0] / matrix[0][0])
for i in range(1, N - 1):
    z = matrix[i][i] + matrix[i][i - 1] * alpha[i - 1]
    alpha.append(-matrix[i][i + 1] / z)
    beta.append(B[i] - matrix[i][i - 1] * beta[i - 1] / z)
N -= 1
Y[N] = (B[N] - matrix[N][N - 1] * beta[N - 1]) / (matrix[N][N] + matrix[N][N - 1] * alpha[N - 1])
for i in reversed(range(0, N - 1)):
    Y[i] = alpha[i] * Y[i + 1] + beta[i]
print("Y-values", Y)
df = pd.DataFrame({'X': tableX, 'Y': Y})
plt.plot('X', 'Y', data=df, linestyle='-', marker='o')
plt.show()