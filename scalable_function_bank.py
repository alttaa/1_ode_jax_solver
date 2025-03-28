import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd
from basic_data import data
from basic_function import sin, cos, tan, exp, ln, polynomial

class Functions:
    def __init__(self): 
        self.functions = {
            'sin': lambda t,a,b,c,n: sin(t,a,b,c,n),
            'cos': lambda t,a,b,c,n: cos(t,a,b,c,n),
            'tan': lambda t,a,b,c,n: tan(t,a,b,c,n),
            'exp': lambda t,a,b,c,n: exp(t,a,b,c,n),
            'ln': lambda t,a,b,c,n: ln(t,a,b,c,n),
            'polynomial': lambda t,a,b,c,n: polynomial(t,a,b,c,n)
        }
    def get_function(self):
        name = np.random.choice(list(self.functions))
        func =  self.functions[name]

def random_func(a,b,c,n):
    F = Functions()
    name = np.random.choice(list(F.functions))
    func = F.functions[name]
    return func, name

# a,b,c
# def sys(t,y):
#     P, P_name = random_func(a,b,c,n)
#     return P(t)
# tspan = [0,10]
# sol = solve_ivp(sys,tspan,[9], t_eval=np.arange(0,10))
# print(sol.y)

# def random_func(t,a,b,c,n):
#     func_list = [sin(t,a,b,c,n), cos(t,a,b,c,n), tan(t,a,b,c,n), exp(t,a,b,c,n), ln(t,a,b,c,n), polynomial(t,a,b,c,n)]
#     return np.random.choice(func_list), np.random.choice(func_list)

# # P_t, R_t = random_func(1,1,1,1,1) would print integer values
# # print(P_t, R_t)

