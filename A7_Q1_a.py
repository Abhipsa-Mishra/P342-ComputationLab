from Tools_DE import euler_forward
from math import log, exp


def f(x,y):
    return y * log(y) / x


X_1, Y_1 = euler_forward(f, 0.5, 2, 2.71828, 10)
X_2, Y_2 = euler_forward(f, 0.05, 2, 2.71828, 100)
X_3, Y_3 = euler_forward(f, 0.01, 2, 2.71828, 500)
X_4, Y_4 = euler_forward(f, 0.001, 2, 2.71828, 5000)

# the output is just list of x and y values which are attached as separate .dat files and graphs which are
# attached as .png files with file names corresponding to question numbers

