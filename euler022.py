"""
Используйте euler022.txt, текстовый файл размером 46 КБ, содержащий более пяти тысяч имен.
Начните с сортировки в алфавитном порядке.
Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в
отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN
(алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке.
Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
https://euler.jakumo.org/problems/view/22.html

Using euler022.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
https://projecteuler.net/problem=22
"""


def _main() -> int:
    names = []
    with open('euler022.txt', 'r') as f:
        data = f.read()
        names = [name.strip('"') for name in data.split(',')]
    names.sort()
    summary = 0
    for index, name in enumerate(names):
        summary += (index + 1) * sum([ord(char) - 64 for char in name.upper()])
    return summary


if __name__ == "__main__":
    print(_main())
