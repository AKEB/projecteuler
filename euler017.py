"""
Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.
https://euler.jakumo.org/problems/view/17.html

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
https://projecteuler.net/problem=17
"""
import re


l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
l2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def numberInEnglish(n: int) -> str:
    if not n:
        return 'zero'
    result = ''
    if n // 1000:
        result += '{} thousand '.format(l1[n // 1000 - 1])
    n = n % 1000
    if n // 100 and n % 100:
        result += '{} hundred and '.format(l1[n // 100 - 1])
    elif n // 100:
        result += '{} hundred'.format(l1[n // 100 - 1])

    if n % 100 <= 19:
        result += l1[n % 100 - 1]
    else:
        if n % 10:
            result += l2[n % 100 // 10 - 2] + '-' + l1[n % 10 - 1]
        else:
            result += l2[n % 100 // 10 - 2]
    return result


def _main(N: int) -> int:
    summ = 0
    for i in range(1, N + 1):
        string = numberInEnglish(i)
        string = re.sub(r"[ -]", "", string)
        summ += len(string)
    return summ


if __name__ == "__main__":
    print(_main(1000))
