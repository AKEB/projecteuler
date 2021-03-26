"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
https://euler.jakumo.org/problems/view/10.html

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
https://projecteuler.net/problem=10
"""


def _main():
    a = 1
    b = 1
    c = 1000 - a - b
    for a in range(1, 1000 - 1):
        for b in range(1, 1000 - 1):
            c = 1000 - a - b
            if a > c or b > c:
                break
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return 0


if __name__ == "__main__":
    print(_main())
