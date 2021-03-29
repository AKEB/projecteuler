"""
Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
Сколько существует таких маршрутов в сетке 20×20?
https://euler.jakumo.org/problems/view/15.html

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
https://projecteuler.net/problem=15
"""
import pprint


def _main(N: int, M: int) -> int:
    array = [[1 if i * j == 0 else 0 for i in range(N + 1)] for j in range(M + 1)]
    array[0][0] = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            array[i][j] = array[i - 1][j] + array[i][j - 1]
    return array[N][M]
    pass


if __name__ == "__main__":
    print(_main(20, 20))
