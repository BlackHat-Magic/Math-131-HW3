def Lagrange_interp(x_data, y_data, x_interp):
    n = len(x_data)
    m = len(y_data)
    xs = len(x_interp)
    if(n != m):
        return
    p_interp = x_interp * 0
    for i in range(n):
        L_i = np.array([1.] * xs)
        for j in range(n):
            if(i == j):
                continue
            L_i *= (x_interp - x_data[j]) / (x_data[i] - x_data[j])
        p_interp += y_data[i] * L_i
    return(p_interp)