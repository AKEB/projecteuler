"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?
https://euler.jakumo.org/problems/view/7.html

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
https://projecteuler.net/problem=7
"""


def _simple(N: int) -> list:
    a = []
    for i in range(N):
        a.append(i)
    a[1] = 0
    i = 2
    while i < N:
        if a[i] != 0:
            j = i + i
            while j < N:
                a[j] = 0
                j = j + i
        i += 1
    return a


def _main():
    simples = _simple(2_000_000)
    num = 0
    response = 0
    for i in simples:
        if i != 0:
            num += 1
            response = i
        if num == 10_001:
            break
    return (num, response)


if __name__ == "__main__":
    print(_main())
