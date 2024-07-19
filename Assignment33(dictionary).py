#1. Write a Python program and calculate the mean of the below dictionary.

def calculate_mean(dictionary):
    total_sum = 0
    count = 0

    for value in dictionary.values():
        total_sum += value
        count += 1

    mean = total_sum / count
    return mean

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

mean_value = calculate_mean(test_dict)

print(f"The mean of the dictionary values is: {mean_value}")

'''
Output:
The mean of the dictionary values is: 6.2
'''

