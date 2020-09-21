from Crypto.Util.number import getPrime
from math import gcd
from json import dumps


class RSA:
    def __init__(self, bits):
        self.e1 = 65537
        self.e2 = 104891
        self.p = 1
        self.q = 1
        while gcd((self.p - 1) * (self.q - 1), self.e1 * self.e2) != 1:
            self.p = getPrime(bits)
            self.q = getPrime(bits)
        self.n = self.p * self.q
        self.d1 = pow(self.e1, -1, (self.p - 1) * (self.q - 1))
        self.d2 = pow(self.e2, -1, (self.p - 1) * (self.q - 1))

    def encrypt(self, m):
        return {'c1': pow(m, self.e1, self.n), 'c2': pow(m, self.e2, self.n)}

    def decrypt(self, c1, c2):
        m1 = pow(c1, self.d1, self.n)
        m2 = pow(c2, self.d2, self.n)
        assert (m1 == m2)
        return m1

    def publickey(self):
        return {'n': self.n, 'e1': self.e1, 'e2': self.e2}

    def privatekey(self):
        return {'n': self.n, 'p': self.p, 'q': self.q, 'e1': self.e1, 'e2': self.e2, 'd1': self.d1, 'd2': self.d2}


rsa = RSA(bits=512)
flag = int.from_bytes(open('flag.txt', 'rb').read(), byteorder='big')

encrypted = rsa.encrypt(flag)
open('encrypted.json', 'w').write(dumps(encrypted))
open('publickey.json', 'w').write(dumps(rsa.publickey()))
