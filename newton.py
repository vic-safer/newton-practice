def optimize(x0,f,h,stop):
    # stop = 1e-2
    # h = 1e-4
    f0 = f(x0)
    df = (f(x0 + h) - f0) / h
    d2f = (f(x0 + h) - 2*f0 + f(x0 - h)) / (h**2)
    x1 = x0 - df / d2f
    while abs(x1 - x0) > stop:
        x0 = x1
        f0 = f(x0)
        df = (f(x0 + h) - f0) / h
        d2f = (f(x0 + h) - 2*f0 + f(x0 - h)) / (h**2)
        x1 = x0 - df / d2f
    print("minimum found at:", x1)
    return
