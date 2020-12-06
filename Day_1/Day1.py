# Day 1 solutions for Advent Of Code 2020
with open('input.txt', 'r') as puzzle_input:
    input_list = [int(line.strip()) for line in puzzle_input.readlines()]


def part_one():
    res = []
    for i in input_list:
        if 2020-i in input_list:
            res.append(i)
            res.append(2020-i)
            break
    return res.pop() * res.pop()


def part_two():
    res = set()
    for i in input_list:
        for j in input_list:
            if 2020-(i+j) in input_list:
                res.add(i)
                res.add(j)
                break
    return res.pop() * res.pop() * res.pop()


print('Part 1:', part_one())
print('Part 2:', part_two())
