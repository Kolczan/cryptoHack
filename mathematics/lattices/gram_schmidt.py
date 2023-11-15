import numpy as np

def gram_schmidt():
    v1 = np.array([4, 1, 3, -1])
    v2 = np.array([2, 1, -3, 4])
    v3 = np.array([1, 0, -2, 7])
    v4 = np.array([6, 2, 9, -5])

    V = np.array([v1, v2, v3, v4])
    U = np.zeros([4, 4])

    U[0] = V[0]
    for i in range(1, len(V)):
        mu = [np.dot(V[i], U[j]) / np.dot(U[j], U[j]) for j in range(i)]
        U[i] = V[i] - np.sum([mu[j] * U[j] for j in range(i)], axis=0)
    print(round(U[3][1], 5))   ## result is 0.9161073825503355 -> need to round it to 0.91611
