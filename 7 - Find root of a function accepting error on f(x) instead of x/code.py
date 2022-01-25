"""You could use the scipy.optimize.root for achieving this as described here.
You could use any of the mentioned methods on the above-mentioned link. I am choosing broyden1. In this method, you can set fatol to 0.2 as it is the absolute tolerance for the residual."""

from scipy.optimize import root

amountOfCalls = 0

def myFunc(x):
    global amountOfCalls
    amountOfCalls+=1
    y = x ** 3 + x -5
    return y

x0 = 3
res = root(myFunc, x0, method='broyden1', options={'disp':True, 'fatol':0.2})
print(res)

"""The above code will terminate when myFunc(x) < 0.2.

If you want your condition to be explicitly abs(f(x)) < 0.2, then you could use the callback function as it is called at each iteration. You can then check at each iteration, if the condition is met and raise an Error to stop the root-finding method as follows:"""

from scipy.optimize import root

class Error(Exception):
    pass

class AlmostReachedZeroError(Error):
    pass

class rootFinder():

    def __init__(self):
        self.amountOfCalls = 0

    def fun(self, x0):
        y = x0 ** 3 + x0 - 5
        return y

    def callback(self, x, f):
        # callback to terminate if condition is met
        self.amountOfCalls+=1

        if abs(self.fun(x[0])) < 0.2:
            print("Current x: ", x[0], "Current fval: ", f[0],
                  "Iterations: ", self.amountOfCalls)
            raise AlmostReachedZeroError("Terminating optimization: limit reached")

    def find_root(self):
        x0 = 3
        opt = root(self.fun, x0, method='broyden1', callback=self.callback,
                   options={'disp':True, 'ftol':0.2})
        return opt

rf = rootFinder()
res = rf.find_root()
print(res)

"""The above code will terminate the root-finding method if abs(f(x)) < 0.2, and will produce an Error. Also, the current x value, the current fval, and the iterations that the method took will be printed."""
