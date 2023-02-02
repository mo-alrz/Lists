# - Create a two-dimensional list dynamically with the following content.
#   Note that a two-dimensional list is often called matrix if every
#   internal list has the same length.
#   Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
#   Its length should depend on a variable
#
# - Print this two-dimensional list to the output


def matrix(length):
    my_matrix = []
    for i in range(length):
        b = []
        for j in range(length):
            b.append(j)
            if i == j:
                b[j] = 1
            else:
                b[j] = 0
        my_matrix.append(b)

    for elem in my_matrix:
        print(*elem)


matrix(4)
print('=======')


# Or with list comprehension

def two_dim_arr(n):
    a = [[0] * n for i in range(n)]
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                a[i][j] = 1
    for elem in a:
        print(*elem)


two_dim_arr(4)
