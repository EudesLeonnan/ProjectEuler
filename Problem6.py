"""The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is .
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


def calc(k):
    x = 0
    y = 0
    for n in range(k):
        print('n = ', n)
        x = x + n**2
        y = y + n
        z = y**2
        print('x = ', x)
        print('z = ', z)
    return z - x


if __name__ == '__main__':
    result = calc(101)
    print('O resultado é =', result)

    def test_calc():
        assert calc(101) == 25164150