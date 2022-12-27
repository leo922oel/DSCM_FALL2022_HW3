#%%
import numpy as np
import random
from scipy import stats
#%%
def simulated_distribution(x):
    value = np.exp(-abs(x)**3 / 3)
    return value
def target_distribution(mean, sd):
    f = stats.norm(mean, sd)
    return f


def Importance_sampling(n, target_mean, target_std):
    p = target_distribution(target_mean, target_std)
    x = np.zeros(n)
    weight = np.zeros(n)

    for i in range(n):
        x[i] = random.random()
        q_x = simulated_distribution(x[i])
        p_x = p.cdf(x[i])

        w_x = p_x / q_x
        weight[i] = w_x

    return np.sum((x**2) * weight) / n

def Rejection_sampling(n, target_mean, target_std):
    p = target_distribution(target_mean, target_std)
    x = np.zeros(n)
    output = np.zeros(n)
    # mean_q = 1
    # sd_q = 0.5

    i = 0
    while i < n:
        rv = random.random()
        U = random.uniform(0, 1)
        q_x = simulated_distribution(rv)
        p_x = p.cdf(rv)
        if U < p_x/q_x:
            x[i] = rv
            i = i + 1
    
    return np.sum((x**2) * p.cdf(x)) / n
#%%
# print(Importance_sampling(10000, 0, 1))
print(Rejection_sampling(10000, 0, 1))