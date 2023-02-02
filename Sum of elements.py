# - Create a variable named `numbers`
#   with the following content: `[54, 23, 66, 12]`
# - Print the sum of the second and the third element

numbers = [54, 23, 66, 12]
c = numbers[1] + numbers[2]
print(c)


# or

def sum_of_elements(indexes):
    my_sum = 0
    for i in range(len(numbers)):
        if i in indexes:
            my_sum += numbers[i]
    return my_sum


print(sum_of_elements([1, 2]))


# Sum of all elements:

def sum_of_all_elements(my_list):
    my_sum = 0
    for i in my_list:
        my_sum += i
    return my_sum


print(sum_of_all_elements(numbers))


# Built-in function:

def sum_of_all_elements_built_in(my_list):
    return sum(my_list)


print(sum_of_all_elements_built_in(numbers))
