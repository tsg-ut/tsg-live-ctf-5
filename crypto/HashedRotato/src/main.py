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


flag = open('flag.txt', 'rb').read()
hashed_flag = hash(flag)

print('Hi!', end=' ')
for i in range(100):
    attempt = hash(input('Do you really know the flag?:\n').encode('ascii'))
    if hashed_flag == attempt:
        print(f'Great! You know the flag: {flag}')
        exit(0)
    else:
        print(f'Hash mismatch.\nflag hash is {hashed_flag:x}, but given is {attempt:x}')
print("Too many tries. You don't know the flag!")
