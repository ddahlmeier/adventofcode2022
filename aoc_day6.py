from collections import Counter

inputs = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def all_unique(items):
    return all (map(lambda x:x==1, Counter(items).values()))


# part 1: start of packet: n=4
# part 2: start of message: n=14
def detect_start(inputs, n=4):
    for i in range(len(inputs)-n):
        if all_unique(inputs[i:i+n]):
            return i+n
    return None

def start_of_packet(inputs):
    return detect_start(inputs, 4)

def start_of_message(inputs):
    return detect_start(inputs, 14)
