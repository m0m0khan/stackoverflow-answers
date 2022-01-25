"""In such an equation system, where the previous values of some variables are required in the evolution equation of other variables, you could define your function as follows:"""

import numpy as np

def fun(RHS, t):

    # get initial boundary condition values
    discrete_S0 = RHS[0]
    discrete_I0 = RHS[1]
    discrete_Q0 = RHS[2]
    discrete_H0 = RHS[3]
    discrete_D0 = RHS[4]

    # calculte rate of respective variables
    discrete_S0dt = - v * discrete_S0 * discrete_I0 / (N - discrete_Q0 - discrete_H0 - discrete_D0)
    discrete_I0dt = v * discrete_S0 * discrete_I0 / (N - discrete_Q0 - discrete_H0 - discrete_D0) - gamma * discrete_I0 - alpha * discrete_I0 - psi * discrete_I0
    discrete_Q0dt = alpha * discrete_I0 - eta_q * discrete_Q0 - k_h *discrete_Q0 + k_q * discrete_H0
    discrete_H0dt = psi * discrete_I0 - eta_h * discrete_H0 + k_h * discrete_Q0 - k_q * discrete_H0 - zeta * discrete_H0
    discrete_D0dt = eta_q * discrete_Q0 + eta_h * discrete_H0

    # Left-hand side of ODE
    LHS = np.zeros([5,])

    LHS[0] = discrete_S0dt
    LHS[1] = discrete_I0dt
    LHS[2] = discrete_Q0dt
    LHS[3] = discrete_H0dt
    LHS[4] = discrete_D0dt

    return LHS

# Afterward, you can solve it (according to your boundary conditions) as follows:

from scipy.integrate import odeint

v=0.1
alpha = 0.3
gamma = 1/21
psi = 0.2
k_h=0.1
k_q=0.1
eta_h=0.3
eta_q=0.3
y0 = [99, 1, 0, 0, 0]
t = np.linspace(0,13,14)

res = odeint(fun, y0, t)

# Here y0 is the initial boundary condition for all the variables defined in the function fun at t=0. That's why the variable t starts from 0.
# Also, you can get the result of all the variables as follows:

print(res[:,0])
print(res[:,1])
print(res[:,2])
print(res[:,3])
print(res[:,4])
