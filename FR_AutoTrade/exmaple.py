from scipy.sparse import random
from scipy import stats
import numpy as np
import time
import matplotlib.pyplot as plt
class CustomRandomState(np.random.RandomState) :
    def randint(self,k):
        i = np.random.randint(k)
        return i - i%2
x=[]
y=[]
for i in range(1000,20000,2000):
    time_start = time.process_time()
    np.random.seed(12345)
    rs = CustomRandomState()
    rvs = stats.poisson(25, loc=10).rvs
    Sparse_matrix_smaple = random(i,i,density = 0.25,random_state = rs, data_rvs = rvs)
    time_elapsed = (time.process_time() - time_start)
    x.append(i)
    y.append(time_elapsed)

plt.figure()
plt.plot(x,y)
plt.show()
