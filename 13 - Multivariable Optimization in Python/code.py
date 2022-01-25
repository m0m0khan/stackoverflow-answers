# You can use scipy.optimize.minimize to minimize a scalar function with one or more variables. For this, first change your function as:

def average_receptance(x):

    K_t = x[0]
    C_t = x[1]

    frequency_matrix = np.array([])
    alphabetaE11_matrix = np.array([])

    for i in range(first_natural_frequency - natural_frequency_delta,first_natural_frequency + natural_frequency_delta):

        frequency_matrix = np.append(frequency_matrix, i)
        alphabetaE11_matrix = np.append(alphabetaE11_matrix, math.log(abs(receptance(K_t, C_t, i))))

    receptance_average = np.average(alphabetaE11_matrix)

    return receptance_average

# then use minimize function of scipy, to minimize the variables. You need to pass an initial guess though for the optimization to start. You can do this as follows:

x0 = [600000, 50] # -> example guess for K_t and C_t
res = minimize(average_receptance, x0, method="Nelder-Mead", options={'disp':True, 'fatol':1e-04})
print(res)

# The above code will minimize both the parameters of your function.
