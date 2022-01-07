"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""


def largprimo(x):
    n = 2
    while n * n < x:
        while x % n == 0:
             x = x / n
        n = n + 1
    return x
        
def test_largprimo():
    assert largprimo(10001) == 6857.0  

if __name__ == '__main__':
    k = largprimo(600851475143)
    print('O maior número primo é =', k)
    

