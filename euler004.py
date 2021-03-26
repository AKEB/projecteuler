"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
https://euler.jakumo.org/problems/view/4.html

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
https://projecteuler.net/problem=4
"""


def isPalindrom(string: str) -> bool:
    """Определяет является ли строка палиндромом"""
    chars = list(string)
    lenght = len(chars)
    for i in range((lenght // 2)):
        if chars[i] != chars[lenght - 1 - i]:
            return False
    return True


def _main(N: int) -> int:
    """Возвращает максимальное число палиндром из произведения чисел до N"""
    response = 0
    for i in range(N - 1, 0, -1):
        for j in range(i, 0, -1):
            multi = i * j
            if multi < 10:
                continue
            if multi < response:
                continue
            if isPalindrom(str(multi)):
                # print(multi, "=", i, "x", j)
                response = max(response, multi)
    return response


if __name__ == "__main__":
    print(_main(1000))
