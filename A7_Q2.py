from Tools_DE import rk_4


def dy_dx(x, y, z):
    return z


def dz_dx(x, y, z):
    return 1 - x - z


x_0, y_0, z_0 = 0, 2, 1

# different values of dx, from coarse to fine
h_1, h_2, h_3, h_4 = 0.5, 0.05, 0.01, 0.001

X_1_m, Y_1_m = rk_4(dy_dx, dz_dx, -h_1, x_0, y_0, z_0, 25)
X_1_m.reverse()
Y_1_m.reverse()
X_1_p, Y_1_p = rk_4(dy_dx, dz_dx, h_1, x_0, y_0, z_0, 25)
X_1, Y_1 = X_1_m + X_1_p, Y_1_m + Y_1_p

X_2_m, Y_2_m = rk_4(dy_dx, dz_dx, -h_2, x_0, y_0, z_0, 102)
X_2_m.reverse()
Y_2_m.reverse()
X_2_p, Y_2_p = rk_4(dy_dx, dz_dx, h_2, x_0, y_0, z_0, 102)
X_2, Y_2 = X_2_m + X_2_p, Y_2_m + Y_2_p

X_3_m, Y_3_m = rk_4(dy_dx, dz_dx, -h_3, x_0, y_0, z_0, 500)
X_3_m.reverse()
Y_3_m.reverse()
X_3_p, Y_3_p = rk_4(dy_dx, dz_dx, h_3, x_0, y_0, z_0, 500)
X_3, Y_3 = X_3_m + X_3_p, Y_3_m + Y_3_p

X_4_m, Y_4_m = rk_4(dy_dx, dz_dx, -h_4, x_0, y_0, z_0, 5000)
X_4_m.reverse()
Y_4_m.reverse()
X_4_p, Y_4_p = rk_4(dy_dx, dz_dx, h_4, x_0, y_0, z_0, 5000)
X_4, Y_4 = X_4_m + X_4_p, Y_4_m + Y_4_p

# the output is just list of x and y values which are attached as separate .dat files and graphs which are
# attached as .png files with file names corresponding to respective question numbers
