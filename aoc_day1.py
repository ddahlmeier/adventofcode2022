inputs = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

# part 1: find the maximum amount of calories carried by any elve
max([sum(map(lambda x:int(x), block.split())) for block in inputs.strip().split("\n\n")])

# part 2: find the amount of calories carried by the top 3 elves
sum(sorted([sum(map(lambda x:int(x), block.split())) for block in inputs.strip().split("\n\n")], reverse=True)[:3])

