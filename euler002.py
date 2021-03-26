"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
https://euler.jakumo.org/problems/view/2.html

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
https://projecteuler.net/problem=2
"""


def _main(N: int) -> int:
    """Возвращает сумму чисел ряда Фибоначчи меньше N"""
    summ = 0
    f1 = 1
    f2 = 1
    while True:
        fib = f1 + f2
        f1, f2 = f2, fib
        if fib > N:
            break
        if fib % 2 == 0:
            summ += fib
    return summ


if __name__ == "__main__":
    print(_main(4000000))
