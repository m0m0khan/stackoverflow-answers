 # As suggested by joni, this is doable by using the scipy.optimize.minimize library. You could define a function residual as follows:

def residual(x):
    # calculate/define Q1 = g1(x)
    # calculate/define Q2 = g2(x)

    res = Q1 + Q2

    return res

# This function then can easily be minimized using a constrained algorithm from scipy.optimize.minimize:

import numpy as np
from scipy.optimize import minimize

x0 = 1 # just for example
res = minimize(residual, x0, method='trust-constr', constraints=your_constraints)

# The constraint P1+P2 = target must be defined and passed to the constraints argument as described here. You have to look for linear or non-linear constraint depending upon your constraint.
