"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
https://euler.jakumo.org/problems/view/3.html

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
https://projecteuler.net/problem=3
"""


def _prime(num: int) -> set:
    """Возвращает делители числа"""
    prime = set()
    for i in range(1, int(((num + 1) ** 0.5) * 10 // 10)):
        if num % i == 0:
            if i % 2 > 0:
                prime.add(i)
    return prime


def _main(N: int) -> int:
    """Возвращает максимальный простой делитель числа N"""
    prime = _prime(N)
    simple = []
    for test in prime:
        primeNew = _prime(test)
        if len(primeNew) == 1:
            simple.append(test)
    simple.sort()
    return simple[len(simple) - 1]


if __name__ == "__main__":
    print(_main(600851475143))
