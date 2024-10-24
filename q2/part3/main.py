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

def xor(a, b):
    li = []

    for i in range(len(a)):
        li.append((a[i] ^ b[i]) & 1)

    return li

plaintext = [int(i) for i in '1001001001101101100100100110']
ciphertext = [int(i) for i in '1011110000110001001010110001']

kstream = xor(ciphertext, plaintext)
print(kstream)

"""
[0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1]

Looking at the key streams, it seams to be repeating in 7 bits (2^3 - 1) period
So, we can easily assume value 3 for m
"""

"""
The output sequence is same as the original stream for the values of IV, taps and 'm'
First 7 stream values match kstream values from above
"""
print(lfsr_states(0b100, [0,1], 3))


