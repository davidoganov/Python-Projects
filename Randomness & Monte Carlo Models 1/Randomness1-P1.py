#=============================================================================
# Randomness and Monte Carlo Methods 1 - Problem 1
# Solution to Shiflet & Shiflet (2014)'s Figure 9.2.2 problem (p. 379-380)
# Author(s): Defined functions 
#                f(x), do_one_sim, and do_one_set_sims by Johnny Lin
#                main by David Oganov
# April 15, 2023
#=============================================================================

import numpy as N
import matplotlib.pyplot as plt


def f(x):
    """Function for Figure 9.2.1.
    """
    return N.sqrt(N.power(N.cos(x),2)+1.0)


def do_one_sim(num_darts, xrange=[0.0,2.0], yrange=[0.0,1.5]):
    """Do one Figure 9.2.2 simulation with num_dart darts.
    """
    rand_x = N.random.uniform(low=xrange[0], high=xrange[1], 
                              size=(num_darts,))
    rand_y = N.random.uniform(low=yrange[0], high=yrange[1], 
                              size=(num_darts,))
    rect_area = (xrange[1] - xrange[0]) * (yrange[1] - yrange[0])
    return N.sum( N.where(rand_y < f(rand_x), 1, 0) ) / \
           float(num_darts) * rect_area


def do_one_set_sims(num_sims=100, num_darts=1000):
    """One set of num_sims Monte Carlo simulations.

    Returns a tuple with the mean and standard deviation of the areas
    calculated by the num_sims set of Monte Carlo simulations.
    """
    areas = N.zeros(num_sims, dtype='f')
    for isim in range(num_sims):
        areas[isim] = do_one_sim(num_darts)
    return (N.mean(areas), N.std(areas))


#- I don't provide a main program using the above functions because that's
#  a problem in the randomness1 homework.
###########################################################################

# define main
def main():
    # create 20 samples spaced on log scale 10^1-10^5
    sample_sizes = N.logspace(1, 5, num=20, dtype=int)

    # create empty list to store stdev
    errors = []
    
    # loop thru samples 
    for n in sample_sizes:
        # perform 1000 sims with sample size n
        # get only the stdev of tuple [mean, stdev]
        _, std_dev = do_one_set_sims(num_sims=1000, num_darts=n)
        # add the std_dev to the errors list
        errors.append(std_dev)

    # Plot the results
    plt.plot(sample_sizes, errors)
    plt.xscale('log')
    plt.xticks([10, 100, 1000, 10000, 100000])
    plt.xlabel('Number of Samples')
    plt.ylabel('Standard Deviation')
    plt.title('Error vs. Sample Size')
    plt.show()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()

