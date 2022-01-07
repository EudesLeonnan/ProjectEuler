""""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def calc(x):
    z = 0
    a = 0
    while True:
        z = z + 1
        for n in range(2, z+1):
            if n < z and z % n == 0:
                break
            if n == z and z % n == 0:
                a += 1
        if a == x: 
            return (z)
                        
    
if __name__ == '__main__':
    result = calc(10001)
    print(f'O primo {result} é o {10001}')
    
    def test_calc():
        assert calc(10001) == 104743
    