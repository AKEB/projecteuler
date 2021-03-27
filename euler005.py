"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
https://euler.jakumo.org/problems/view/5.html

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
https://projecteuler.net/problem=5
"""


def isGoodNum(num) -> bool:
    nums = (19, 18, 17, 16, 14, 13, 11)
    for t in nums:
        if num % t != 0:
            return False
    return True


def _main() -> int:
    response = 20
    while True:
        if isGoodNum(response):
            break
        else:
            response += 20
    return response


if __name__ == "__main__":
    print(_main())
