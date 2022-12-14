inputs = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def parse_tuple(item):
    left, right = map(int, item.split('-'))
    return left, right

def parse(line):
    left, right = map(parse_tuple, line.strip().split(','))
    return left, right

def dominates(first, second):
    return first[0] <= second[0] and first[1]>= second[1]

def has_overlap(first, second):
    return second[0]<=first[0]<=second[1] or first[0]<=second[0]<=first[1]

# part 1
full_overlaps = 0
for line in inputs.splitlines():
    elve1, elve2 = parse(line)
    full_overlaps += int(dominates(elve1, elve2) or dominates(elve2, elve1))
print(full_overlaps)

# part 2
overlaps = 0
for line in inputs.splitlines():
    elve1, elve2 = parse(line)
    overlaps += int(has_overlap(elve1, elve2))
print(overlaps)



