"""A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""


def palindromic():
    a = 0
    for n in range(100, 1000):
        for k in range (100, 1000):
            x = n * k
            y = str(x)
            if y[0:1] == y[5:6] and y[1:2] == y[4:5] and y[2:3] == y[3:4] and x > a:
                a = x
    return a

def test_palindromic():
    assert palindromic() == 906609   

if __name__ == '__main__':
    result = palindromic() 
    print("O valor solicitado é:", result)