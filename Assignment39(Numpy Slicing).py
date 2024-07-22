#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

zeros_array = np.zeros(10)
print("Array of 10 zeros:")
print(zeros_array)

ones_array = np.ones(10)
print("\nArray of 10 ones:")
print(ones_array)

fives_array = np.full(10, 5)
print("\nArray of 10 fives:")
print(fives_array)

'''
Output:
Array of 10 zeros:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Array of 10 ones:
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

Array of 10 fives:
[5 5 5 5 5 5 5 5 5 5]
'''
