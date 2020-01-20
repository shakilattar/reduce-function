from functools import reduce


def p(a, b):
    return a + b


r = reduce(p, [1, 2, 3, 4, 5, 6, 7])
print(r)
