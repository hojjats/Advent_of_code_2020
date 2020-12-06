# Day 6 solutions for Advent Of Code 2020
def part_one():
    count = 0
    for line in open('input.txt').read().split('\n\n'):
        count += len(set(line.replace('\n', '')))
    return count


def part_two():
    count = 0
    for line in open('input.txt').read().split('\n\n'):
        for i in set(line.replace('\n', '')):
            if line.count(i) == len(line.split('\n')):
                count += 1
    return count


print('Part 1:', part_one())
print('Part 2:', part_two())
