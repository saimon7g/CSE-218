import numpy as np
import sys

n = int(input())

A = np.zeros((n, n))
B = np.zeros(n);

for i in range(n):
    arr = input().split();
    for j in range(n):
        A[i][j] = float(arr[j])

for i in range(n):
    B[i] = float(input())


def show(A, B):
    print("================================================================")
    for i in range(n):
        for j in range(n):
            print('%8.4f' % A[i][j], end='\t')
        print('| %8.4f' % B[i])


def GaussianElimination(A, B, pivot=True, showall=True):
    for k in range(n - 1):
        if pivot == True:
            for i in range(k + 1, n):
                if (np.fabs(A[i, k])) > (np.fabs(A[k, k])):
                    A[[k, i]] = A[[i, k]]
                    B[[k, i]] = B[[i, k]]
        if (np.fabs(A[k, k])) < 1.0e-10:
            sys.exit("Division by 0 found")
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] = A[i, j] - (factor * A[k, j])
            B[i] = B[i] - (factor * B[k])
            if showall:
                show(A, B)

    x = np.zeros(n)
    x[n - 1] = B[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i, j] * x[j]

        if np.fabs(A[i, i]) < 1.0e-12:
            sys.exit("Divition by 0 found")
        x[i] = (B[i] - sum) / A[i, i]

    return x;


ara = GaussianElimination(A, B)
print("Solution to this system of linear equations:")
for i in range(n):
    print('%8.4f' % ara[i], end='\t')