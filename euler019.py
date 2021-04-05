"""
Дана следующая информация (однако, вы можете проверить ее самостоятельно):

1 января 1900 года - понедельник.
В апреле, июне, сентябре и ноябре 30 дней.
В феврале 28 дней, в високосный год - 29.
В остальных месяцах по 31 дню.
Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00) является високосным в том и только том случае, если делится на 400.
Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?
https://euler.jakumo.org/problems/view/19.html

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
https://projecteuler.net/problem=19
"""


def _main() -> int:
    days_count = 0
    sunday_counts = 0
    for year in range(1900, 2001):
        leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days = [0, 31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month in range(1, 13):
            if (days_count + 1) % 7 == 0 and 1900 < year < 2001:
                sunday_counts += 1
            # print(year, leap, month, days_count, (days_count + 1) % 7)
            days_count += days[month]
    return sunday_counts


if __name__ == "__main__":
    print(_main())
