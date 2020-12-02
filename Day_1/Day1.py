# Input for part 1 and 2
with open('input.txt', 'r') as puzzle_input:
    input_list = [int(line.strip()) for line in puzzle_input.readlines()]

list = input_list
# Part 1
res = []
for i in list:
    if 2020-i in list:
        res.append(i)
        res.append(2020-i)
        break
print(res[0]*res[1])

# Part 2
res2 = set()
for i in list:
    for j in list:
        if 2020-(i+j) in list:
            res2.add(i)
            res2.add(j)
            break
print(res2.pop() * res2.pop() * res2.pop())
