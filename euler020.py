"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
https://euler.jakumo.org/problems/view/20.html

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
https://projecteuler.net/problem=20
"""


def factorial(L: int, R: int):
    if L >= R:
        return L
    if L + 1 == R:
        return L * R
    M = (L + R) // 2
    return factorial(L, M) * factorial(M + 1, R)


def _main(N: int) -> int:
    number = factorial(2, N)
    number = str(number)
    summ = 0
    for i in list(number):
        summ += int(i)
    return summ


if __name__ == "__main__":
    print(_main(100))
