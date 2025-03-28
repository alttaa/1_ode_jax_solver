import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
from basic_data import data
from basic_function import sin, cos, tan, exp, ln, polynomial
from scalable_function_bank import Functions, random_func

# a, b upper and lwower bound of real coefficients 
# n = greatest order of function
# M = # of data points (# of rows)
#num_y0 = # of initial conditions tested for each function
#y0_span = range of y0 -- if want to test 1 value, [y0, y0] , y0_span[0] = y0_span[1]
#tspan = bounds of times of data range tspan = [t0 , tf]
def ode_dataset(upper,lower,n, M, num_y0, y0_span, tspan,steps):
    #print(pd.DataFrame(trial, columns = ['a', 'b','a+b']))
    t0 = tspan[0]
    tf = tspan[1]
    for i in range(M):
        trial = data(M, upper, lower)
        trial[i].append(np.random.randint(0,n))
        P_lambda, P_name = random_func(trial[0][i],trial[1][i],trial[2][i],trial[-1])
        #      trial[0],trial[1], trial[2],n) #ccount for lambda t when solve_ivp
        R_lambda, R_name = random_func(trial[0[i]],trial[1][i],trial[2][i],trial[-1])
        #      trial[0],trial[1], trial[2],n)
        trial[i].append(P_name) #in df, P(t) class
        trial[i].append(R_name)#in df, R(t))  class
        def sys(t,y):
             return -P_lambda(t) - R_lambda(t)
        for j in range(num_y0):
             IC = [np.random.randint(y0_span, y0_span[1])]  
             sol = solve_ivp(sys, [t0, tf], IC, t_eval=np.arange(t0, tf, steps))
             trial[i].append(sol.y)
     
        return trial

print(ode_dataset(-5, 5, 4, 10,3,[0,10],[0,10],100))