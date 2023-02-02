# - Create an array variable named `numbers` with the following content:
#   `[3, 4, 5, 6, 7]`
# - Double all the values in the array

numbers = [3, 4, 5, 6, 7]
for c, i in enumerate(numbers):
    numbers[c] = i * 2

print(numbers)

# or

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)
