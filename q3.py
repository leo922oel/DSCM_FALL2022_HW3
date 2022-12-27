#%%
import numpy as np
from random import uniform
import matplotlib.pyplot as plt

def pi_estimation(n, h):
    X = np.zeros((2, n))
    t = np.zeros((1, n))

    for epoch in range(n):
        X[0, epoch] = 2 * uniform(0, h) - 1
        X[1, epoch] = 2 * uniform(0, h) - 1 

        if X[0, epoch]**2 + X[1, epoch]**2 <= 1:
            t[0, epoch] = 1
    
    circle = X[:, t[0,:]==1]
    square = X[:, t[0,:]==0]
    plt.scatter(circle[0,:], circle[1,:], s=0.5, color="blue")
    plt.scatter(square[0,:], square[1,:], s=0.5, color="green")
    
    return t.sum() / n * 4

def wrong_pi_estimation(n, h):
    X = np.zeros((2, n+1))
    outside = []
    t = 1
    total = 0

    while t != n:
        X[0, t] = X[0, t-1] + 2 * uniform(0, h) - 1
        X[1, t] = X[1, t-1] + 2 * uniform(0, h) - 1 
        total += 1

        if X[0, t]**2 + X[1, t]**2 <= 1:
            t += 1
        else:
            outside.append((X[0, t], X[1, t]))
    
    outside = np.array(outside)
    print(outside)
    plt.scatter(X[0,:], X[1,:], s=0.5, color="blue")
    plt.scatter(outside[:, 0], outside[:, 1], s=0.7, color="green")
    
    return t / total * 4
#%%
print(pi_estimation(20000, 1))
# print(wrong_pi_estimation(20000, 1))
