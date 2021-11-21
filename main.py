def main():
    nand_test()


def nand(x, y):
    return not (x and y)


def nand_test():
    print(f'Actual [ x=0, y=0: {nand(0, 0)} ], Expected[ True ]')
    print(f'Actual [ x=1, y=0: {nand(1, 0)} ], Expected[ True ]')
    print(f'Actual [ x=0, y=1: {nand(0, 1)} ], Expected[ True ]')
    print(f'Actual [ x=1, y=1: {nand(1, 1)} ], Expected[ False ]')


main()
