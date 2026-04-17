import numpy as np
import matplotlib.pylab as plt

# Min and max for axii
x_min, x_max = -2, 2
y_min, y_max = -2, 2

# Arrays for each Re and Im value split evenly along axis
x_arrary = np.linspace(x_min, x_max, 500)
y_arrary = np.linspace(y_min, y_max, 500)
# Grid array for values
space = np.zeros((len(y_arrary), len(x_arrary)))
# Max iterations
N = 200
# Nested loops for Mandelbrot set test
row = 0
for y in y_arrary:
    col = 0
    for x in x_arrary:
        z = 0
        c = complex(x, y)
        for n in range(N):
            z = z**2 + c
            if abs(z) > 2:
                space[row, col] = n
                break
        col += 1
    row += 1 

plt.title("Mandelbrot Set")
plt.imshow(space, cmap="Spectral")
plt.show()