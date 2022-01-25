"""The function to be optimized by scipy.optimize.minimize should return a scalar value. Please see here.
That being said, you can implement a for-loop and solve stress for each strain value. Afterward, you can take the sum of the stress values and minimize the sum.
Before that, you need to first re-structure your VOCE function as follows:"""

import numpy as np

def voce(sigma_s, sigma_y, epsilon_0, strain):
    stress = sigma_s - (sigma_s - sigma_y)*np.exp(-strain/epsilon_0)
    return stress

# Now, for optimization, introduce a new function, say fun, where you will pass sigma_s, sigma_y, and epsilon_0 to be minimized and strain (1-D array) as an argument for your VOCE function

def fun(x, strain):

    sigma_s = x[0]
    sigma_y = x[1]
    epsilon_0 = x[2]

    stress = []
    sum = 0

    for i in strain:
        s = voce(sigma_s, sigma_y, epsilon_0, i)
        stress.append(s)

    sum = np.sum(stress)

    return sum

# Now, optimize and print the result as follows:

from scipy.optimize import minimize

# strain = [x,y,z] <-- Assign your strain array here
initial_guess = [1, 1, 1]
res = minimize(fun, initial_guess, method="Nelder-Mead", args=(strain))
print(res)

"""Furthermore, if you want to fit the VOCE equation to your stress-strain data (meaning you already have measured stress values from an experiment), you can compare the results (calculated stress) of the VOCE equation with the measured stress using mean squared error from sklearn. For this, you could change the fun as"""

from sklearn.metrics import mean_squared_error

def fun(x, measured_strain, measured_stress):

    sigma_s = x[0]
    sigma_y = x[1]
    epsilon_0 = x[2]

    calculated_stress = []
    error = 0

    for i in measured_strain:
        s = voce(sigma_s, sigma_y, epsilon_0, i)
        calculated_stress.append(s)

    error = mean_squared_error(measured_stress, calculated_stress)

    return error

# where measured_stress is a 1-D array. Now, optimize and print the result as follows

from scipy.optimize import minimize

# measured_strain = [x,y,z] <-- Assign your measured strain array here
# measures_stress = [a,b,c] <-- Assign your measured stress array here
initial_guess = [1, 1, 1]
res = minimize(fun, initial_guess, method="Nelder-Mead",
               args=(measured_strain, measured_stress))
print(res)
