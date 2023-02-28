# Fizz-buzz multiplication table
# Create a function called fizz_buzz_table that takes a positive integer (n) as an input, and returns the
# n x n multiplication table in a two dimensional array, where the “fizz-buzz” numbers are represented by their
# “fizz-buzz” string. A number is a “fizz-buzz” number if it’s a multiple of 3 or 5. If it’s a multiple of 3,
# it’s value should be Fizz. If it’s a multiple of 5, it’s value should be Buzz. If it’s a multiple of both 3 and 5,
# it’s value should be FizzBuzz.
# fizz_buzz_table(5)
# Should return
#
# [
#   [1, 2, 'Fizz', 4, 'Buzz'],
#   [2, 4, 'Fizz', 8, 'Buzz'],
#   ['Fizz', 'Fizz', 'Fizz', 'Fizz', 'FizzBuzz'],
#   [4, 8, 'Fizz', 16, 'Buzz'],
#   ['Buzz', 'Buzz', 'FizzBuzz', 'Buzz', 'Buzz']
# ]
#
# fizz_buzz_table(3)
#
# Should return
#
# [
#   [1, 2, 'Fizz'],
#   [2, 4, 'Fizz'],
#   ['Fizz', 'Fizz', 'Fizz']
# ]

def fizz_buzz_table(n):
    list_1 = []
    for i in range(1, n + 1):
        list_2 = []
        for j in range(1, n + 1):
            if i * j % 3 == 0 and i * j % 5 == 0:
                list_2.append('FizzBuzz')
            elif i * j % 3 == 0:
                list_2.append('Fizz')
            elif i * j % 5 == 0:
                list_2.append('Buzz')
            else:
                list_2.append(i * j)
        list_1.append(list_2)

    return list_1


print(fizz_buzz_table(3))
print(fizz_buzz_table(5))
