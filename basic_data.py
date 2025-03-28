import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def gen_data(a,b):
    cond =  np.random.uniform(a, b) , np.random.uniform(a, b)
    return [cond[0], cond[1],  cond[0] +cond[1]] # averaging index 0 and 1, better data, clusterig
#^ change later s.t i have n uniform for n variables, 

def data(height,a,b):
    data = []
    for i in range(height):
        data.append(gen_data(a,b))
    return data

trial = data(10,-5, 5)
a = trial[0]
b =  trial[1]
c = trial[2]
df = pd.DataFrame(trial, columns =['a' , 'b', 'c'] )
print(np.shape(b))

# #testing 
# #trial = np.array((data(10,-5,5))) # pracing with 10 trials, a = -1, b = 1) 
# #print(np.shape(trial))

# #df = pd.DataFrame(trial, columns=['a', 'b', 'a+b'])
# print(df)
# #print(df['a+b'].sum())

# #logic check
# logic_array = [] #will be nx1 array
# for i in range(df.shape[0]): 
#     if trial[i][2] != trial[i][0] + trial[i][1]:
#         #logic_array.append(data[i][2] == data[i][0] + data[i][1]) - basically what its doig
#         logic_array.append(False)
#     else:
#         logic_array.append(True)

# print(len(logic_array))
# print(logic_array)
# if np.sum(logic_array) != len(logic_array):
#     print("Error")
# else:
#     print("Successful")

# #storing
# np.save("dataset.csv", trial) 

# #TLDR: value generator for random values of data set to build off of
# '''''

# if __name__ == "__main__":
#     trial = np.array(data(10, -5, 5))
#     df = pd.DataFrame(trial, columns=['a', 'b', 'a+b'])
#     print(df)