# same len
M1 = "Every"
M2 = "small"
M3 = "group"
M4 = "wants"
M5 = "peace"
SAME_KEY = "NOMCS"


def to_ascii(a):
    li = []

    for i in a:
        li.append(ord(i))

    return li

def xor(a, b):
    li = []

    for i in range(len(a)):
        li.append(a[i] ^ b[i])

    return li

def un_ascii(a):
    s = ""

    for i in a:
        s += chr(i)
    
    return s

def main():

    m1 = to_ascii(M1)
    m2 = to_ascii(M2)
    m3 = to_ascii(M3)
    m4 = to_ascii(M4)
    m5 = to_ascii(M5)
    k = to_ascii(SAME_KEY)

    en1 = xor(m1, k)
    en2 = xor(m2, k)
    en3 = xor(m3, k)
    en4 = xor(m4, k)
    en5 = xor(m5, k)

    # only if we somehow guessed that the first cipher is the message "Every", we will be able to guess all the other messages encrypted using the same key
    guessed_msg1 = to_ascii("Every")
    guessed_key = xor(guessed_msg1, en1)

    # now we can decrypt the rest of the messages using the guessed_key
    print(un_ascii(xor(en1, guessed_key)))
    print(un_ascii(xor(en2, guessed_key)))
    print(un_ascii(xor(en3, guessed_key)))
    print(un_ascii(xor(en4, guessed_key)))
    print(un_ascii(xor(en5, guessed_key)))


if __name__ == '__main__':
    main()
