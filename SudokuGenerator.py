"""
A python script to generate valid Sudoku problems using rotation + randomization
Author : Vedant Raghuwanshi
Contact : raghuvedant00@gmail.com | www.linkedin.com/in/vedantraghuwanshi

"""


from random import sample

foot = 3


def shift(r, c):
    return (foot * (r % foot) + r // foot + c) % (foot**2)


def shuffle(itr):
    return sample(itr, len(itr))


def sudoku_generator():
    itr = range(foot)
    rows = [i*foot + r for i in shuffle(itr) for r in shuffle(itr)]
    cols = [i*foot + c for i in shuffle(itr) for c in shuffle(itr)]
    gen = shuffle(range(1, foot**2+1))

    grid = [[gen[shift(r, c)] for c in cols] for r in rows]

    edge = foot*foot
    dim = edge*edge
    zeroes = dim * 3//4
    for cell in sample(range(dim), zeroes):
        grid[cell//edge][cell%edge] = 0

    return grid


if __name__ == "__main__":

    grid = sudoku_generator()
    for line in grid:
        print(line)








