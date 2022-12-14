inputs = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def priority(item):
    if item.islower():
        # a-z have prioritoes 1-26
        return ord(item)-96
    elif item.isupper():
        # A-Z have prioritoes 27-52
        return ord(item)-38
    else:
        assert(False)
# part 1
total = 0
for rucksack in inputs.splitlines():
    n = len(rucksack)
    left, right = set(rucksack[:n//2]), set(rucksack[(n//2):])
    both = left.intersection(right)
    assert(len(both) == 1)
    total += priority(list(both)[0])
print(total)


# part 2
total = 0
elves = inputs.splitlines()
groups = [elves[i:i+3] for i in range(0, len(elves), 3)]
for group in groups:
    common = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))
    assert(len(common)==1)
    total += priority(common[0])
print(total)