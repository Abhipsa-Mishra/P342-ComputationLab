from Tools_DE import euler_forward


def f(x,y):
    return 6 - 2*y/x


X_1, Y_1 = euler_forward(f, 0.5, 3, 1, 20)
X_2, Y_2 = euler_forward(f, 0.05, 3, 1, 100)
X_3, Y_3 = euler_forward(f, 0.01, 3, 1, 500)
X_4, Y_4 = euler_forward(f, 0.001, 3, 1, 5000)

# the output is just list of x and y values which are attached as separate .dat files and graphs which are
# attached as .png files with file names corresponding to respective question numbers

