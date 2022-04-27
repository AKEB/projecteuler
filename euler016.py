"""
2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 2**1000?
https://euler.jakumo.org/problems/view/16.html

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
https://projecteuler.net/problem=16
"""


def _main(N: int) -> int:
    number = str(2 ** N)
    summ = 0
    for i in range(len(number)):
        summ += int(number[i])
    return summ


if __name__ == "__main__":
    print(_main(1000))
