#==============================================================================
# Shiftlet & Shiftlet Exercise 8
#
# By David Oganov
# April 11, 2023
#==============================================================================

import matplotlib.pyplot as plt
import numpy as np

# calc investment value
def calc_investment_value(p, r, t, dt, n):
    v = p
    for i in range(n):
        a = r * v
        b = r * (v + 0.5 * a * dt)
        c = r * (v + 0.5 * b * dt)
        d = r * (v + c * dt)
        v += ((a + (2 * b) + (2 * c) + d) * dt )/ 6
    return v

# define points, (init $500 investment, 9.3% growth rate, time interval)
points = [(500, 0.093, 10), (500, 0.093, 20), (500, 0.093, 30), (500, 0.093, 40)]

# time steps & # of them
dt = 0.01
n = 1000

# calc investment values for each point
calc_values = []
for point in points:
    p, r, t = point
    calc_value = calc_investment_value(p, r, t, dt, n)
    calc_values.append(calc_value)

# calc analytical investment values 
p, r, t = np.array(points).T
analytical_values = p * np.exp(r * t)

# calc absolute and relative errors
absolute_errors = np.abs(np.array(calc_values) - np.array(analytical_values))
relative_errors = absolute_errors / np.abs(np.array(analytical_values))

# print output
print("Absolute errors:", absolute_errors)
print("Relative errors:", relative_errors)

# plot investment values for each point and analytical values
plt.plot([point[2] for point in points], calc_values, label='Simulated values')
plt.plot([point[2] for point in points], analytical_values, label='Analytical values')
plt.legend()
plt.show()


