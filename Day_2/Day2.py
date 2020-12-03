# Input for part 1 and 2
with open('input.txt', 'r') as puzzle_input:
    input_list = [line.strip() for line in puzzle_input.readlines()]


def part_one():
    valids = 0
    for s in input_list:
        s = s.split()
        policy_range = s[0].split('-')
        policy_char = s[1][0]
        if s[2].count(policy_char) in range(int(policy_range[0]), int(policy_range[1])+1):
            valids += 1
    return valids


print('Part 1: ', part_one())


def part_two():
    valids = 0
    for s in input_list:
        s = s.split()
        policy_range = s[0].split('-')
        policy_char = s[1][0]
        if (s[2][int(policy_range[0])-1] == policy_char) ^ (s[2][int(policy_range[1])-1] == policy_char):
            valids += 1
    return valids


print('Part 2: ', part_two())
