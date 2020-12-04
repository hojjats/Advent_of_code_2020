# Day 4
def part_one():
    valids = 0
    for line in open('input.txt').read().split("\n\n"):
        if all(item in line for item in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            valids += 1
    return valids


def validator(s):
    s = s.split(':')
    if s[0] == 'byr':
        return len(s[1]) == 4 and int(s[1]) in range(1920, 2003)
    elif s[0] == 'iyr':
        return len(s[1]) == 4 and int(s[1]) in range(2010, 2021)
    elif s[0] == 'eyr':
        return len(s[1]) == 4 and int(s[1]) in range(2020, 2031)
    elif s[0] == 'hgt':
        if s[1].count('in'):
            return int(s[1].split('i')[0]) in range(59, 77)
        elif s[1].count('cm'):
            return int(s[1].split('c')[0]) in range(150, 194)
    elif s[0] == 'hcl':
        return s[1][0] == '#' and len(s[1]) == 7 and all(['a' <= c <= 'f' or '0' <= c <= '9' for c in s[1][1:]])
    elif s[0] == 'ecl':
        return s[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif s[0] == 'pid':
        return s[1].isdigit() and len(s[1]) == 9
    elif s[0] == 'cid':
        return True


def part_two():
    valids = 0
    for line in open('input.txt').read().split("\n\n"):
        if not all(item in line for item in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            continue
        validity = 0
        for el in line.split():
            if validator(el):
                validity += 1
        if validity == len(line.split()):
            valids += 1
    return valids


print('Part 1: ', part_one())
print('Part 2: ', part_two())
