# Check if "list_of_numbers" contains all the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# It should return "True" if it contains all elements, otherwise returns "False"

# 1
a = [4, 8, 12, 12]
b = [2, 4, 6, 8, 10, 12, 14, 16]

print(all(i in b for i in a))


# 2
def is_in_it(a, b):
    counter = len(a)
    for i in a:
        if i in b:
            counter -= 1
    return counter == 0


print(is_in_it(a, b))