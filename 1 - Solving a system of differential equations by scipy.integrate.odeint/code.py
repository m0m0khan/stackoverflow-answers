def f(t):
    # relation between f and t
    return value

def rxn1(C,t):
    return np.array([f(t)*C0/v-f(t)*C[0]/v-k*C[0], f(t)*C[0]/v-f(t)*C[1]/v-k*C[1]])
