"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
https://euler.jakumo.org/problems/view/1.html

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1
"""


def _main() -> int:
    summ = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ


if __name__ == "__main__":
    print(_main())
