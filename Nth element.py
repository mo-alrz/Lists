# nth element of an array

numbers = [4, 5, 6, 7]
n = 3
print(numbers[n - 1])

# if it's necessary to save it in a new variable:

third_element = numbers[n - 1]
print(third_element)


# or

def nth_element(my_list, n):
    for element in range(len(my_list)):
        if element == n - 1:
            print(my_list[element])


nth_element([4, 5, 6, 7], 3)


# or

def nth_element(my_list, n):
    for index, elem in enumerate(my_list):
        if index == n - 1:
            print(elem)


nth_element([4, 5, 6, 7], 3)
