"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2  For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""


import math


def calc_triplet():    
    for c in range(1, 1000):
        for b in range(1, 1000):
            a = c*c - b*b
            if a > 0:
               a = math.sqrt(a)
            if a + b + c == 1000:
                return a * b * c

def test_calc_triplet():
    assert calc_triplet(1000) == 31875000.0

if __name__ == '__main__':
    k = calc_triplet()
    print('a * b * c =', k) 
