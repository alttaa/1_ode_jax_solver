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
        trial_p = np.array(data(M, upper, lower))
        a_list, b_list, c_list = trial_p[:,0], trial_p[:,1], trial_p[:,2]
        trial_r = data(M, upper, lower)
        e_list, f_list, g_list = trial_r[:,0], trial_r[:,1], trial_r[:,2]
        trial_p.append(trial_r)
        trial_p[i].append(np.random.randint(0,n))
        P_lambda, P_name = random_func(a_list, b_list, c_list)
        R_lambda, R_name = random_func(e_list, f_list, g_list) 
        trial_p[i].append(P_name) #in df, P(t) class
        trial_p[i].append(R_name)#in df, R(t))  class
        def sys(t,y,trail):
             return -P_lambda(t,a_list,b_list,c_list) - R_lambda(t,e_list,f_list, g_list)
        for j in range(num_y0):
             IC = [np.random.randint(y0_span[0], y0_span[1])]  
             sol = solve_ivp(sys, [t0, tf], IC, t_eval=np.arange(t0, tf, steps))
             trial_p[i].append(sol.y)
     
        return trial

print(ode_dataset(-5, 5, 4, 10,3,[0,10],[0,10],100))