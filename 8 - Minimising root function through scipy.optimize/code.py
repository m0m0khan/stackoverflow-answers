from scipy.optimize import minimize

def residual(x):
    return (peak_infections(x) - 0.1) ** 2

x0 = 0.5
res = minimize(residual, x0, method="Nelder-Mead", options={'fatol':1e-04})
print(res)


## Edit

import numpy as np
from scipy.integrate import odeint
from  scipy.optimize import minimize
import pandas as pd

d = {'Week': [1, 2,3,4,5,6,7,8,9,10,11], 'incidence': [206.1705794,2813.420201,11827.9453,30497.58655,10757.66954,7071.878779,3046.752723,1314.222882,765.9763902,201.3800578,109.8982006]}
df = pd.DataFrame(data=d)

def peak_infections(beta, df):

    # Weeks for which the ODE system will be solved
    weeks = df.Week.to_numpy()

    # Total population, N.
    N = 1000
    # Initial number of infected and recovered individuals, I0 and R0.
    I0, R0 = 10, 0
    # Everyone else, S0, is susceptible to infection initially.
    S0 = N - I0 - R0
    J0 = I0
    # Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
    gamma = 1/7 * 7 #rate should be in weeks now
    # A grid of time points (in days)
    t = np.linspace(0, weeks[-1], weeks[-1] + 1)

    # The SIR model differential equations.
    def deriv(y, t, N, beta, gamma):
        S, I, R, J = y
        dS = ((-beta * S * I) / N)
        dI = ((beta * S * I) / N) - (gamma * I)
        dR = (gamma * I)
        dJ = ((beta * S * I) / N)
        return dS, dI, dR, dJ

    # Initial conditions are S0, I0, R0
    # Integrate the SIR equations over the time grid, t.
    solve = odeint(deriv, (S0, I0, R0, J0), t, args=(N, beta, gamma))
    S, I, R, J = solve.T

    return I/N

def residual(x, df):

    # Total population, N.
    N = 1000
    incidence = df.incidence.to_numpy()/N
    return np.sum((peak_infections(x, df)[1:] - incidence) ** 2)

x0 = 0.5
res = minimize(residual, x0, args=(df), method="Nelder-Mead", options={'fatol':1e-04})
print(res)
