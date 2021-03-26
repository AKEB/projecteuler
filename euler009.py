"""
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a**2 + b**2 = c**2
Например, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
https://euler.jakumo.org/problems/view/9.html

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
https://projecteuler.net/problem=9
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
