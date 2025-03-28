import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def polynomial(x,y):
    return 3*x**2 + 2*x + y + 1

class Functions:
    def __init__(self): 
        self.functions = {
            'polynomial': lambda x,y: polynomial(x,y)
        }
    def get_function(self):
        name = 'polynomial'
        func =  self.functions[name]
        return func
    
print(Functions().get_function()(5,5))

# testing how functions work within classes

def ODE(t,y):
    dydt = lambda t,y: y - 6*y - 2
    return dydt(t,y)

y0 = 0
t = np.linspace(0, 20, 100)
t_eval = np.linspace(0, 20, 100)

sol= solve_ivp(ODE, [t[0], t[-1]], [y0], t_eval=t_eval)
# print(sol.y)
# note solve_ivp returns a tuple, the first element is the time, the second element is the solution
    # syntax(func, [t0, tf], y0, t_eval = t_eval), , t_eval = linspace array/ arange time array

