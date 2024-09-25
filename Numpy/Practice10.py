# Generate a 6x6 matrix of random numbers between 0 and 1. Compute the mean, median, variance, and standard deviation of the matrix.

import numpy as np

matrix_6_6=np.random.randint(1,101,(6,6))
print("MATRIX : ")
print(matrix_6_6)

matrix_mean=np.mean(matrix_6_6)
print("\nMEAN : " , matrix_mean)

matrix_median=np.median(matrix_6_6)
print("\nMEDIAN : ", matrix_median)

matrix_variance=np.var(matrix_6_6)
print("\nVARIANCE : ", matrix_variance)

matrix_sd=np.std(matrix_6_6)
print("\nSTANDARD DEVIATION : ", matrix_sd)
