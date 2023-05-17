School Assignment Prompt:

Please do these problems.

Recall the exercise we did in lecture where we implemented in Python the area calculation for S&S's Figure 9.2.2 (p. 379) example, and returned an estimate of the error (i.e., the standard deviation) of our area estimate.
For this homework problem, calculate how the error (standard deviation) changes as the number of samples in a simulation (i.e., the number of "dart throws").  Plot the error versus number of samples.
Do Exercise 2, S&S Module 9.3, p. 401.  Turn in both your Python code and the PNG or PDF of your plots.  There is a typo in the problem description.  It should be osqrt(-2ln(rand)), not just osqrt(ln(rand)).
Do Exercise 6, S&S Module 9.3, p. 401-402. 

Exercise 2, S&S Module 9.3, p. 401:

This question refers to the Box-Muller-Gauss method, which generates random
numbers from a normal distribution with mean = 9 and standard deviation = 2.

a. Assign to a a uniformly distributed random number between 0 and 2π.
b. Assign to b the product of the standard deviation (stdDev = 2) and the
   square root of the negative natural logarithm of a uniformly distributed
   random number between 0.0 and 1.0.
c. Return a list of pairs of numbers with (b sin(a) + mean) as the first coordinate
   and (b cos(a) + mean) with mean = 9 as the second that the Box-
   Muller-Gauss method produces. Be sure to use the same a and b for both
   members of a pair.
d. Assign to tblGauss a list of 1000 random numbers in the normal distribution
   with mean = 9 and standard deviation = 2. One way of accomplishing this
   task is to generate a table/array of 500 ordered pairs similar to Part c and to
   flatten the table/array to a corresponding list of 1000 numbers.
e. Display a histogram of these values.
f. If available, use a built-in method to generate the table in Part d.
g. Display a histogram of these values.

Do Exercise 6, S&S Module 9.3, p. 401-402:

This question develops code for the rejection method with the probability
density function f(x) = 2π sin(4πx).

a. Define the function f(x) = 2π sin(4πx). See Figure 9.3.12.
b. Plot f(x) from 0.0 to 0.25.
c. Assign to variable rand a uniform random number from 0.0 to 0.25, the
   interval of interest in Figure 9.3.12.
d. Define the function rej with no arguments to return a random number
   using the rejection method. If f(rand) is greater than a uniform random
   number from 0 to 2π sin(4π/8) = 2π sin(π/2) = 2π, which is the maximum
   value of f(x), return rand. If the condition is false, we must reject rand and
   search for another candidate. To do so, we call the function rej again. Be
   sure rand gets a new value with each function call. (The process of a function,
   such as rej, calling itself is recursion.)
e. Write a statement to generate a list of 1000 random numbers from 0.0 to
   0.25 with the probability density function f(x) = 2π sin(4πx).
f. Display a histogram of these values.
