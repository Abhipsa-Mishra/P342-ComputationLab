# TOOLS FOR SOLVING DIFFERENTIAL EQUATIONS

########################################################################################################################
########################################################################################################################


# Forward Euler's Method
def euler_forward(f, h, x_0, y_0, n):
    # f = dy/dx, x_0, y_0 = given values, n = number of iterations

    x = []
    y = []
    for i in range(n):
        y_0 += h * f(x_0, y_0)
        x_0 += h
        x.append(x_0)
        y.append(y_0)
    return x, y


########################################################################################################################
########################################################################################################################


# Runge-Kutta Method of Order 4 for solving 2nd order DE
def rk_4(dy_dx, d2y_dx2, h, x_0, y_0, z_0, n):
    # dy_dx = z; d2y_dx2 = dz/dx; x_0, y_0, z_0 = given values; n = no. of iterations

    # list of x values
    X = []

    # list of y values
    Y = []

    # initialise process
    x, y, z = x_0, y_0, z_0
    for i in range(n):
        X.append(x)
        Y.append(y)
        k1y = h * dy_dx(x, y, z)
        k1z = h * d2y_dx2(x, y, z)

        k2y = h * dy_dx(x + h / 2, y + k1y / 2, z + k1z / 2)
        k2z = h * d2y_dx2(x + h / 2, y + k1y / 2, z + k1z / 2)

        k3y = h * dy_dx(x + h / 2, y + k2y / 2, z + k2z / 2)
        k3z = h * d2y_dx2(x + h / 2, y + k2y / 2, z + k2z / 2)

        k4y = h * dy_dx(x + h, y + k3y, + z + k3z)
        k4z = h * d2y_dx2(x + h, y + k3y, + z + k3z)

        y += 1 / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        z += 1 / 6 * (k1z + 2 * k2z + 2 * k3z + k4z)
        x += h

    return X, Y

########################################################################################################################
########################################################################################################################
