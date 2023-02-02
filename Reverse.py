numbers = [3, 4, 5, 6, 7]

reverse = []
for i in numbers:
    reverse = [i] + reverse
print(reverse)

# Built-in function:

numbers.reverse()
print(numbers)

# Another built in :

numbers.sort(reverse=True)
print(numbers)
