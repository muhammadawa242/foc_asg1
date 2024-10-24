import random

def lfsr_states(state, taps, ln):
    c = 0
    initial_state = state
    li = []

    # continue until state repeats
    while (c != 1) or (state != int(initial_state)):
        li.append("{:0{ln}b}".format(state, ln=ln))

        new = state>>taps[0]
        for i in range(1, len(taps)):
            new ^= (state>>taps[i])
        new = new & 1

        state = (new << (ln-1)) | (state >> 1)
        c = 1

    return li

def generate_random_bits(length):
    # Generate a random binary string of the specified length
    res = '0'*length
    while res == '0'*length or res == '1'*length:
        res = ''.join(random.choice('01') for _ in range(length))

    return res


def get_states(taps, ln):
    bits = int(generate_random_bits(ln), 2)
    li = lfsr_states(bits, taps, ln)
    s = str(li) + ', ' + str(len(li)) + ', ' + "{:0{ln}b}\n".format(bits, ln=ln)

    return s

# x4 + x + 1
with open('./1.txt', 'w') as f:
    for i in range(10):
        f.write(get_states([0, 1], 4))

# x4 + x2 + 1
with open('./2.txt', 'w') as f:
    for i in range(10):
        f.write(get_states([0, 2], 4))

# x4 + x3 + x2 + x + 1
with open('./3.txt', 'w') as f:
    for i in range(10):
        f.write(get_states([0, 1, 2, 3], 4))

