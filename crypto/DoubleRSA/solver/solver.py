from json import load

rsa = load(open('publickey.json', 'r'))
enc = load(open('encrypted.json', 'r'))
c1 = enc['c1']
c2 = enc['c2']
n = rsa['n']

print((pow(c1, -68608, n) * pow(c2, 42867, n) % n).to_bytes(length=512, byteorder='big'))
