import matplotlib.pyplot as plt
import numpy as np
f = open("data.txt", "r")
data_list = []
for x in f:
    data_list.append(x.split())
xs = [int(x[0]) for x in data_list]
ys = [int(x[1]) for x in data_list]
plt.scatter(xs, ys)
npxs = np.array(xs)
npys = np.array(ys)

def Pearson_correlation(X,Y):
    if len(X)==len(Y):
        Sum_xy = sum((X-X.mean())*(Y-Y.mean()))
        Sum_x_squared = sum((X-X.mean())**2)
        Sum_y_squared = sum((Y-Y.mean())**2)       
        corr = Sum_xy / np.sqrt(Sum_x_squared * Sum_y_squared)
    return corr

a, b = np.polyfit(npxs, npys, 1)
plt.plot(npxs, a*npxs+b)          
print(Pearson_correlation(npxs,npys))    
plt.show()