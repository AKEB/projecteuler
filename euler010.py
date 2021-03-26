"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
https://euler.jakumo.org/problems/view/10.html

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
https://projecteuler.net/problem=10
"""


def _main(N: int) -> int:
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
    a = set(a)
    a.remove(0)
    return sum(a)


if __name__ == "__main__":
    print(_main(2000000))
