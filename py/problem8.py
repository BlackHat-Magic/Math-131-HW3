def least_squares(datx, daty, n):
    X = np.vander(datx, n+1)
    coefficients = np.linalg.solve(X.T @ X, X.T @ daty)
    return(coefficients)

def exp_least_squares(datx, daty):
    log_daty = np.log(daty)
    X = np.vstack([np.ones_like(datx), datx]).T
    b, _, _, _ = np.linalg.lstsq(X, log_daty, rcond=None)
    b0 = b[0]
    b1 = b[1]
    a0 = np.exp(b0)
    a1 = b1
    return(a0, a1)