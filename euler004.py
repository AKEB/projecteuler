"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
https://euler.jakumo.org/problems/view/4.html

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
https://projecteuler.net/problem=4
"""


def isPolindrom(string: str) -> bool:
    chars = list(string)
    lenght = len(chars)
    for i in range((lenght // 2)):
        if chars[i] != chars[lenght - 1 - i]:
            return False
    return True


def _main():
    response = 0
    for i in range(1000):
        for j in range(1000):
            if isPolindrom(str(i * j)):
                response = max(response, i * j)
    return response


if __name__ == "__main__":
    print(_main())
