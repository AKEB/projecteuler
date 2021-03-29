"""
Следующая повторяющаяся последовательность определена для множества натуральных чисел:

n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.
https://euler.jakumo.org/problems/view/14.html

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
https://projecteuler.net/problem=14
"""


def generate(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1


def _main(Num: int):
    numbers = [0] * (2 * Num + 1)
    for n in range(2 * Num, 0, -1):
        if numbers[n] > 0:
            continue
        numbers[n] = generate(n)
    max_count = 0
    max_num = 0
    for i in range(2, Num):
        count = 1
        number = i
        while number > 1:
            if number < len(numbers):
                number = numbers[number]
                count += 1
            else:
                number = generate(number)
                count += 1
        if max_count < count:
            max_count = count
            max_num = i

    number = max_num
    while number > 1:
        print(number, end='->')
        number = generate(number)
    print(1)
    return max_num, max_count


if __name__ == "__main__":
    print(_main(1_000_000))
