"""
Сумма квадратов первых десяти натуральных чисел равна
1^2+2^2+...+10^2=385
Квадрат суммы первых десяти натуральных чисел равен
(1+2+...+10)^2=55^2=3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
https://euler.jakumo.org/problems/view/6.html

The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
https://projecteuler.net/problem=6
"""


def _main(N: int) -> int:
    summary1 = sum([i * i for i in range(N + 1)])
    summary2 = sum(range(N + 1)) ** 2
    return summary2 - summary1


if __name__ == "__main__":
    print(_main(100))
