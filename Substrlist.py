#  Create a function that takes a string and a list of string as a parameter
#  and returns the index of the string (in the list) which contains the first string
#  You only need to find the first occurrence and return the index of that
#  Return `-1` if none of the items in the list contain the first string

def find_index(my_str, my_list):
    indexes = []
    for c, i in enumerate(my_list):
        if my_str in i:
            indexes.append(c)

    if len(indexes) == 0:
        return -1
    return indexes


print(find_index("ching", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `4`
print(find_index("hi", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `0 , 4`
print(find_index("not", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `-1`
