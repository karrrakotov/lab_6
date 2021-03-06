#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

#   В списке, состоящем из целых элементов, вычислить:
#   1) номер максимального элемента списка;
#   2) произведение элементов списка, расположенных между первым и вторым нулевыми элементами.
#   Преобразовать список таким образом, чтобы в первой его половине располагались элементы,
#   стоявшие в нечетных позициях, а во второй половине - элементы, стоявшие в четных позициях.

if __name__ == '__main__':
    a = list(map(int, input("Введите список: ").split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    #   Произведение элементов списка, расположенных между первым и вторым нулевыми элементами.
    lst = []
    for i, item in enumerate(a):
        if item == 0:
            lst.append(i)

    x = lst[0] + 1
    y = lst[1]
    m = 1

    for item in a[x:y]:
        m *= item
    print("Произведение элементов списка, расположенных между первым и вторым нулевыми элементами равно:", m)