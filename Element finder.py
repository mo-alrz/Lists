# Write a function that checks if the list contains "7"
# If it does, return "Hoorray" otherwise return "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8]

def contains_number(list,number):
    if number in list:
        return 'Hoorray'
    else:
        return 'Nooooo'

print(contains_number(numbers,7))
print(contains_number(numbers,8))
# The output should be: "Noooooo"
# Do this again with a different solution using different list functions!