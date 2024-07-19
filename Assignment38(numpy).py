#2. Convert the below list into a numpy array then display the array then display the first and
#last index and then multiply each element by 2 and display the result.
#Input: my_list = [1, 2, 3, 4, 5]

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
​
print(f"First Element: {arr[0]}")
print(f"Last Element: {arr[-1]}")
​
multiplied_array = arr * 2
​
print(f"Array multiplied by 2: { multiplied_array}")

'''
Output:
[1 2 3 4 5]
First Element: 1
Last Element: 5
Array multiplied by 2: [ 2  4  6  8 10]
'''
