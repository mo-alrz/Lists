# Create an identical list from the first list using list comprehension.

lst1 = [1, 2, 3, 4, 5]

lst2 = [i for i in lst1]
print(lst2)

# Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.

rng = range(1200, 2000, 130)
lst = [i for i in rng]
print(lst)

# Use list comprehension to contract a new list but add 6 to each item.

lst1 = [44, 54, 64, 74, 104]
lst2 = [i + 6 for i in lst1]
print(lst2)

# Using list comprehension,construct a list from the squares of each element in the list.

lst1 = [2, 4, 6, 8, 10, 12, 14]
lst2 = [i * i for i in lst1]
print(lst2)

# Using list comprehension, construct a list from the squares of each element in the list, if the square is greater
# than 50.

lst1 = [2, 4, 6, 8, 10, 12, 14]
lst2 = [i * i for i in lst1 if i * i > 50]
print(lst2)

# Given dictionary is consisted of vehicles and their weights in kilograms. Contract a list of the names of vehicles
# with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.

dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600,
        "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

names = [i.upper() for i in dict.keys() if dict[i] > 5000]
print(names)

# Given a list of numbers, remove all odd numbers from the list:

numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
new_numbers = [i for i in numbers if i % 2 == 0]
print(new_numbers)

# Find all numbers from 1-1000 that have a 3 in them

all_nums_with_3 = [i for i in range(1, 1001) if '3' in str(i)]
print(all_nums_with_3)

# Count the number of spaces in a string

string = 'Hello World Hello World'
spaces = [i for i in string if i == ' ']
print(len(spaces))

# Create a list of all the consonants in the string

string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
non_consonants = ['a', 'e', 'i', 'o', 'u']
consonants = [i for i in string if i.lower() not in non_consonants ]
print(consonants)

# Get the index and the value as a tuple for items in the

list = ["hi", 4, 8.99, 'apple', ('t,b','n')]
tuples_of_val_index = [(c,i) for c,i in enumerate(list)]
print(tuples_of_val_index)

# Find the common numbers in two lists (without using a tuple or set)

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common = [i for i in list_a if i in list_b]
print(common)

# Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even, and the word
# 'odd' if the number is odd. Result would look like 'odd','odd','even'

list_of_odds = ['even' if n % 2 == 0 else 'odd' for n in range(20)]
print(list_of_odds)

# Use a nested list comprehension to find all numbers from 1-100 that are divisible by any single digit besides 1 (2-9)

all_numbs = [number for number in range(1, 100) if any(number % x == 0 for x in range(2, 10))]
print(all_numbs)
