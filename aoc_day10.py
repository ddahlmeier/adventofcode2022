# Day 10: cathode-ray tube

inputs = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()


def register_values(inputs):
    register = 1
    cycle = 1
    yield (cycle, register)
    for instruction in inputs:
        if instruction == "noop":
            cycle +=1
            yield (cycle, register)
        elif instruction.startswith("addx"):
            value = int(instruction.split()[1])
            cycle += 1
            yield (cycle, register)
            cycle += 1
            register += value
            yield (cycle, register)
        else:
            print("unknown instruction")
            break

# part 1
cycles = filter(lambda x:x[0] in [20, 60, 100, 140, 180, 220], register_values(inputs))
signal_strength = map(lambda x : x[0]*x[1], cycles)
print(sum(signal_strength))

# part 2
def generate_pixels(inputs):
    for pixel, (cycle, register) in enumerate(register_values(inputs)):
        if abs(register-pixel%40) <=1:
            yield "#"
        else: 
            yield(".")

def draw_screen(pixels):
    # screen dimensions: 40 pixels wide, 6 pixels height, left to right
    for i, pixel in enumerate(pixels, start=1):
        end_char = "\n" if i%40==0 else ""
        print(pixel, end=end_char)


    