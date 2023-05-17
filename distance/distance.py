import math as M
import numpy as N
def distance(x, y, pt):
    """
    Description
    -----------
    Calculates the distance of every point in x and y to 
    pt and output the resulting array.
    
    Parameters
    ----------
    x : vector
        a vector of x-locations, x-point .
    y : vector
        a vector of y-locations, y-point
    pt : tuple
        a tuple, providing a point (x,y)
        
    Returns
    -------
    dist - an array with shape (4,5) that indicates
            the distance from pt to each point.
    """
    # init array of shape (4,5), will contain float, 
    dist = N.zeros((N.shape(y)[0],N.shape(x)[0]), dtype=float)
    # loop thru array
    for i in range(N.size(y)):
        for j in range(N.size(x)):
            # establish the distance between points using distance formula
            # dist = sqrt( (x2-x1)^2 + (y2-y1)^2 )
            dist[i,j] = M.sqrt( ((pt[0] - x[j])**2) + ((pt[1] - y[i])**2) )
    return dist