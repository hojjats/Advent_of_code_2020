# Day 3 solutions for Advent Of Code 2020
with open('input.txt', 'r') as puzzle_input:
    input_list = [line.strip() for line in puzzle_input.readlines()]


def count_trees(right, down):
    trees = 0
    spot = 0
    for line in input_list[::down]:
        row_width = len(line)
        if (spot >= row_width):
            spot = spot % row_width
        if line[spot] == '#':
            trees += 1
        spot += right
    return trees


print('Part 1: ', count_trees(3, 1))
print('Part 2: ', count_trees(1, 1)*count_trees(3, 1) *
      count_trees(5, 1)*count_trees(7, 1)*count_trees(1, 2))
