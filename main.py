# Nand
def nand(x, y):
    return not (x and y)


# Not
def not_func(x):
    return nand(x, x)


# Or
def or_func(x, y):
    if x == y:
        return not_func(nand(x, y))

    return nand(x, y)


# Xor
def xor(x, y):
    if x != y:
        return nand(x, y)
    if or_func(x, y):
        return nand(x, y)

    return not_func(nand(x, y))
