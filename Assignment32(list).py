#2. Write a Python program to get the largest and smallest number from a list without builtin functions.

lst = [3, 5, 1, 8, -2, 7, 10]

largest = lst[0]
smallest = lst[0]

for item in lst[1:]:
    if item > largest:
        largest = item
    if item < smallest:
        smallest = item

print(f"Largest number is: {largest}")
print(f"Smallest number is: {smallest}")

'''
Output:
Largest number is: 10
Smallest number is: -2
'''
