# Day 5 solutions for Advent Of Code 2020
# Golfy solution using str.maketrans() and binary conversion
with open('input.txt', 'r') as puzzle_input:
    input_list = [int(line.translate(str.maketrans('FBLR', '0101')).strip(), 2)
                  for line in puzzle_input.readlines()]


def part_one():
    return max(input_list)


def part_two():
    return [seat for seat in range(min(input_list), max(input_list)) if seat-1 in input_list and seat+1 in input_list and seat not in input_list][0]


print('Part 1:', part_one())
print('Part 2:', part_two())


# Less Golfy solution using recursion
with open('input.txt', 'r') as puzzle_input:
    input_list = [line.strip() for line in puzzle_input.readlines()]


def search(string, spot, r):
    if len(r) == 1:
        return r
    else:
        if string[spot] == 'F' or string[spot] == 'L':
            return search(string, spot+1, r[:int(len(r)/2)])
        elif string[spot] == 'B' or string[spot] == 'R':
            return search(string, spot+1, r[int(len(r)/2):])


seat_ids = []


def part_one():
    for line in input_list:
        seat_ids.append((search(line[:7], 0, list(range(0, 128)))[
                        0] * 8) + search(line[7:], 0, list(range(0, 8)))[0])
    return max(seat_ids)


def part_two():
    return [seat for seat in range(min(seat_ids), max(seat_ids)) if seat-1 in seat_ids and seat+1 in seat_ids and seat not in seat_ids][0]


print('Part 1:', part_one())
print('Part 2:', part_two())
