def sum_100():
    """

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

    """
    i = 0
    sum1 = 0
    while i < 101:
        sum1 += i
        i = i + 1
    print(sum1)
    return sum1


def square_100():
    i = 1
    sqr1, sqr = 0, 0
    while i < 101:
        sqr1 = i**2
        sqr += sqr1
        i = i + 1
    print(sqr)
    return sqr


sum_100()
square_100()
value = square_100() - sum_100()
print(value)
