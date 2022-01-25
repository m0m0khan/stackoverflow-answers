import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

x = [1, 2, 3] # --> assuming your x-data
y = [0.1, 1, 10] # --> assuming your y-data

coefs = poly.polyfit(x, y, 2)
ffit = poly.Polynomial(coefs)
x_new = np.linspace(1, 3, 10) # --> more data points for a smooth curve

plt.plot(x, y, label="Data")
plt.plot(x_new, ffit(x_new), label="Fit")
plt.legend()
plt.show()
