'''1. Suppose you have a dataset containing daily temperature readings for a city,
and you want to identify days with extreme temperature conditions.
Find days where the temperature either exceeded 35 degrees Celsius (hot day) or
dropped below 5 degrees Celsius (cold day).''' 


import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, -4.0, 37.2, -4, -12])

hot_days = np.where(temperatures > 35)[0]

cold_days = np.where(temperatures < 5)[0]

print("Hot Days:")
print("Day\t Temperature")
for index in hot_days:
    print(f"{index+1}\t {temperatures[index]}")


print("\nCold Days:")
print("Day\t Temperature")
for index in cold_days:
    print(f"{index+1}\t {temperatures[index]}")


'''
Output:
Hot Days:
Day	 Temperature
3	 36.8
6	 38.7
11	 37.2

Cold Days:
Day	 Temperature
10	 -4.0
12	 -4.0
13	 -12.0
'''
