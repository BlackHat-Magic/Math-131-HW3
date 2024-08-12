def linear_spline(x_data, y_data, x_interp):
    if(len(x_data) != len(y_data)):
        return
    p_interp = x_interp.copy()
    for i, x in enumerate(x_interp):
        dist = [(xd, yd) for xd, yd in zip(x_data, y_data)]
        dist.sort(key=lambda k: abs(k[0] - x))
        important = dist[:2]
        lowerx, lowery = min(important)
        higherx, highery = max(important)
        p_interp[i] = (highery - lowery) / (higherx - lowerx) * (x - lowerx) + lowery

    return(p_interp)