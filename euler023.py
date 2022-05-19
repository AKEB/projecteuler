"""
Совершенным числом называется число, у которого сумма его делителей равна самому числу.
Например, сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28, что означает,
что число 28 является совершенным числом.

Число n называется недостаточным, если сумма его делителей меньше n, и называется
избыточным, если сумма его делителей больше n.

Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16),
наименьшее число, которое может быть записано как сумма двух избыточных чисел, равно 24.
Используя математический анализ, можно показать, что все целые числа больше 28123 могут быть
записаны как сумма двух избыточных чисел. Эта граница не может быть уменьшена дальнейшим анализом,
даже несмотря на то, что наибольшее число, которое не может быть записано как сумма
двух избыточных чисел, меньше этой границы.

Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел.
https://euler.jakumo.org/problems/view/23.html

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is
called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that
can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown
that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
https://projecteuler.net/problem=23
"""


def _prime(num: int) -> set:
    """Возвращает делители числа"""
    prime = set()
    for i in range(1, int(((num + 1) / 2))):
        if num % i == 0:
            prime.add(i)
            if i * i != num and i != 1:
                prime.add(num // i)
    return prime


def _main(num: int) -> int:
    abundants = set()
    for i in range(1, num + 1):
        s = sum(_prime(i))
        if s > i:
            abundants.add(i)
    finish_set = set()
    for i in range(1, num + 1):
        found = False
        for abundant in abundants:
            if abundant > i:
                break
            if i - abundant > 0 and i - abundant in abundants:
                found = True
                break
        if not found:
            finish_set.add(i)
    return sum(finish_set)


if __name__ == "__main__":
    # from timeit import Timer
    # print(Timer('print(_main(28123))', 'from __main__ import _main').timeit(1))
    print(_main(28123))
