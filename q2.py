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
def Average(lst):
    return sum(lst) / len(lst)

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
#%%
print(Importance_sampling(10000, 0, 1))
#%%
# reject sampling
def n_distribution(mean, sd):
    distribution = stats.norm(mean, sd)
    return distribution
p_x = n_distribution(mean_q, sd_q)
mean_q = 1
sd_q = 0.5
i = 0
output = np.zeros(n)
while i < n:
  U = random.random()
  V = target_distribution(U)
  if V < p_x.pdf(U):
    output[i] = U
    i = i + 1
print(output)
#%%
