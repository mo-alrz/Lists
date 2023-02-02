# Print all elements by looping through
numbers = [4, 5, 6, 7]
for elem in numbers:
    print(elem, end='\n')
print('--------------')

# Print all elements and their indexes by looping through

for index, elem in enumerate(numbers):
    print(index, elem)
print('--------------')

# Print all elements and their indexes while indexes begin from 1
# by looping through

for index, elem in enumerate(numbers, 1):
    print(index, elem)
print('--------------')