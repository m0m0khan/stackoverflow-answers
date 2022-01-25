"""Optimization in scipy.optimize.minimize can be terminated by using tol and maxiter (maxfev also for some optimization methods). There are also some method-specific terminators like xtol, ftol, gtol, etc., as mentioned on scipy.optimize.minimize documentation page. It is also mentioned that if you don't provide a method then BFGS, L-BFGS-B, or SLSQP is used depending on the problem.

Regarding your first question, you are using the maxiter option in the right way, but I can't say why it is not being enforced as you haven't provided an MWE. However, the tol option is placed in options bracket, which is wrong and should be outside of it, like:

res = minimize(f, x0=x0, bounds=bounds, tol=1e-6,options={'maxiter':100})

My suggestion would be to look for your problem-specific optimization method on the above-mentioned scipy.optimize.minimize documentation page and use the specific tolerance options.
Regarding your second question, if you want to terminate the optimization after some time, you could do something as follows, which is inspired by this solution proposed by SuperKogito:"""


from time import time
import warnings
from scipy.optimize import minimize

class TookTooLong(Warning):
    pass

class optimizer():

    def __init__(self, maxtime_sec):
        self.nit = 0
        self.maxtime_sec = maxtime_sec

#    def fun(self, *args):
        # define your function to be minimized here

    def callback(self, x):
        # callback to terminate if maxtime_sec is exceeded
        self.nit += 1
        elapsed_time = time() - self.start_time
        if elapsed_time > self.maxtime_sec:
            warnings.warn("Terminating optimization: time limit reached",
                          TookTooLong)

        else:
            # you could print elapsed iterations and time
            print("Elapsed: %.3f sec" % elapsed_time)
            print("Elapsed iterations: ", self.nit)

    def optimize(self):
        self.start_time = time()
        # set your initial guess to 'x0'
        # set your bounds to 'bounds'
        opt = minimize(self.fun, x0=x0, bounds=bounds,
                       callback=self.callback, tol=1e-6,options={'maxiter':100})
        return opt

# set maxtime_sec variable to desired stopping time
maxtime_sec = 100
op = optimizer(maxtime_sec)
res = op.optimize()
print(res)

# You can also use callback stop optimization after the desired iteration. However, this is not elegant. Just change the callback function in the above code as follows:

class TookTooManyIters(Warning):
    pass

class optimizer():

    def __init__(self, maxtime_sec):
        self.nit = 0
        self.maxtime_sec = maxtime_sec

   # def fun(self, *args):
       # define your function to be minimized here

    def callback(self, x):
        # callback to terminate if desired_iteration is reached
        self.nit += 1
        desired_iteration = 10 # for example you want it to stop after 10 iterations

        if self.nit == desired_iteration:
            warnings.warn("Terminating optimization: iteration limit reached",
                          TookTooManyIters)

        else:
            # you could print elapsed iterations, current solution
            # and current function value
            print("Elapsed iterations: ", self.nit)
            print("Current solution: ", x)
            print("Current function value: ", self.fun(x))
