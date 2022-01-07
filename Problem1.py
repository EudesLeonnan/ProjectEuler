"""Problem 1 - If we list all the natural numbers below 10 
that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""


def calculo_soma(n):
    soma = 0
    for n in range(n):
            if n % 3 == 0 or n % 5 == 0:
                soma += n
    return soma

def test_caculo_soma():
    assert calculo_soma(1000) == 233168        

if __name__ == '__main__':
    n = input('Digita ai')
    valor = calculo_soma(int(n))
    print('Soma =', valor)

