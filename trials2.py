import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from basic_data import data

# print(np.uniform(-1,1,3))

m = 10
a = -5
b = 5
y0_span = [0,10]
y_idk = np.random.randint(y0_span[0], y0_span[1])
print(y_idk, 'FUCK YEA')
                          

print('----')

print(y_idk)


trials = data(m,a,b)
#print(trials)

df = pd.DataFrame(trials, columns = ['a', 'b', 'a+b'])
# print(df)
y0_span = [0,10]
num_y0 = 3
for j in range(num_y0):
        IC  = [np.random.randint(y0_span[0], y0_span[1])]
        # print(IC, np.shape(IC), type(IC))

trial = data(10, -5, 5)
print(trial[0][1])

