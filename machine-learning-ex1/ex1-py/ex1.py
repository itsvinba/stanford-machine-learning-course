__author__ = 'Vincent Wei'

import numpy as np
import matplotlib.pyplot as plt

A = np.identity(5)

# Load data from ex1data1
data = np.loadtxt('ex1data1.txt', delimiter=',')

# visualise the data
x = data[:,0] # Populations
y = data[:,1] # Profits
plt.scatter(x, y, c='red', marker='x')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.show()


# implementing linear regression
m, n = np.shape(x);
print(m,n)
X = []
