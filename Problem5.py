"""2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder. What is the smallest positive number 
that is evenly divisible by all of the numbers from 1 to 20?"""

def calc(x):
    z = 0
    while True:
        z = z + 1
        for n in range(1, x+1):
            if z % n == 0:
                a = n
            else:   
                break
        if a == x: 
            return z

              
    
if __name__ == '__main__':
    result = calc(20)
    print('Para z =', result)

    def test_calc():
        assert calc(20) == 232792560
 
    