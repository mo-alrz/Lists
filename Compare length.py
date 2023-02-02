# - Create a variable named `firstArrayOfNumbers`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `secondArrayOfNumbers`
#   with the following content: `[4, 5]`
# - Print "secondArrayOfNumbers is longer" if `secondArrayOfNumbers` has more
#   elements than `firstArrayOfNumbers`
# - Otherwise print: "firstArrayOfNumbers is the longer one"


def compare_length(firstArrayOfNumbers, secondArrayOfNumbers):
    if len(firstArrayOfNumbers) > len(secondArrayOfNumbers):
        print("First array is longer one")

    elif len(firstArrayOfNumbers) == len(secondArrayOfNumbers):
        print("The lengths of two arrays are equal")

    else:
        print("Second array is longer one")


first = [1, 2, 3]
second = [4, 5]

compare_length(first, second)
