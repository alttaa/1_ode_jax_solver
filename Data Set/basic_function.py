import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd
from basic_data import data

#1st order ode = dy/dt + P(t)y^n = R(t)
#need to define and pull generic functions(e.g sin, cos, tan, exp, ln, polynomials, etc) for non homogenous and coefficient functions
#data set will be trained off of a some of these defined functions with random real variables (e.g let R(t)) = asin((bt) where a = 4, b = 9.5

n = np.random.randint(0,4)

def sin(t,a,b,c,n):
    return a * np.sin(b * t**n) + c

def cos(t, a, b, c, n):
    return a * np.cos(b * t**n) + c

def tan(t, a, b, c, n):
   return a * np.tan(b * t**n) + c

def exp(t, a, b, c, n):
        return a * np.exp(b * t**n) + c

def ln(t, a, b, c, n):
        return a * np.log(b * t**n) + c

def polynomial(t,a,b,c,n):
    if n> 1:
        return a * (t**n) + b*(t**(n-1)) + c
    elif n == 1:
        return a*(t) +b
    else:
        return c #COVERS CONSTANT CASES of R(t), P(t)  !!, no need to write another | constants form of polynomials :D


# def trial(height,a,b):
#     trial = np.array((data(height,a,b)))
#     return trial_data

# trial_data = trial(10,-5,-5)
# print(np.shape(trial_data))

# df = pd.DataFrame(trial, columns=['a', 'b', 'a+b'])
# # print(df)

# n_list =[]
# #for i in range(10):
#     n = np.random.randint(0,4)
#     n_list.append(n)
# #