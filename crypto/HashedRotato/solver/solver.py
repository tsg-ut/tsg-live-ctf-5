def unhash(x):
    mask = (1 << 64) - 1
    x ^= (x >> 31) ^ (x >> 62)
    x *= 1909397134988591089
    x &= mask
    x ^= (x >> 27) ^ (x >> 54)
    x *= 10116706974279672171
    x &= mask
    x ^= (x >> 30) ^ (x >> 60)
    return (x + 5537064727323688734) & mask


def hash(in_bytes):
    x = int.from_bytes(in_bytes, byteorder='big')
    mask = (1 << 64) - 1
    while x > mask:
        x = (x >> 64) ^ (x & mask)
    x += 12909679346385862882
    x &= mask
    x ^= x >> 30
    x *= 5820690703483732803
    x &= mask
    x ^= x >> 27
    x *= 15893541517945753873
    x &= mask
    return x ^ (x >> 31)


def byte_to_printable(b):
    for i in range(33, 127):
        for j in range(33, 127):
            if (i ^ j) == b:
                return i, j


def bytes_to_printable(b):
    s = []
    t = []
    while b > 0:
        c, d = byte_to_printable(b & 255)
        b >>= 8
        s.append(chr(c))
        t.append(chr(d))
    return ''.join(s[::-1]) + ''.join(t[::-1])


print('a')
input()
input()
given = int(input().split(' ')[3][:-1], 16)
x = unhash(given)
s = bytes_to_printable(x)
assert (hash(s.encode('ascii')) == given)
print(s)
