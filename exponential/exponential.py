import math as M

def exponential(x, tol=None):
    """
    Description
    -----------
    This function takes a scalar input x and provides
    scalar output of the exponential function. The 
    tolerance is being used as a minimum value for the
    while loop and totaling the calculation as it goes.

    Parameters
    ----------
    x : float
        scalar, positional input
    tol : float
        tolerance to set min in loop. 
        The default is None.

    Returns
    -------
    res : float
        The scalar output of the exponential function 
        upon the given scalar input x.
    """
    # init result var, counter, temp val
    res = 0
    n = 0
    temp = 1
    # loop thru while cond met
    while temp > tol:
      # perform algorithm and place result in temp variable
      temp = (x**n) / M.factorial(n)
      # continue to sum the result
      res += temp
      # increment counter
      n += 1
    return res