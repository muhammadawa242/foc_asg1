
# Open the file in binary mode
# with open('./sherlock.txt', 'r') as file:
#     data = file.read()
#
#     binary_stream = ' '.join(format(ord(char), '08b') for char in data)
#
#     with open('eng_bin.txt', 'w') as file:
#         file.write(binary_stream)


with open('./eng_bin.txt', 'r') as f:
    d = f.read()
    d = d.replace(' ', '')


with open('./eng_bin_streams.txt', 'w') as f:
    for i in range(len(d)):
        if i % 1000000 == 0:
                f.write('\n')
        f.write(d[i])
