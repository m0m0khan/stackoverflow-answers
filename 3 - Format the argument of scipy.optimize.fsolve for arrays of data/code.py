"""The function, that is passed to fsolve, takes at least one (possibly vector) argument and returns a value of the same length as mentioned here.
In your case, you are passing x0=0 and args=np.array([1,2,3,4]) to fsolve. The return value of fun has a different length to x0 (x0 is a scalar and args is an array having shape (4,)).
The following code solves your problem:"""

import numpy as np
from scipy.optimize import fsolve

def fun(x, y):
    return x+y

data = np.array([1, 2, 3, 4])
x = fsolve(fun, x0=np.array([0,0,0,0]), args=data)
print(x)
