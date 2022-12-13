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

max([sum(map(lambda x:int(x), block.split())) for block in inputs.strip().split("\n\n")])
