#=============================================================================
# Randomness and Monte Carlo Methods 1 - Problem 3
# Author: David Oganov
# April 16, 2023
#=============================================================================
import random
import math
import matplotlib.pyplot as plt

# define probability density function
def f(x):
    return 2 * math.pi * math.sin(4 * math.pi * x)

# plot f(x) 
x = [i/100 for i in range(101)]
y = [f(i) for i in x]
plt.plot(x, y)
plt.title("Probability Density Function")
plt.xlabel("x")
plt.ylabel("f(x)")

# define rejection method
def rej():
    rand = random.uniform(0, 0.25)
    u = random.uniform(0, 2 * math.pi)
    if f(rand) > u:
        return rand
    else:
        return rej()

# create list of 1000 random #'s
samples = [rej() for i in range(1000)]

# plot histogram of random #'s
plt.figure()
plt.hist(samples, bins=25, range=(0, 0.25), density=True, alpha=0.5, edgecolor='black')
plt.title("Histogram of Random Numbers")
plt.xlabel("x")
plt.ylabel("Frequency")
plt.show()
