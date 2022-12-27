#%%
import numpy as np
import math
import scipy
from random import uniform, gammavariate

def get_RandomVariable():
    return uniform(0, 1)

def Normal_Distribution(mean, std):
    U = get_RandomVariable()

    pass
def Exponential_Distribution(l):
    U = get_RandomVariable()
    return np.log(1-U) / (-l)

def Poisson_Distribution(l):
    U = get_RandomVariable()
    cdf = 0
    x = 0
    while cdf <= U:
        cdf += (l ** x) * np.exp(-l) / math.factorial(x)
        print(cdf)
        x += 1
    return x-1

def Chi_Square_Distribution(df):
    U = get_RandomVariable()
    scipy.gamma()
    pass
def F_Distribution(mean, std):
    U = get_RandomVariable()
    pass
def Binomial_Distribution(n, p):
    U = get_RandomVariable()
    cdf = 0
    x = 0
    while cdf <= U:
        cdf += (math.factorial(n) / (math.factorial(x) * math.factorial(n-x))) * (p**x) * ((1-p)**(n-x))
        x += 1
    return x-1

def N_Binomial_Distribution(r, p):
    U = get_RandomVariable()
    cdf = 0
    x = 0
    while cdf <= U:
        cdf += (math.factorial(x+r-1) / (math.factorial(r-1) * math.factorial(x))) * (p**(r)) * ((1-p)**(x))
        x += 1
    return x-1

def Dirichlet_Distribution(a):
    U = get_RandomVariable()
    # gammavariate(a, 1) for a in params
    pass
#%%
print(Poisson_Distribution(10))