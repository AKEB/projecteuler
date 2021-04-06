"""
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.
https://euler.jakumo.org/problems/view/21.html

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
https://projecteuler.net/problem=21
"""


def d(N: int) -> int:
    return sum(_prime(N))


def _prime(num: int) -> set:
    """Возвращает делители числа"""
    prime = set()
    for i in range(1, int(((num + 1) ** 0.5))):
        if num % i == 0:
            prime.add(i)
            if i * i != num and i != 1:
                prime.add(num // i)
    return prime


def _main(N: int) -> int:
    numbers = set()
    for i in range(1, N + 1):
        if i in numbers:
            continue
        num = d(i)
        if d(num) == i and num != i:
            numbers.add(i)
            numbers.add(num)
    return sum(numbers)


if __name__ == "__main__":
    print(_main(10000))
