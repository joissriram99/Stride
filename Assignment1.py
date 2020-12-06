A = [1, 2, 3]
B = [2, 3]


def Sum(A, B):
    """Args : Lists A and B are list of Numbers.
    Returns : Sum of the Squares of List A and Cubes of List B.
    """

    sum1 = 0
    sum2 = 0

    sum1 = sum([A[i] ** 2 for i in range(len(A))])
    sum2 = sum([B[i] ** 3 for i in range(len(B))])

    return sum1 + sum2


print(Sum(A, B))
