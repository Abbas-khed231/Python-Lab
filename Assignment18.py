#Python Program to Count the Number of Occurrence of a Character in String

count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)


""" Output=>
 2 """
